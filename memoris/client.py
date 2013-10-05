# -*- coding: utf-8 -*-
import sys

from memoris.helpers import Memoris

URL = 'http://n.lkng.me'


def main():
    memoris = Memoris(URL)
    if len(sys.argv) == 2:
        print memoris.get(sys.argv[1])
    elif len(sys.argv) == 3:
        if sys.argv[1] == 'h':
            print memoris.hgetall(sys.argv[2])[sys.argv[2]]
        else:
            print memoris.set(sys.argv[1], sys.argv[2])[sys.argv[1]]
    elif len(sys.argv) == 4:
        if sys.argv[1] == 'h':
            print memoris.hget(
                sys.argv[2],
                sys.argv[3]
            )[sys.argv[2]][sys.argv[3]]
    elif len(sys.argv) == 5:
        if sys.argv[1] == 'h':
            print memoris.hset(
                sys.argv[2],
                sys.argv[3],
                sys.argv[4]
            )[sys.argv[2]][sys.argv[3]]
    else:
        print """
              Usage:
              \n - get: memoris <key>
              \n - update: memoris <key> <value>
              """


if __name__ == '__main__':
    main()
