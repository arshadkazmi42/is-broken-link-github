import time


class ProcessTimer:


    def __init__(self):

        self.start_time = time.time()
        self.elapsed_minutes = None


    def start(self):

        self.start_time = time.time()

    
    def capture_elapsed_minutes(self):

        self.elapsed_minutes = self.convert_to_minutes((time.time() - self.start_time))


    def get_elapsed_minutes(self):

        self.capture_elapsed_minutes()
        
        return self.elapsed_minutes

    
    def convert_to_minutes(self, time):

        return (time / 60)
    