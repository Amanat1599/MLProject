from src.MLProject.logger import logging
from src.MLProject.exception import CustomException
import sys

if __name__=="__main__":
    logging.info("The execuation has started : ")

    try:
        a=1/0
    except Exception as e:
        logging.info("Custom Exception occur : ")
        raise CustomException(e,sys)