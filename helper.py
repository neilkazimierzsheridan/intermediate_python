import logging


logger = logging.getLogger(__name__) #set logger name
#as name of module, not the default name of root
logger.info('Hello from helper!')

#handlers to send the log messages to different places
stream_h = logging.StreamHandler() #send to screen handler
file_h = logging.FileHandler('file.log') #send to file
#handler

# level and format for handlers
stream_h.setLevel(logging.WARNING)
file_h.setLevel(logging.ERROR)

#formatter = logging.Formatter(see docs!)
#stream_h.setFormatter(formatter)
#file_h.setFormatter(formatter)

logger.addHandler(stream_h)
logger.addHandler(file_h)

logger.warning('this is your warning') #log something with
#the logger using the handlers!
logger.error('this is the error!')

#note we can define our loggers and handlers in a .conf
# or .ini and import e.g. logging.config etc.
# call logging.config.fileConfig('logging.conf') or
#can use a dict config