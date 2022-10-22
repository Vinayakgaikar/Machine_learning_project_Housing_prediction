from housing.entity.config_entity import DataIngestionConfig
from housing.exception import HousingException
import sys , os
from housing.logger import logging

class DataIngestion :

    def __init__(self,data_ingestion_config : DataIngestionConfig):
        try:
            logging.info(f"{'='*20}Data Ingestion log started.{'='*20} ")
            self.data_ingestion_config = data_ingestion_config

        except Exception as e :
            raise HousingException(e,sys)


    def initiate_data_ingestion(self)-> DataIngestionArtifact:
        try:
            #tgz_file_path =  self.download_housing_data()
            #self.extract_tgz_file(tgz_file_path=tgz_file_path)
            #return self.split_data_as_train_test()
            pass
        except Exception as e:
            raise HousingException(e,sys) from e