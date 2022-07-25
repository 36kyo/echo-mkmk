#!/usr/bin/env python
import argparse
import random
import unicodedata

def text_width(in_txt: str)->int:
    out_width = 0
    for c in in_txt:
        if unicodedata.east_asian_width(c) in 'FWA':
            out_width += 2
        else:
            out_width += 1
    return out_width

def mkmk_unit(look:str)->str:
    # todo 向き指定のときも、ランダムにする
    eye_ball = "◎"
    eye_open = eye_ball
    eye_close = "ー"
    eye_lookback = "  "
    eye_unit_close = "( " + eye_close + " )"
    eye_unit_lookback = "( " + eye_lookback + " )"
    eye_unit_open_l = "(" + eye_open + "  )"
    eye_unit_open_c = "( " + eye_open + " )"
    eye_unit_open_r = "(  " + eye_open + ")"

    eye_unit = ""
    if look == 'c':
        eye_unit = eye_unit_open_c
    elif look == 'l':
        eye_unit = eye_unit_open_l
    elif look == 'r':
        eye_unit = eye_unit_open_r
    else:
        eye_unit = random.choice([eye_unit_lookback, eye_unit_lookback, eye_unit_lookback, eye_unit_lookback, eye_unit_close, eye_unit_open_l, eye_unit_open_c, eye_unit_open_r])
    return eye_unit


def mkmk(in_txt: str, look: str, is_all_front: bool):
    out_txt = ""
    out_header = ""
    out_footer = ""
    out_payload = in_txt
    eye_ball = "◎"
    out_payload_header = "( " + eye_ball + " )" # test
    out_payload_footer = "( " + eye_ball + " )" # test

    mkmk_unit_len = text_width("( " + eye_ball + " )")
    print(mkmk_unit_len)

    out_payloads = out_payload.splitlines()
    payload_max_width = 0
    for s in out_payloads:
        payload_max_width = max(payload_max_width, text_width(s))
    print(payload_max_width)

    out_txt += out_header
    out_p_str = ""
    for i in out_payloads:
        out_p_str = i
        if len(i) < payload_max_width:
            out_p_str += ' ' * (payload_max_width - len(i))
    
    out_txt += out_p_str

    out_header_mkmks = int(payload_max_width/mkmk_unit_len)
    if payload_max_width % mkmk_unit_len != 0:
        out_header_mkmks += 1



    # if is_all_front:
    #     # random
    #     pass
    # else:

    
    # out_header = '(' * payload_max_width
    # out_footer = ')' * payload_max_width

    # out_header = "( ◎ )" * out_header_mkmks + '\n'

    eye_unit = mkmk_unit(look)
    # out_footer = "( ◎ )" * out_header_mkmks + '\n'
    out_header = eye_unit * out_header_mkmks + '\n'
    out_footer = eye_unit * out_header_mkmks + '\n'

    out_txt = out_header + out_txt + '\n' + out_footer
    print(out_txt)

def main():
    psr = argparse.ArgumentParser()
    psr.add_argument('in_txt', default="", help="print txt")
    psr.add_argument('-a', '--all', default=' ', help="look front all")
    psr.add_argument('-l', '--look', default=' ', help="look left(--look l), right(--look r), center(--look c)")
    args = psr.parse_args()

    in_txt = args.in_txt
    is_all_front = args.all
    look_dir = args.look
    mkmk(in_txt, look_dir, is_all_front)

if __name__ == '__main__':
    main()
