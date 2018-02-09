import time
import linecache
import sys
import os

import datetime
from dj.settings import MARKOV_LOGGING
# Tools for development and logging purposes.
# I.e custom built profilers and loggers (although third party loggers are probably idea.)

DEBUG_TOOLBAR_CONFIG = {
    "SHOW_TOOLBAR_CALLBACK" : lambda request: True,
}


def exception(err, filename="general_log.txt", exception=False):
  if MARKOV_LOGGING:
      errorFile = open(os.path.join(os.path.dirname(__file__), 'errors', filename), "a")
      startTime = time.time()
      startTime = datetime.datetime.fromtimestamp(startTime) # check 
      errorFile.write("Time: " + str(startTime) + "  ")
      errorFile.write(str(err))
      if exception:
          exc_type, exc_obj, tb = sys.exc_info()
          f = tb.tb_frame
          lineno = tb.tb_lineno
          filename = f.f_code.co_filename
          linecache.checkcache(filename)
          line = linecache.getline(filename, lineno, f.f_globals)
          exception = 'EXCEPTION IN ({}, LINE {} "{}"): {}'.format(filename, lineno, line.strip(), exc_obj)
          errorFile.write("\n" + exception)
      errorFile.write("\n")
      errorFile.close()