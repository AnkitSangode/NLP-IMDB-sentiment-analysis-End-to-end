from sentiment_analysis.config.configuration import ConfigurationManager
from sentiment_analysis.components.data_ingestion import DataIngestion
from sentiment_analysis.exception.customException import CustomException
from sentiment_analysis.logger.logger_setup import logger
import sys

class DataIngestionPipeline:
    def main(self):
        try:
            config = ConfigurationManager()
            data_ingestion_config = config.get_data_ingestion_config()
            data_ingestion = DataIngestion(config = data_ingestion_config)
            data_ingestion.download_data()
            data_ingestion.extract_file()
        except Exception as e:
            raise CustomException(e,sys)
        

STAGE_NAME = 'Data Ingestion'

if __name__ == "__main__":
    try:
        logger.info(f">>>>>>>>>>>{STAGE_NAME}<<<<<<<<<< Started")
        obj = DataIngestionPipeline()
        obj.main()
        logger.info(f">>>>>>>>>>>>>{STAGE_NAME} completed <<<<<<<<<<<<<")
    except CustomException as e:
        raise CustomException(e,sys)