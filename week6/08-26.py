import logging

def sum(a,b) :
    logging.warning(f"Atliekama suma: {a} + {b}")
    print("Sum function!")
    return a + b

sum(1,2)

logging.basicConfig(level=logging.DEBUG,format='%(filename)s| %(lineno)d')
logging.debug("Debug message")
logging.info("Info message")
logging.warning("Warning message")
logging.error("Error message")
logging.critical("Critical message")
logging.basicConfig(level=logging.INFO)

# https://docs.python.org/3/library/logging.html#formatter-objects

