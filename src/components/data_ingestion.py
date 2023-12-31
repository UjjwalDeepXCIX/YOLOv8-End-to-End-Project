import os
import sys
import zipfile
import gdown
from src.logger import logging
from src.exception import Customed_exception
from src.entity.config_entity import DataConfig
from src.entity.artifacts import DataArtifact


class DataIngestion:
    def __init__(self, data_ingestion_config: DataConfig = DataConfig()):
        try:
            self.data_ingestion_config = data_ingestion_config
        except Exception as e:
           raise Customed_exception(e, sys)
        

        
    def download_data(self)-> str:
        try: 
            dataset_url = self.data_ingestion_config.data_download_url
            zip_download_dir = self.data_ingestion_config.data_ingestion_dir
            os.makedirs(zip_download_dir, exist_ok=True)
            data_file_name = "data.zip"
            zip_file_path = os.path.join(zip_download_dir, data_file_name)
            logging.info(f"Downloading data from {dataset_url} into file {zip_file_path}")


            file_id = dataset_url.split("/")[-2]
            prefix = 'https://drive.google.com/uc?/export=download&id='
            gdown.download(prefix+file_id,zip_file_path)

            logging.info(f"Data downloading completed successfully")

            return zip_file_path

        except Exception as e:
            raise Customed_exception(e, sys)
        

    
    def extract_zip_file(self,zip_file_path: str)-> str:
        try:
            feature_path = self.data_ingestion_config.feature_store_file_path
            os.makedirs(feature_path, exist_ok=True)
            with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
                zip_ref.extractall(feature_path)
            logging.info(f"Extracting zipped data: {zip_file_path} to dir: {feature_path}")

            return feature_path

        except Exception as e:
            raise Customed_exception(e, sys)
        


    
    def initiate_data_ingestion(self)-> DataArtifact:
        logging.info("initiating data_ingestion ")
        try: 
            zip_file_path = self.download_data()
            feature_path = self.extract_zip_file(zip_file_path)

            data_ingestion_artifact = DataArtifact(
                data_zip_file_path = zip_file_path,
                feature_path = feature_path
            )
            logging.info(f"Data artifacts Extracted successfully: {data_ingestion_artifact}")

            return data_ingestion_artifact

        except Exception as e:
            raise Customed_exception(e, sys)
        