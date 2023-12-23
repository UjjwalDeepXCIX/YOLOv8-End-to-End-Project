import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')



list_of_files = [
    "data/.gitkeep",
    "__init__.py",
    "components/__init__.py",
    "components/data_ingestion.py",
    "components/data_validation.py",
    "components/model_trainer.py",
    "constant/__init__.py",
    "constant/training_pipeline/__init__.py",
    "constant/application.py",
    "entity/config_entity.py",
    "entity/artifacts_entity.py",
    "exception/__init__.py",
    "logger/__init__.py",
    "pipeline/__init__.py",
    "pipeline/training_pipeline.py",
    "utils/__init__.py",
    "utils/main_utils.py",
    "templates/index.html",
    "app.py",
    "Dockerfile",
]


for filepath in list_of_files:
    filepath = Path(filepath)

    filedir, filename = os.path.split(filepath)

    if filedir!="":
        os.makedirs(filedir,exist_ok=True)
        logging.info(f"Creating directory: {filedir} for the file {filename}")

    
    if(not os.path.exists(filename)) or (os.path.getsize(filename) == 0):
        with open(filepath, "w") as f:
            pass
            logging.info(f"Creating empty file: {filename}")

    
    else:
        logging.info(f"{filename} is already created")

