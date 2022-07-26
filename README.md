# echo-mkmk

- [echo-mkmk](#echo-mkmk)
  - [How to use](#how-to-use)
    - [look (front / back) all](#look-front--back-all)
    - [align message (left / right)](#align-message-left--right)
    - [gaze (left / center / right)](#gaze-left--center--right)
    - [escape line feed code ```\n```](#escape-line-feed-code-n)
    - [not escape](#not-escape)
    - [show license](#show-license)
    - [no last line feed](#no-last-line-feed)
  - [ミャクミャク's license](#ミャクミャクs-license)

## How to use

### look (front / back) all

```sh
$ python echo-mkmk.py "ワ" -a f
( ー )(◎  )( ー )
(  ◎)  ワ  ( ー )
( ー )(◎  )(  ◎)

```

```sh
$ python echo-mkmk.py "ワ" -a b
(    )(    )(    )
(    )  ワ  (    )
(    )(    )(    )
```

### align message (left / right)

```sh
$ python echo-mkmk.py "ワ" --align l
(    )(  ◎)(    )
(  ◎)ワ    ( ◎ )
( ー )(    )(    )

```

```sh
$ python echo-mkmk.py "ワ" --align r
( ◎ )(    )(    )
(    )    ワ(◎  )
( ー )( ◎ )(  ◎)

```

### gaze (left / center / right)

```sh
$ python echo-mkmk.py "ワ" -a f -g l
(◎  )(◎  )(◎  )
(◎  )  ワ  (◎  )
(◎  )(◎  )(◎  )

```

```sh
$ python echo-mkmk.py "ワ" -a f -g c
( ◎ )( ◎ )( ◎ )
( ◎ )  ワ  ( ◎ )
( ◎ )( ◎ )( ◎ )

```

```sh
$ python echo-mkmk.py "ワ" -a f -g r
(  ◎)(  ◎)(  ◎)
(  ◎)  ワ  (  ◎)
(  ◎)(  ◎)(  ◎)

```

### escape line feed code ```\n```

```sh
$ python echo-mkmk.py "大阪万博\n2025" -e -g c
(    )( ◎ )( ◎ )( ◎ )
( ー )  大阪万博  ( ◎ )
( ー )    2025    ( ◎ )
(    )(    )( ー )(    )

```

( not escape )

```sh
$ python echo-mkmk.py "大阪万博\n2025"
(    )(    )(  ◎)(    )(    )
(    )  大阪万博\n2025  (    )
(  ◎)( ◎ )(◎  )( ◎ )(◎  )
```

### show license

```sh
$ python echo-mkmk.py "ワ" -l
( ー )(    )( ー )
( ー )  ワ  (    )
( ◎ )(    )(    )
©Copyright Japan Association for the 2025 World Exposition, All rights reserved.

```

### no last line feed

```sh
$ python echo-mkmk.py "ワ" -n
(◎  )(    )(    )
(◎  )  ワ  (    )
( ◎ )(    )(  ◎)
```

## ミャクミャク's license

```txt
©Copyright Japan Association for the 2025 World Exposition, All rights reserved.
```
