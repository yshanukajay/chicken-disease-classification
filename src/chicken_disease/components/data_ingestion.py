import os
import urllib.request as request
import zipfile 
from chicken_disease import logger
from chicken_disease.utils.common import get_size
from chicken_disease.entity.config_entity import DataIngestionConfig
from pathlib import Path

class DataIngestion:
    def __init__(self, config : DataIngestionConfig):
        self.config = config

    def download_file(self):
        if not os.path.exists(self.config.local_data_file):
            filename, headers = request.urlretrieve(
                url = self.config.source_URL,
                filename = self.config.local_data_file
            )
            logger.info(f"{filename} downloaded with following info: \n{headers}")
        else:
            logger.info(f"File already exists of size: {get_size(Path(self.config.local_data_file))}")

    def extract_zip_file(self):
        """ 
        zip_file_path: str
        Extracts the zip file to the unzipped_data_dir
        Function returns None
        """
        unzip_path = self.config.unzipped_data_dir
        os.makedirs(unzip_path, exist_ok= True)

        with zipfile.ZipFile(self.config.local_data_file, 'r') as zip_ref:
            zip_ref.extractall(unzip_path)
