import time
import linecache
import sys
import os

import datetime
from core.settings import MARKOV_LOGGING
# Tools for development and logging
# I know that a third party logger is a great idea, but time is time.

DEBUG_TOOLBAR_CONFIG = {
    "SHOW_TOOLBAR_CALLBACK" : lambda request: True,
}


def exception(filename="general_log.txt", exception=True, err=""):
  """ Sends exception to core.errors.general_log.txt, or a user denoted string """
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
          errorFile.write("\n" + exception) # All of the above is a hacky way of receiving the current exception as a string
      errorFile.write("\n")
      errorFile.close()