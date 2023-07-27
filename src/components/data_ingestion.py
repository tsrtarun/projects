import os
import sys
from src.exception import CustomException
from src.logger import logging
import pandas as pd

from sklearn.model_selection import train_test_split
from dataclasses import dataclass

#from src.components.data_transformation import DataTransformation
#from src.components.data_transformation import DataTransformationConfig

@dataclass
class DataIngestionConfig:
    train_data_path : str = os.path.join('artifacts', 'train.csv')
    test_data__path : str = os.path.join('artifacts', 'test.csv')
    raw_data_path: str=os.path.join('artifacts',"data.csv")

class DataIngestion:
    def __init__(self):
        self.ingestion_config = DataIngestionConfig()

    def initate_data_ingestion(self):
        logging.info("Data ingestion started")
        
        try:
            df = pd.read_csv('notebook/data/studs.csv')
            logging.info('Read the dataset')

            #make a folder with specified path of artifacts train.csv
            os.makedirs(os.path.dirname(self.ingestion_config.train_data_path), exist_ok= True)

            df.to_csv(self.ingestion_config.raw_data_path, index = False, header = True)
            logging.info('Raw data CSV file created in artifacts folder')

            logging.info("Train test split initiated")
            train_set,test_set=train_test_split(df,test_size=0.2,random_state=42)

            train_set.to_csv(self.ingestion_config.train_data_path,index=False,header=True)

            test_set.to_csv(self.ingestion_config.test_data__path, index = False, header = True)

            logging.info('All csv files are saved in attributes folder')

            return(
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data__path
            )
        
        except Exception as e:
            raise CustomException(e,sys)
            pass

if __name__ == "__main__":
    obj = DataIngestion()
    obj.initate_data_ingestion()
