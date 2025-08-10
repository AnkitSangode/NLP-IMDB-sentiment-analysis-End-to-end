import pandas as pd
from sentiment_analysis.logger.logger_setup import logger
from sentiment_analysis.config.configuration import DataValidationConfig
import os

class DataValidation:
    def __init__(self,config: DataValidationConfig):
        self.config = config

    def validate(self):
        if not os.path.exists(self.config.datadata_file):
            raise FileNotFoundError(f"Data file not found: {self.config.datadata_file}")

        df = pd.read_csv(self.config.datadata_file)

        if df.empty:
            raise ValueError("Data file is empty")

        required_columns = ['review', 'sentiment']
        for col in required_columns:
            if col not in df.columns:
                raise ValueError(f"Missing required column: {col}")

            missing_values = df.isnull().sum().any()
            if missing_values > 0:
                logger.info("Warning: Missing values found!")

            dup_count = df.duplicated().sum()
            if dup_count > 0:
                logger.info(f"Warning: {df.duplicated().sum()} duplicate rows found!")

       
        with open(self.config.status_file, "w") as f:
            f.write("Data validation: PASSED\n")
            f.write(f"Missing values: {missing_values}\n")
            f.write(f"Duplicates removed: {dup_count}\n")
            

            logger.info("✅ Data validation passed.")
            return True
        