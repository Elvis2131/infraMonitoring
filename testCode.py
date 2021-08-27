import logging


def test(msg, where):
    logger = logging.getLogger(where)
    logging.basicConfig(filename='workin.log', filemode='a', format='%(name)s - %(levelname)s - %(message)s - %(asctime)s',
                    datefmt='%d-%b-%y %H:%M:%S')
    logger.exception(f"{msg}")

