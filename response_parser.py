class GithubResponseParser:

    def __init__(self, response):

        self.response = response


    def get_status_code(self):

        if not self.response:
            return None

        return self.response.status_code