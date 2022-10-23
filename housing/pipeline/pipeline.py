from housing.config.configuration import Configuration
from housing.logger import logging #get_log_file_name
from housing.exception import HousingException


from housing.entity.artifact_entity import DataIngestionArtifact
from housing.entity.config_entity import DataIngestionConfig
from housing.component.data_ingestion import DataIngestion
import os,sys


class Pipeline :#(Thread):
    #experiment: Experiment = Experiment(*([None] * 11))
    #experiment_file_path = None

    def __init__(self, config: Configuration = Configuration() ) -> None:
        try:
            #os.makedirs(config.training_pipeline_config.artifact_dir, exist_ok=True)
            #Pipeline.experiment_file_path=os.path.join(config.training_pipeline_config.artifact_dir,EXPERIMENT_DIR_NAME, EXPERIMENT_FILE_NAME)
            #super().__init__(daemon=False, name="pipeline")
            self.config = config
        except Exception as e:
            raise HousingException(e, sys) from e

    
    def start_data_ingestion(self) -> DataIngestionArtifact:
        try:
            data_ingestion = DataIngestion(data_ingestion_config=self.config.get_data_ingestion_config())
            return data_ingestion.initiate_data_ingestion()     #After execution of this code it will start data ingestion process
        except Exception as e:
            raise HousingException(e, sys) from e         


    def run_pipeline(self):
        try:
            data_ingestion_artifact = self.start_data_ingestion()
        except Exception as e:
            raise HousingException(e,sys) from e
