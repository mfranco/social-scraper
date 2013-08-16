import httplib2
import urllib

class BaseScraper(object):
    def __init__(self, *args, **kwargs):
        self.user_agent = 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)'
        self.encoding = kwargs.get('encoding', 'utf-8')
        self.h = httplib2.Http("/tmp/social.cache")

    def build_url(self, path, params={}):
        url = '{0}{1}'.format(self.base_url, path)
        if params:
            url += urllib.urlencode(params)
        return url

    def post(self, **kwargs):
        headers = kwargs.get('headers', {})
        data = urllib.parse.urlencode(kwargs.get('data', {}))
        headers['User-Agent'] = self.user_agent
        url = self.build_url(kwargs.get('path', ''), params=kwargs.get('params'))
        resp, content = self.h.request(url, 'POST', data, headers=headers)
        str_content = content.decode(self.encoding)
        return resp, str_content

    def get(self, **kwargs):
        headers = kwargs.get('headers', {})
        headers['User-Agent'] = self.user_agent
        url = self.build_url(kwargs.get('path', ''), params=kwargs.get('params'))
        resp, content = self.h.request(url, 'GET', headers=headers)
        return resp, content

    def request(self, url, *args, **kwargs):
        resp, content = self.h.request(url, *args, **kwargs)
        return resp, content
