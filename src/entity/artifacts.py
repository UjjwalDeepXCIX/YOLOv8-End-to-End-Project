from dataclasses import dataclass

@dataclass
class DataArtifact:
    data_zip_file_path:str
    feature_path:str

@dataclass
class DataCheckArtifact:
    data_status: bool


@dataclass
class ModelTrainerArtifact:
    trained_model_file_path: str
