import time

from arguments import Arguments
from request import Request
from sleep import Sleep


KEY_HEADER_AUTHORIZATION = 'Authorization'
KEY_HEADER_AUTHORIZATION_TOKEN = 'token'
KEY_RATE_LIMIT_REMAINING = 'X-RateLimit-Remaining'
KEY_RATE_LIIMIT_RESET = 'X-RateLimit-Reset'
KEY_RETRY_AFTER = 'Retry-After'


class RequestProcess:

    def __init__(self, url):
        
        self.request = Request(url)

        self.arguments = Arguments()
        self.sleep = Sleep()

    
    def get(self, headers=None, timeout=None):

        if not headers:
            headers = self.format_request_headers()

        response = self.request.get(headers, timeout)

        if response.status_code == 429:

            if self.is_wait_limit(response):

                return self.get(headers, timeout)

        if response.status_code == 403:

            if self.is_github_ratelimit(response):

                return self.get(headers, timeout)

        return response


    def format_request_headers(self):

        headers = {}
        github_token = self.arguments.get_github_token()

        if github_token:
            headers[KEY_HEADER_AUTHORIZATION] = f'{KEY_HEADER_AUTHORIZATION_TOKEN} {github_token}'

        return headers


    def is_wait_limit(self, response):

        sleep_time = None

        if KEY_RETRY_AFTER in response.headers:

            sleep_time = int(response.headers[KEY_RETRY_AFTER])

        self.sleep.start(sleep_time)

        return False


    def is_github_ratelimit(self, response):

        if KEY_RATE_LIMIT_REMAINING in response.headers:

            limit_remaining = int(response.headers[KEY_RATE_LIMIT_REMAINING])
            
            if limit_remaining == 0 and KEY_RATE_LIMIT_RESET in response.headers:

                reset_time = int(response.headers[KEY_RATE_LIMIT_RESET])
                current_time = int(time.time())
                sleep_time = reset_time - current_time + 1
                return self.sleep.start(sleep_time)
                        
        return False