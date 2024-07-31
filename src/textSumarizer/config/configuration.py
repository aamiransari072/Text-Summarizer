from textSumarizer.constants import *
from textSumarizer.utils.common import read_yaml, create_directories
from textSumarizer.entity import DataIngestionConfig
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