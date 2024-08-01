from textSumarizer.constants import *
from textSumarizer.utils.common import read_yaml, create_directories
from textSumarizer.entity import DataIngestionConfig , DataValidationConfig , DataTransformationConfig
from box import ConfigBox



class ConfigurationManager:
    def __init__(
            self,
            config_filepath = CONFIG_FILE_PATH,
            params_filepath = PARAMS_PATH):
        
        try:

            print(f"Loading config from: {config_filepath}")
            self.config = ConfigBox(read_yaml(config_filepath))
            print(f"Config loaded: {self.config}")

            self.params = ConfigBox(read_yaml(params_filepath))
            create_directories([self.config.artifacts_root])

        except Exception as e:
            print(f"Error during configuration loading: {e}")
            raise



    def get_data_ingestion_config(self) -> DataIngestionConfig:

        config = self.config.data_ingestion
        
        create_directories([config.root_dir])

        data_ingestion_config = DataIngestionConfig(
            root_dir = config.root_dir,
            source_url = config.source_url,
            local_data_file = config.local_data_file,
            unzip_dir = config.unzip_dir
        ) 

        return data_ingestion_config
    
    def get_data_validation_config(self) -> DataValidationConfig:
        config = self.config.data_validation

        create_directories([config.root_dir])

        data_validation_config = DataValidationConfig(
            root_dir= config.root_dir,
            STATUS_FILE= config.STATUS_FILE,
            ALL_FILE_REQUIRED= config.ALL_FILE_REQUIRED
        )

        return data_validation_config
    
    def get_data_transformation_config(self) -> DataTransformationConfig:
        config = self.config.data_transformation

        create_directories([config.root_dir])

        data_transformation_config = DataTransformationConfig(
            root_dir = config.root_dir,
            data_path =  config.data_path,
            tokenizer_name = config.tokenizer_name 

        )
        return data_transformation_config





