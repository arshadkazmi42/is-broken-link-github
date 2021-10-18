import requests


DEFAULT_REQUEST_TIMEOUT = 40

class Request:

    def __init__(self, url):

        self.url = url

    
    def get(self, headers, timeout=DEFAULT_REQUEST_TIMEOUT):

        return requests.get(self.url, headers=headers, timeout=timeout)