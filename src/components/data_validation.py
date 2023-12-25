import os,sys
import shutil
from src.logger import logging
from src.exception import Customed_exception
from src.entity.config_entity import validationConfig
from src.entity.artifacts import (DataArtifact, DataValArtifact)





class DataValidation:
    def __init__(
        self,
        data_ingestion_artifact: DataArtifact,
        data_validation_config: validationConfig,
    ):
        try:
            self.data_ingestion_artifact = data_ingestion_artifact
            self.data_validation_config = data_validation_config

        except Exception as e:
            raise Customed_exception(e, sys) 
        


    
    def validate_all_files_exist(self)-> bool:
        try:
            data_status = None

            all_files = os.listdir(self.data_ingestion_artifact.feature_path)

            for file in all_files:
                if file not in self.data_validation_config.data_files:
                    data_status = False
                    os.makedirs(self.data_validation_config.data_validate, exist_ok=True)
                    with open(self.data_validation_config.data_status, 'w') as f:
                        f.write(f"Validation status: {data_status}")
                else:
                    data_status = True
                    os.makedirs(self.data_validation_config.data_validate, exist_ok=True)
                    with open(self.data_validation_config.data_status, 'w') as f:
                        f.write(f"Validation status: {data_status}")

            return data_status


        except Exception as e:
            raise Customed_exception(e, sys)
        


    
    def initiate_data_validation(self) -> DataValArtifact: 
        logging.info("Checking if required files exists or not")
        try:
            status = self.validate_all_files_exist()
            data_validation_artifact = DataValArtifact(
                data_status=status)

            logging.info("Checking complete")
            logging.info(f"{data_validation_artifact}")

            if status:
                shutil.copy(self.data_ingestion_artifact.data_zip_file_path, os.getcwd())

            return data_validation_artifact

        except Exception as e:
            raise Customed_exception(e, sys)
        
    