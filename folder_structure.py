import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')



list_of_files = [
    "gitkeep/.gitkeep"
    "data/.gitkeep",
    "src/__init__.py",
    "src/pipeline/__init__.py",
    "src/pipeline/training_pipeline.py",
    "src/utils/__init__.py",
    "src/utils/utils.py",
    "src/components/__init__.py",
    "src/components/data_ingestion.py",
    "src/components/data_validation.py",
    "src/components/model_trainer.py",
    "src/constant/__init__.py",
    "src/constant/training_pipeline/__init__.py",
    "src/constant/application.py",
    "src/entity/config_entity.py",
    "src/entity/artifacts.py",
    "src/exception/__init__.py",
    "src/logger/__init__.py",
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

