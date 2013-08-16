class TwitterMockRequest(object):
    def request(self, url, *args, **kwargs):
        content = ''
        file_name = ''
        if 'search' in url:
            file_name = 'test/twitter/search_profile.html'

        else:
            file_name = 'test/twitter/profile.html'
        with  open(file_name)  as  f:
            content = f.read()
            f.close()
        return {}, content
