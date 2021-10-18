import sys


DEFAULT_QUERY = 'github.com'


class Arguments:

    def __init__(self):
        
        self.args = sys.argv


    def get_organization(self):

        if len(self.args) < 2:
            raise Exception('Organzation / Username missing')
            
        return self.args[1]


    def get_github_token(self):

        if len(self.args) < 3:
          return

        return self.args[2]

    
    def get_search_query(self):

        if len(self.args) < 4:
            return DEFAULT_QUERY

        return self.args[3]