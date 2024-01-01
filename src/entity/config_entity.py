import os
from dataclasses import dataclass
from datetime import datetime
from src.constant.parameters import *



@dataclass
class TrainingPipelineConfig:
    artifacts_dir: str = Artifacts



training_pipeline_config:TrainingPipelineConfig = TrainingPipelineConfig() 


@dataclass
class DataConfig:
    data_ingestion_dir: str = os.path.join(
        training_pipeline_config.artifacts_dir, data_ingestion_path
    )

    feature_store_file_path: str = os.path.join(
        data_ingestion_dir, data_features_path
    )

    data_download_url: str = data_url

@dataclass
class DataCheckConfig:
    data_check: str = os.path.join(training_pipeline_config.artifacts_dir, Data_validation)
    data_status: str = os.path.join(data_check, Data_status)
    data_files = Data_files

#@dataclass
#class ModelTrainerConfig:
#    model_trainer_dir: str = os.path.join(
#        training_pipeline_config.artifacts_dir, MODEL_TRAINER_DIR_NAME
#    )

#    weight_name = MODEL_TRAINER_PRETRAINED_WEIGHT_NAME

#    no_epochs = MODEL_TRAINER_NO_EPOCHS

#    yaml_file = data_path
   #batch_size = MODEL_TRAINER_BATCH_SIZE


