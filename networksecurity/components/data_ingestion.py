from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.logging.logger import logging

from networksecurity.entity.config_entity import DataIngestionConfig
from networksecurity.entity.artifact_entity import DataIngestionArtifact

import os 
import sys
import numpy as np
import pandas as pd
from sqlalchemy import create_engine

from typing import List
from sklearn.model_selection import train_test_split

from dotenv import load_dotenv
load_dotenv()

class DataIngestion:

    def __init__(self, data_ingestion_config: DataIngestionConfig):
        try:
            self.data_ingestion_config = data_ingestion_config
        except Exception as e:
            raise NetworkSecurityException(e, sys)

    def export_data_from_db_as_dataframe(self) -> pd.DataFrame:
        try:
            logging.info("Exporting data from database")
            connection = f'mysql+mysqlconnector://{os.getenv("DB_USER")}:{os.getenv("DB_PASSWORD")}@{os.getenv("DB_HOST")}:{os.getenv("DB_PORT")}/{self.data_ingestion_config.database_name}'
            engine = create_engine(connection)

            query = f"SELECT * FROM {self.data_ingestion_config.table_name}"

            df = pd.read_sql(query, engine)

            if "id" in df.columns.tolist():
                df.drop("id", axis=1, inplace=True)

            df.replace({np.inf: np.nan, -np.inf: np.nan}, inplace=True)

            return df
        except Exception as e:
            raise NetworkSecurityException(e, sys)

    def data_into_feature_store(self, df: pd.DataFrame) -> pd.DataFrame:
        try:
            logging.info("Exporting data into feature store")
            os.makedirs(os.path.dirname(self.data_ingestion_config.feature_store_file_path), exist_ok=True)
            df.to_csv(self.data_ingestion_config.feature_store_file_path, index=False, header=True)

            return df
        except Exception as e:
            raise NetworkSecurityException(e, sys)
        
    def split_data_as_train_test(self, df: pd.DataFrame) -> None:
        try:
            logging.info("Splitting data into train and test sets")
            train_df, test_df = train_test_split(df, test_size=self.data_ingestion_config.train_test_split_ratio)

            os.makedirs(os.path.dirname(self.data_ingestion_config.training_file_path), exist_ok=True)

            train_df.to_csv(self.data_ingestion_config.training_file_path, index=False, header=True)
            test_df.to_csv(self.data_ingestion_config.test_file_path, index=False, header=True)

            logging.info(f"Data split into train and test sets. Train set saved at {self.data_ingestion_config.training_file_path} and test set saved at {self.data_ingestion_config.test_file_path}")  

        except Exception as e:
            raise NetworkSecurityException(e, sys)

    def initiate_data_ingestion(self) -> str:
        try:
            df = self.export_data_from_db_as_dataframe()
            df = self.data_into_feature_store(df)
            self.split_data_as_train_test(df)

            data_ingestion_artifact = DataIngestionArtifact(
                train_file_path=self.data_ingestion_config.training_file_path,
                test_file_path=self.data_ingestion_config.test_file_path
            )

            return data_ingestion_artifact

        except Exception as e:
            raise NetworkSecurityException(e, sys)