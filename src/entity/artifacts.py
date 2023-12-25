from dataclasses import dataclass

@dataclass
class DataArtifact:
    data_zip_file_path:str
    feature_path:str

@dataclass
class DataValArtifact:
    data_status: bool
