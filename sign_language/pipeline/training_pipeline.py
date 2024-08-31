import sys,os
from sign_language.logger import logging
from sign_language.exception import SignException
from sign_language.components.data_ingestion import DataIngestion
from sign_language.components.data_validation import DataValidation
from sign_language.components.model_trainer import ModelTrainer

from sign_language.entity.config_entity import (DataIngestionConfig,
                                                DataIngestionConfig,ModelTrainerConfig)


from sign_language.entity.artifacts_entity import (DataValidationArtifact,DataIngestionArtifact,ModelTrainerArtifact)


class TrainPipeline:
    def __init__(self):
        self.data_ingestion_config=DataIngestionConfig()
        self.data_ingestion_config=DataIngestionConfig()
    
    
    def start_data_ingestion(self) -> DataIngestionArtifact:
        try:
            logging.info(
                "Entered the start_data_ingestion method of TrainPipeline class"
            )
            logging.info("Getting the data from URL")
            
            data_ingestion = DataIngestion(
                data_ingestion_config = self.data_ingestion_config
            )
            
            data_ingestion_artifact = data_ingestion.initiate_data_ingestion()
            logging.info("Got the data from URL")
            logging.info(
                "Exited the start_data_ingestion method of TrainPipeline class"
            )
            return data_ingestion_artifact
    
        
        
        except Exception as e:
            raise SignException(e, sys)
    def start_data_validation(self,data_ingestion_artifact: DataIngestionArtifact) -> DataValidationArtifact:
     

        logging.info("Entered the start_data_validation method of TrainPipeline class")

        try:
            data_validation = DataValidation(
                data_ingestion_artifact=data_ingestion_artifact,
                data_validation_config=self.data_validation_config,
            )

            data_validation_artifact = data_validation.initiate_data_validation()

            logging.info("Performed the data validation operation")

            logging.info("Exited the start_data_validation method of TrainPipeline class")

            return data_validation_artifact

        except Exception as e:
            raise SignException(e, sys) from e
    
    def start_model_trainer(self) -> ModelTrainerArtifact:
        try:
            model_trainer = ModelTrainer(
                model_trainer_config=self.model_trainer_config,
            )
            model_trainer_artifact = model_trainer.initiate_model_trainer()
            return model_trainer_artifact

        except Exception as e:
            raise SignException(e, sys)
        

        
    
    def run_pipeline(self):
        try:
            data_ingetion_artifacts=  self.start_data_ingestion()  
            data_validation_artifacts=self.start_data_validation(data_ingestion_artifact=data_ingetion_artifacts) 
            # erorr is coming solve it later
            
            if data_validation_artifacts.validation_status ==True:
                model_trainer_artifacts =self.start_model_trainer()
            else:
                raise Exception("your data is not correct format")
        
        
        except Exception as e:
            raise SignException(e, sys)
        