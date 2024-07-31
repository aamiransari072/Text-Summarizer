from textSumarizer.config.configuration import ConfigurationManager
from textSumarizer.components.data_validation import DataValidation
from textSumarizer.logging import logger

class DataValidationPipeline:
    def __init__(self):
        pass



    def main(self):
        config = ConfigurationManager()
        data_val_config = config.get_data_validation_config()
        data_val = DataValidation(config=data_val_config)
        data_val.validate_all_file_exist()