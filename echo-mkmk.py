#!/usr/bin/env python
import argparse
import random
import unicodedata


def text_width(in_txt: str) -> int:
    out_width = 0
    for c in in_txt:
        if unicodedata.east_asian_width(c) in 'FWA':
            out_width += 2
        else:
            out_width += 1
    return out_width

eye_ball = "◎"

def mkmk_unit(look_dir: str, look_fb: str) -> str:
    # todo 向き指定のときも、ランダムにする
    eye_open = eye_ball
    eye_close = "ー"
    eye_lookback = "  "
    eye_unit_close = "( " + eye_close + " )"
    eye_unit_lookback = "( " + eye_lookback + " )"
    eye_unit_open_l = "(" + eye_open + "  )"
    eye_unit_open_c = "( " + eye_open + " )"
    eye_unit_open_r = "(  " + eye_open + ")"
    eye_unit = ""

    # force look back
    if look_fb == 'b':
        eye_unit = eye_unit_lookback
    # force look front
    elif look_fb == 'f':
        if look_dir== 'c':
            eye_unit = eye_unit_open_c
        elif look_dir== 'l':
            eye_unit = eye_unit_open_l
        elif look_dir== 'r':
            eye_unit = eye_unit_open_r
        else:
            eye_unit = random.choice([eye_unit_close, eye_unit_open_l, eye_unit_open_c, eye_unit_open_r])
    # random
    else:
        if look_dir== 'c':
            eye_unit = random.choice([eye_unit_open_c, eye_unit_close, eye_unit_lookback, eye_unit_lookback])
        elif look_dir== 'l':
            eye_unit = random.choice([eye_unit_open_l, eye_unit_close, eye_unit_lookback, eye_unit_lookback])
        elif look_dir== 'r':
            eye_unit = random.choice([eye_unit_open_r, eye_unit_close, eye_unit_lookback, eye_unit_lookback])
        else:
            eye_unit = random.choice([eye_unit_open_c, eye_unit_open_l, eye_unit_open_r, eye_unit_close, eye_unit_lookback, eye_unit_lookback, eye_unit_lookback, eye_unit_lookback])

    return eye_unit


def mkmk(in_txt: str, look: str, look_dir_fb: str, message_align: str, is_escape: bool, is_show_license: bool, is_no_ln: bool):
    out_header = ""
    out_footer = ""
    out_message = in_txt

    message_align_txt = " "
    # message_align_txt = "_"  # debug
    license_txt = "©Copyright Japan Association for the 2025 World Exposition, All rights reserved."

    mkmk_unit_len = text_width("( " + eye_ball + " )")
    # print(mkmk_unit_len) # debug

    if is_escape:
        out_messages = out_message.replace("\\n", '\n').splitlines()
    else:
        out_messages = out_message.splitlines()

    message_max_width = 0
    for s in out_messages:
        message_max_width = max(message_max_width, text_width(s))
    # print(message_max_width) # debug

    out_header_mkmks = int(message_max_width / mkmk_unit_len)
    if message_max_width % mkmk_unit_len != 0:
        out_header_mkmks += 1
    out_header_len = out_header_mkmks * mkmk_unit_len

    out_messages_formatted = []
    for i in out_messages:
        buf_txt = i
        txt_len_diff = out_header_len - text_width(i)
        if txt_len_diff > 0:
            if message_align == 'l':
                buf_txt = buf_txt + message_align_txt * txt_len_diff
                # buf_txt += "_" * txt_len_diff  # debug
            elif message_align == 'r':
                buf_txt = message_align_txt * txt_len_diff + buf_txt
            else:
                txt_len_diff_half = int(txt_len_diff / 2)
                buf_txt = message_align_txt * txt_len_diff_half + buf_txt + message_align_txt * (txt_len_diff - txt_len_diff_half)
        out_messages_formatted.append(buf_txt)

    out_header = ""
    out_footer = ""
    for i in range(out_header_mkmks+2):
        out_header += mkmk_unit(look, look_dir_fb)
        out_footer += mkmk_unit(look, look_dir_fb)

    out_txt = out_header + '\n'
    for i in out_messages_formatted:
        out_txt += mkmk_unit(look, look_dir_fb) + i + mkmk_unit(look, look_dir_fb) + '\n'
    out_txt += out_footer

    if is_show_license:
        out_txt += '\n' + license_txt

    if is_no_ln:
        print(out_txt, end='')
    else:
        print(out_txt)


def main():
    psr = argparse.ArgumentParser()
    psr.add_argument('in_txt', default="", help="print txt")
    psr.add_argument('-a', '--all', default='', help="look 'f'(front)/'b'(back) all")
    psr.add_argument('--align', default='c', help="align message 'l'(left),'c'(center),'r'(right)")
    psr.add_argument('-e', '--escape_ln', action='store_true', help="escape \\n")
    psr.add_argument('-g', '--gaze', default='', help="gaze 'l'(left),'c'(center),'r'(right)")
    psr.add_argument('-l', '--license', action='store_true', help="print license of ミャクミャク")
    psr.add_argument('-n', '--no_ln', action='store_true', help="not output last \\n")
    args = psr.parse_args()

    mkmk(in_txt=args.in_txt, look=args.gaze, look_dir_fb=args.all, message_align=args.align, is_escape=args.escape_ln, is_show_license=args.license, is_no_ln=args.no_ln)


if __name__ == '__main__':
    main()
