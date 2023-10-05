import os
import sys
import pandas as pd
from src.exception import CustomException
from src.logger import logging
from sklearn.model_selection import train_test_split
from dataclasses import dataclass



@dataclass
class DataIngestionConfig:
      # defining paths for saving the original data to these files
      train_data_path = os.path.join('artifact','train.csv')
      test_data_path =  os.path.join('artifact','test.csv')
      raw_data_path =  os.path.join('artifact','raw.csv')
    
    
class DataIngestion():
        def __init__(self):
              self.ingestion_config = DataIngestionConfig()        
        def initiate_data_ingestion(self):
             logging.info("Data Ingestion starts")
             try:                   
                   # main ingestion code to be written here
                   print("Hello World")
                   df = pd.read_csv(os.path.join('Notebooks/data','gemstone.csv'))
                   logging.info("main data file is read")

                   os.makedirs(os.path.dirname(self.ingestion_config.raw_data_path),exist_ok=True)
                   df.to_csv(self.ingestion_config.raw_data_path,index=False)
                   logging.info('Train test split')
                   train_set,test_set=train_test_split(df,test_size=0.30,random_state=42)
                   train_set.to_csv(self.ingestion_config.train_data_path,index=False,header=True)
                   test_set.to_csv(self.ingestion_config.test_data_path,index=False,header=True)
                   logging.info("train,test and raw data files are created")
                   # since transformation class will be using train and test data thus after ingestion we have to
                   # return paths for train_data and test_data

                   return(
                         self.ingestion_config.train_data_path,
                         self.ingestion_config.test_data_path
                   )
             except Exception as e:
                   logging.info("Exception occured during data ingestion")
                   raise CustomException(e,sys)
             
        
# The following code was just run in the begining to check if the train, test, raw files are created or not
# if __name__ == "__main__":
#       data = DataIngestion()
#       data.initiate_data_ingestion()
      

