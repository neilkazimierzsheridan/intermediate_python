import logging
import traceback

try:
    a = [1,2,3]
    val = a[5] #too large index
except: #so catch everything
    logging.error("The error is %s ", traceback.format_exc())
