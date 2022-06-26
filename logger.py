from datetime import datetime
import os

import linecache
import sys
import traceback as tb


class Logger_class:
    """"

    This class will be used for handling the logs across whole application.

    """
    def __init__(self, log_message):
        self.now = datetime.now()
        self.date = self.now.date().strftime('%d/%b/%y')
        self.file_date = self.now.date().strftime('%d_%m_%y')
        self.current_time = self.now.strftime("%H:%M:%S")
        self.log_message = log_message
        file = open("logs/running_logs.log", 'a+', encoding='utf-8')

        file.write(str(self.date) + ' ➙ ' + str(self.current_time) + " ➥ " + self.log_message + "\n")
        file.close()

    def log(self):
        exc_type, exc_obj, tb = sys.exc_info()
        f = tb.tb_frame
        lineno = tb.tb_lineno
        filename = f.f_code.co_filename
        linecache.checkcache(filename)
        file = open("logs/running_logs.log", 'a+', encoding='utf-8')
        file.write('EXCEPTION IN ({}, LINE {} ):\n {}  \n'.format(filename, lineno, exc_obj))
        file.close()


# if __name__ == '__main__':
#     obj = Logger_class('doing logging')
#     obj.log()