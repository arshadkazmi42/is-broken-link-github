import random
import time


WAIT_SECONDS_RANGE_START = 300
WAIT_SECONDS_RANGE_END = 1000

class Sleep:

    def __init__(self):

        self.wait_seconds = self.get_random_seconds()

    
    def get_random_seconds(self):

        return random.randint(WAIT_SECONDS_RANGE_START, WAIT_SECONDS_RANGE_END)


    def start(self, seconds=None):

        if not seconds:
            seconds = self.wait_seconds

        print(f'\nRandom wait. Sleeping for {seconds} seconds.\n')
        time.sleep(seconds)
        
        return True