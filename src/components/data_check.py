import os,sys
import shutil
from src.logger import logging
from src.exception import Customed_exception
from src.entity.config_entity import DataCheckConfig
from src.entity.artifacts import (DataArtifact, DataCheckArtifact)





class DataCheck:
    def __init__(
        self,
        data_ingestion_artifact: DataArtifact,
        data_check_config: DataCheckConfig,
    ):
        try:
            self.data_ingestion_artifact = data_ingestion_artifact
            self.data_check_config = data_check_config

        except Exception as e:
            raise Customed_exception(e, sys) 
        


    
    def check_all_files_exist(self)-> bool:
        try:
            data_status = None

            all_files = os.listdir(self.data_ingestion_artifact.feature_path)

            for file in all_files:
                if file not in self.data_check_config.data_files:
                    data_status = False
                    os.makedirs(self.data_check_config.data_validate, exist_ok=True)
                    with open(self.data_check_config.data_status, 'w') as f:
                        f.write(f"Validation status: {data_status}")
                else:
                    data_status = True
                    os.makedirs(self.data_check_config.data_validate, exist_ok=True)
                    with open(self.data_check_config.data_status, 'w') as f:
                        f.write(f"Validation status: {data_status}")

            return data_status


        except Exception as e:
            raise Customed_exception(e, sys)
        


    
    def initiate_data_check(self) -> DataCheckArtifact: 
        logging.info("Checking if required files exists or not")
        try:
            status = self.check_all_files_exist()
            data_check_artifact = DataCheckArtifact(
                data_status=status)

            logging.info("Checking complete")
            logging.info(f"{data_check_artifact}")

            if status:
                shutil.copy(self.data_ingestion_artifact.data_zip_file_path, os.getcwd())

            return data_check_artifact

        except Exception as e:
            raise Customed_exception(e, sys)
        
    