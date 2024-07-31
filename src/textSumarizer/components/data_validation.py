import os 
from textSumarizer.logging import logger
from textSumarizer.config.configuration import DataValidationConfig

class DataValidation:
    def __init__(self, config : DataValidationConfig):
        self.config = config
    
    def validate_all_file_exist(self) -> bool:
        try:
            val_status = None
            all_files = os.listdir(os.path.join("artifacts","data_ingestion","samsum_dataset"))

            for file in all_files:
                if file not in self.config.ALL_FILE_REQUIRED:
                    val_status = False
                    with open(self.config.STATUS_FILE,'w') as f:
                        f.write(f"Validation Status: {val_status}")
                else:
                    val_status = True
                    with open(self.config.STATUS_FILE,'w') as f:
                        f.write(f"Validation Status: {val_status}")
                
            return val_status
            
        except Exception as e:
            raise e
            
