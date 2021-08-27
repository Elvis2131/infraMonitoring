"""
Author: Lartey Elvis
Date: 27th Aug, 2021
Description: Parsing and storing app logs.
"""

try:
    import logging, os
except ImportError as e:
    print(f"Failure:{0}".format(e))

appLogdir = 'scriptLogs'


def directoryCreation(dirName=appLogdir):
    """
    Description: Checks if the logs folder exists.
    @rtype: None
    """
    if not os.path.isdir(dirName):
        try:
            os.mkdir(dirName)
            print('Directory was created successfully.')

        except OSError as e:
            print(f"Failure: {e}")

    return dirName


def saveLog(fileInvoke=None, funcInvoke=None, msg=None):
    """
    Description: Parses the info received from the script to store log.
    @rtype: None
    """
    fileexten: str = '.py'

    fileName: str = f'{directoryCreation()}/{fileInvoke.strip(fileexten)}.logs'

    logging.basicConfig(filename=fileName, filemode='a',
                        format=f'{funcInvoke} - %(message)s - %(asctime)s',
                        datefmt='%d-%b-%y %H:%M:%S')
    try:
        logging.error(f"{msg}")
    except Exception as e:
        logging.warning('Program Failure:{0}'.format(e))
