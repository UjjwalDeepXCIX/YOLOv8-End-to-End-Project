import os
from dataclasses import dataclass
from datetime import datetime
from src.constant.training_pipeline import *



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



