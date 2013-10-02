import urllib
import urllib2
import json
import sys

URL = 'http://n.lkng.me'

HTTP_ERROR = {
    403: 'Permissioned denied'
}


def print_http_error(error):
    try:
        if error.code in HTTP_ERROR:
            print HTTP_ERROR[error.code]
        else:
            print json.loads(error.read())['error']
    except (KeyError, ValueError):
        print 'Could not connect to the api'


def get(key):
    try:
        response = urllib2.urlopen("%s/%s" % (URL, key))
        value = json.load(response)[key]
        response.close()
        print value
    except urllib2.HTTPError, e:
        print_http_error(e)


def post(key, value):
    try:
        response = urllib2.urlopen(
            "%s/%s" % (URL, key),
            data=urllib.urlencode({'value': value})
        )
        response.close()
        print 'Successfully updated %s to be %s' % (key, value)
    except urllib2.HTTPError, e:
        print_http_error(e)


def main():
    if len(sys.argv) == 2:
        get(sys.argv[1])
    elif len(sys.argv) == 3:
        post(sys.argv[1], sys.argv[2])
    else:
        print "Usage:\n - get: memoris <key>\n - update: memoris <key> <value>"


if __name__ == '__main__':
    main()
