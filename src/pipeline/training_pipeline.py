import sys, os
from src.logger import logging
from src.exception import Customed_exception
from src.components.data_ingestion import DataIngestion

from src.entity.config_entity import DataConfig                                                

from src.entity.artifacts import DataArtifact

class TrainPipeline:
    def __init__(self):
        self.data_ingestion_config = DataConfig()

    
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
        
    def runpipeline(self) -> None:
        try:
            data_ingestion_artifact = self.start_ingestion()
        except Exception as e:
            raise Customed_exception(e, sys)
