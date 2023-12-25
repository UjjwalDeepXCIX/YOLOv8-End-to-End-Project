import sys, os
from src.logger import logging
from src.exception import Customed_exception
from src.components.data_ingestion import DataIngestion
from src.components.data_validation import DataValidation

from src.entity.config_entity import DataConfig, validationConfig                                            

from src.entity.artifacts import DataArtifact, DataValArtifact

class TrainPipeline:
    def __init__(self):
        self.data_ingestion_config = DataConfig()
        self.data_validation_config = validationConfig()
    
    def start_ingestion(self)-> DataArtifact:
        try: 
            logging.info(
                "Entered the start_data_ingestion method of TrainPipeline class"
            )
            logging.info("Getting the data from URL")

            data_ingestion = DataIngestion(
                data_ingestion_config =  self.data_ingestion_config
            )

            data_ingestion_artifact = data_ingestion.initiate_data_ingestion()
            logging.info(" Data ingestion completed ")

            return data_ingestion_artifact

        except Exception as e:
            raise Customed_exception(e, sys)

    def start_validation(self, data_ingestion_artifact: DataArtifact) -> DataValArtifact:
        logging.info("Initiating Data check")

        try:
            data_validation = DataValidation(
                data_ingestion_artifact=data_ingestion_artifact,
                data_validation_config=self.data_validation_config,
            )

            data_validation_artifact = data_validation.initiate_data_validation()

            logging.info(
                "Exiting the Data Check all required files are present."
            )

            return data_validation_artifact

        except Exception as e:
            raise Customed_exception(e, sys) from e
        
    def runpipeline(self) -> None:
        try:
            data_ingestion_artifact = self.start_ingestion()
            data_validation_artifact = self.start_validation(data_ingestion_artifact= data_ingestion_artifact)
        except Exception as e:
            raise Customed_exception(e, sys)
