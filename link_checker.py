from multiprocessing.pool import ThreadPool as Pool

from arguments import Arguments
from fyle import Fyle
from response_parser import ResponseParser
from process_timer import ProcessTimer
from request_process import RequestProcess


MAX_THREADS = 5
LINK_STATUS_OK = '|---OK---|'
LINK_STATUS_BROKEN = '|-BROKEN-|'


class LinkChecker:

    def __init__(self):

        self.arguments = Arguments()
        self.filename = self.arguments.get_filename()
        self.fyle = Fyle(self.filename)

        self.process_timer = ProcessTimer()


    def get_elapsed_minutes(self):

        return self.process_timer.get_elapsed_minutes()


    def start(self):
        
        lines = self.fyle.get_lines()

        print(f'\n\nTotal Links: {len(lines)}')        

        pool = Pool(MAX_THREADS)

        for line in lines:
            pool.apply_async(self.process_link, (line,))

        pool.daemon = True
        pool.close()
        pool.join()


    def process_link(self, link):

        request_process = RequestProcess(link)
        response = request_process.get()

        response_parser = ResponseParser(response)
        status_code = response_parser.get_status_code()

        link_status = self.get_link_status(status_code)
        
        print(f'{link_status} {link} => {status_code}')


    def get_link_status(self, status_code):

        if status_code == 404:
            return LINK_STATUS_BROKEN

        return LINK_STATUS_OK
