import sys
import os
from src.exception import Customed_exception
from src.logger import logging 
from src.pipeline.training_pipeline import TrainPipeline

obj = TrainPipeline()
obj.runpipeline()
print("data ingestion completed successfully")
print()
print("data checks completed")
 