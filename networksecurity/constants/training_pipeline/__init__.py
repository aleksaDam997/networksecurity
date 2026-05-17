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

PREPROCESSING_OBJECT_FILE_NAME = 'preprocessing.pkl'

DATA_TRANSFORMATION_DIR_NAME = 'data_transformation'
DATA_TRANSFORMATION_TRANSFORMED_DATA_DIR = 'transformed'
DATA_TRANSFORMATION_TRANSFORMED_OBJECT_DIR = 'transformed_object'

DATA_TRANSFORMATION_IMPUTER_PARAMS = {
    'missing_values': np.nan,
    'n_neighbors': 3,
    'weights': 'uniform',
}

MODEL_TRAINER_DIR_NAME = 'model_trainer'
MODEL_TRAINER_TRAINED_MODEL_DIR = 'trained_model'
MODEL_TRAINER_TRAINED_MODEL_NAME = 'model.pkl'
MODEL_TRAINER_EXPECTED_SCORE = 0.6
MODEL_TRAINER_OVER_FITTING_UNDER_FITTING_THRESHOLD = 0.05

SAVED_MODEL_DIR = 'saved_models'
MODEL_FILE_NAME = 'model.pkl'

TRAINING_BUCKET_NAME = "networksecurity"