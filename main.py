from sentiment_analysis.logger.logger_setup import logger
from sentiment_analysis.exception.customException import CustomException
from sentiment_analysis.pipeline.stage_01_data_ingestion import DataIngestionPipeline
import sys

STAGE_NAME = 'Data Ingestion'

if __name__ == "__main__":
    try:
        logger.info(f">>>>>>>>>>>{STAGE_NAME}<<<<<<<<<< Started")
        obj = DataIngestionPipeline()
        obj.main()
        logger.info(f">>>>>>>>>>>>>{STAGE_NAME} completed <<<<<<<<<<<<<")
    except CustomException as e:
        raise CustomException(e,sys)