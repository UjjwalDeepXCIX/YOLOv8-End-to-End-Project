import os,sys
import yaml
from src.utils.utils import read_yaml
from src.logger import logging
from src.exception import Customed_exception
from src.entity.config_entity import ModelTrainerConfig
from src.entity.artifacts import ModelTrainerArtifact
from ultralytics import YOLO




class ModelTrainer:
    def __init__(
        self,
        model_trainer_config: ModelTrainerConfig,
    ):
        self.model_trainer_config = model_trainer_config


    

    def initiate_model_trainer(self,) -> ModelTrainerArtifact:
        logging.info("Entered initiate_model_trainer method of ModelTrainer class")

        try:
            logging.info("Unzipping data")
            os.system("unzip data.zip")
            os.system("rm data.zip")
           
            os.system(f"yolo task=detect mode=train model={self.model_trainer_config.weight_name} data={self.model_trainer_config.yaml_file} epochs={self.model_trainer_config.no_epochs} imgsz=800 save=true")


            os.makedirs(self.model_trainer_config.model_trainer_dir, exist_ok=True)
            os.system(f"cp runs/detect/train/weights/best.pt {self.model_trainer_config.model_trainer_dir}/")
           
            os.system("rm -rf yolov8s.pt")
            os.system("rm -rf train")
            os.system("rm -rf valid")
            os.system("rm -rf data.yaml")
            os.system("rm -rf runs")

            model_trainer_artifact = ModelTrainerArtifact(
                trained_model_file_path="Artifacts/model_trainer/best.pt",
            )

            logging.info("Exited initiate_model_trainer method of ModelTrainer class")
            logging.info(f"Model trainer artifact: {model_trainer_artifact}")

            return model_trainer_artifact


        except Exception as e:
            raise Customed_exception(e, sys)

