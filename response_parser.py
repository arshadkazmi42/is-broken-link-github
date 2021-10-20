class ResponseParser:

    def __init__(self, response):

        self.response = response


    def get_status_code(self):

        return self.response.status_code