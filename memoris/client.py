import urllib2
import json
import sys

URL = 'http://n.lkng.me'


def get(key):
    try:
        response = urllib2.urlopen("%s/%s" % (URL, key))
        value = json.load(response)[key]
        response.close()
        return value
    except urllib2.HTTPError:
        pass


def post(key):
    try:
        response = urllib2.urlopen("%s/%s" % (URL, key))
        response.close()
    except urllib2.HTTPError:
        print "Could not save value"


def main():
    if len(sys.argv) == 2:
        print get(sys.argv[1])
    elif len(sys.argv) == 3:
        print post(sys.argv[1], sys.argv[2])
    else:
        print "Usage:\n - get: memoris <key>\n - update: memoris <key> <value>"


if __name__ == '__main__':
    main()
