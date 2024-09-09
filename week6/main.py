import logging

logging.basicConfig(level=logging.DEBUG,format=' %(levelname)s | %(filename)s| %(lineno)d| %(asctime)s| %(message)s',datefmt = '%d-%m-%y %H:%M:%S', filename="log_paskaita.log",filemode = "a",)
logging.debug("Debug message")
logging.info("Info message")
logging.warning("Warning message")
logging.error("Error message")
logging.critical("Critical message")
logging.basicConfig(level=logging.INFO)

a = 10
b = 0
try:
    c = a/b
except ZeroDivisionError as e:
    logging.error(f"Error. {e}")
try:
    c = "a" / b
except TypeError as e:
    logging.error(f"Error. {e}")

try:
    c = a/b
except ZeroDivisionError as e:
    logging.error(f"Error." , exc_info=True)