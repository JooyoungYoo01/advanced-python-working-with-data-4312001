# # Demonstrate how to customize logging output

# import logging

# # TODO: add another function to log from


# # set the output file and debug level, and
# # TODO: use a custom formatting specification
# logging.basicConfig(filename="output1.log",
#                     level=logging.DEBUG)

# logging.info("This is an info-level log message")
# logging.warning("This is a warning-level message")
##########################################################
# INFO:root:This is an info-level log message
# WARNING:root:This is a warning-level message
##########################################################

# Demonstrate how to customize logging output

import logging

# TODO: add another function to log from


def anotherFunction():
    logging.debug("This is a debug-level log message", extra=extData)


# set the output file and debug level, and
# TODO: use a custom formatting specification
fmtStr = "User: %(user)s %(asctime)s: %(levelname)s: %(funcName)s Line:%(lineno)d %(message)s"
dateStr = "%m/%d/%Y %I:%M:%S %p"
extData = {'user': 'joem@example.com'}

logging.basicConfig(filename="output2.log",
                    level=logging.DEBUG,
                    format=fmtStr,
                    datefmt=dateStr)

logging.info("This is an info-level log message", extra=extData)
logging.warning("This is a warning-level message", extra=extData)
anotherFunction()
##########################################################
# User: joem@example.com 09/11/2023 06:11:48 AM: INFO: <module> Line:43 This is an info-level log message
# User: joem@example.com 09/11/2023 06:11:48 AM: WARNING: <module> Line:44 This is a warning-level message
# User: joem@example.com 09/11/2023 06:11:48 AM: DEBUG: anotherFunction Line:28 This is a debug-level log message
##########################################################
