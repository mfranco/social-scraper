class FacebookMockRequest(object):
    def request(self, url, *args, **kwargs):
        content = ''
        file_name = ''
        if 'search.php' in url:
            file_name = 'test/facebook/search_profile.html'

        else:
            file_name = 'test/facebook/profile.html'
        with  open(file_name)  as  f:
            content = f.read()
            f.close()
        return {}, content
