# -*- coding: utf-8 -*-
import urllib
import urllib2
import json


HTTP_ERROR = {
    403: 'Permissioned denied'
}


def http_error(error):
    try:
        if error.code in HTTP_ERROR:
            return HTTP_ERROR[error.code]
        else:
            return json.loads(error.read())['error']
    except (KeyError, ValueError):
        return 'Could not connect to the api'


class Memoris(object):

    def __init__(self, url):
        self.url = url

    def api_request(self, path, data=None):
        try:
            if data is None:
                response = urllib2.urlopen("%s/%s" % (self.url, path))
            else:
                response = urllib2.urlopen("%s/%s" % (self.url, path), data)
            value = json.load(response)
            response.close()
            return value
        except urllib2.HTTPError, e:
            return http_error(e)

    def get(self, key):
        return self.api_request(key)

    def set(self, key, value):
        return self.api_request(key, data=urllib.urlencode({'value': value}))

    def hgetall(self, name):
        return self.api_request('h/%s' % name)

    def hget(self, name, key):
        return self.api_request('h/%s/%s' % (name, key))

    def hset(self, name, key, value):
        return self.api_request(
            'h/%s/%s' % (name, key),
            data=urllib.urlencode({'value': value})
        )
