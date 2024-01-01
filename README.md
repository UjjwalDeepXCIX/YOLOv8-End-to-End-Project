# YOLOv8-End-to-End-Project

An End to End Segmentation project using YOLOv8 model by Ujjwal Deep.

This application allows you to upload images of grocery shelves and predicts the blank spaces on the shelves using YOLOv8 model.

## How to Run?

Follow these steps to run the project:

1. Clone the repository:
    ```bash
    git clone https://github.com/your-username/YOLOv8-End-to-End-Project.git
    ```

2. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

3. Run the application:
    ```bash
    python app.py
    ```

## Model Training

The notebook for training the model is available on the cloud at [link](insert_cloud_training_notebook_link_here).

To use a pre-trained model:
- Train the model on the cloud platform and download the `best.pt`.
- Copy the downloaded `best.pt` file into the `weights` folder of this project.

Alternatively, you can:
- Uncomment the model training sections in the notebook and follow the folder structure to train the model.

Please ensure you have the necessary dataset and annotations for training the model.

## Folder Structure
# Project Folder Structure Explanation

- `src/`: Root directory containing project source code.
  - `components/`: Houses modules responsible for specific project components.
    - `data_aquisation.py`: Module managing data acquisition processes.
    - `data_check.py`: Module handling data validation and checks.
    - `model_trainer.py`: Module dedicated to training the model.
  - `constant/`: Stores constants and configurations for the project.
    - `training_pipeline/`: Subdirectory holding constants related to the training pipeline.
  - `entity/`: Manages entity-related classes or structures for the project.
    - `artifacts.py`: Module responsible for handling artifacts.
    - `config_entity.py`: Module defining the configuration entity.
  - `exception/`: Handles exception-related functionality for the project.
  - `logger/`: Contains functionality related to logging in the project.
  - `pipeline/`: Houses modules relevant to the project's pipeline.
    - `Training_pipeline.py`: Module managing and orchestrating the training pipeline.
  - `utils/`: Stores utility functions and helper modules for the project.


# Image Results
result_image_paths = [
    "path/to/result_image_1.jpg",
    "path/to/result_image_2.jpg",
    "path/to/result_image_3.jpg",
]

result_image_urls = [
    "https://example.com/result_image_1.jpg",
    "https://example.com/result_image_2.jpg",
    "https://example.com/result_image_3.jpg",
]


