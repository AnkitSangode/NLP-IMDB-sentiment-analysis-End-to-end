from sentiment_analysis.config.configuration import ConfigurationManager
from sentiment_analysis.components.data_validation import DataValidation
from sentiment_analysis.exception.customException import CustomException
from sentiment_analysis.logger.logger_setup import logger
import sys

class DataValidationPipeline:
    def main(self):
        try:
            config = ConfigurationManager()
            data_validation_config = config.get_data_validation_config()
            data_validation = DataValidation(config = data_validation_config)
            data_validation.validate()
        except CustomException as e:
            raise CustomException(e,sys)
        

STAGE_NAME = 'Data Ingestion'

if __name__ == "__main__":
    try:
        logger.info(f">>>>>>>>>>>{STAGE_NAME}<<<<<<<<<< Started")
        obj = DataValidationPipeline()
        obj.main()
        logger.info(f">>>>>>>>>>>>>{STAGE_NAME} completed <<<<<<<<<<<<<")
    except CustomException as e:
        raise CustomException(e,sys)