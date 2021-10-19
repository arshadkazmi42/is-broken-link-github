class Fyle:

    def __init__(self, filename):

        self.filename = filename
        self.lines = []


    def read_lines(self):

        with open(self.filename) as file:
            self.lines = file.readlines()
            self.lines = [line.rstrip() for line in self.lines]

        return self.lines

    
    def get_lines(self):

        return self.read_lines()