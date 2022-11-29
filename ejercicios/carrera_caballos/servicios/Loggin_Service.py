import logging as log
import sys

def setupLogging(logLevel, filePath):
    log.basicConfig(level=logLevel,
                    format='%(asctime)s: %(levelname)s [%(filename)s:%(lineno)s] %(message)s',
                    datefmt='%I:%M:%S %p',
                    handlers=[
                        log.FileHandler(filePath),
                        log.StreamHandler(sys.stdout)
                    ])