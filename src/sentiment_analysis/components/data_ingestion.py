import requests
from zipfile import ZipFile
import os
import sys
from sentiment_analysis.logger.logger_setup import logger
from sentiment_analysis.exception.customException import CustomException
from sentiment_analysis.entity.config_entitiy import DataIngestionConfig

class DataIngestion:
    def __init__(self, config: DataIngestionConfig):
        self.config = config

    def download_data(self):
        try:
            data_url = self.config.source_URL
            zip_download_dir = self.config.local_data_file
            os.makedirs(os.path.dirname(zip_download_dir), exist_ok=True)

            logger.info(f"Downloading data from {data_url} into file {zip_download_dir}")
        
            response = requests.get(data_url, stream=True)
            response.raise_for_status()
        
            with open(zip_download_dir, "wb") as f:
                for chunk in response.iter_content(chunk_size=8192):
                    f.write(chunk)
                
            logger.info(f"Download completed and saved to {zip_download_dir}")
        except Exception as e:
            raise CustomException(e, sys)
        
    def extract_file(self):
        unzip_path = self.config.unzip_dir
        os.makedirs(unzip_path,exist_ok=True)
        with ZipFile(self.config.local_data_file,'r') as zip_ref:
            zip_ref.extractall(unzip_path)