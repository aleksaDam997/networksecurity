import os
import sys
import pandas as pd
import numpy as np

"""
DEFINING COMMON CONSTANT VARIABLES FOR TRAINING PIPELINE
"""

TARGET_COLUMN = 'Result'
PIPELINE_NAME: str = 'NetworkSecurity'
ARTIFACT_DIR: str = 'Artifacts'
FILE_NAME: str = 'phisingData.csv'
TRAIN_FILE_NAME: str = 'train.csv'
TEST_FILE_NAME: str = 'test.csv'

"""
DATA INGESTION RELATED CONSTANTS
"""

DATA_INGESTION_TABLE_NAME = "network_data"
DATA_INGESTION_DATABASE_NAME = "network_data_ml_db"
DATA_INGESTION_DIR_NAME = 'data_ingestion'
DATA_INGESTION_FEATURE_STORE_DIR = 'feature_store'
DATA_INGESTION_INGESTED_DIR = 'ingested'
DATA_INGESTION_TRAIN_TEST_SPLIT_RATION: float = 0.2

SCHEMA_FILE_PATH = os.path.join('data_schema', 'schema.yaml')

DATA_VALIDATION_DIR_NAME = 'data_validation'
DATA_VALIDATION_VALID_DIR = 'validated'
DATA_VALIDATION_INVALID_DIR = 'invalid'
DATA_VALIDATION_DRIFT_REPORT_DIR = 'drift_report'
DATA_VALIDATION_DRIFT_REPORT_FILE_NAME = 'report.yaml'