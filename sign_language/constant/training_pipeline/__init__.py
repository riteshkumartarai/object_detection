import os

ARTIFACTS_DIR: str ="artifacts"

DATA_INGETION_DIR_NAME="data_ingetion"
DATA_INGETION_FEATURE_STORE_DIR="feature_store"

DATA_DOWNLOAD_URL="https://github.com/entbappy/Branching-tutorial/raw/master/Sign_language_data.zip"


"""
Data Validation realted contant start with DATA_VALIDATION VAR NAME
"""

DATA_VALIDATION_DIR_NAME: str = "data_validation"

DATA_VALIDATION_STATUS_FILE = 'status.txt'

DATA_VALIDATION_ALL_REQUIRED_FILES = ["train", "test", "data.yaml"]


"""
MODEL TRAINER related constant start with MODEL_TRAINER var name
"""
MODEL_TRAINER_DIR_NAME: str = "model_trainer"

MODEL_TRAINER_PRETRAINED_WEIGHT_NAME: str = "yolov5s.pt"

MODEL_TRAINER_NO_EPOCHS: int = 1

MODEL_TRAINER_BATCH_SIZE: int = 16