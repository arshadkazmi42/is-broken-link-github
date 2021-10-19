import sys


class Arguments:

    def __init__(self):
        
        self.args = sys.argv


    def get_filename(self):

        if len(self.args) < 2:
            raise Exception('Filename missing')
            
        return self.args[1]


    def get_github_token(self):

        if len(self.args) < 3:
          return

        return self.args[2]
