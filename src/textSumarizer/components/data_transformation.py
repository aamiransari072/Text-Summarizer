import os 
from textSumarizer.logging import logger
from transformers import AutoTokenizer
from datasets import load_dataset , load_from_disk
from textSumarizer.config.configuration import DataTransformationConfig


class DataTransformation:
    def __init__(self, config: DataTransformationConfig):
        self.config = config
        self.tokenizer = AutoTokenizer.from_pretrained(config.tokenizer_name)
    
    def convert_example_to_features(self,example_batch):
        input_encoding = self.tokenizer(example_batch['dialogue'], max_length = 1024, truncation= True)

        with self.tokenizer.as_target_tokenizer():
            target_encoding = self.tokenizer(example_batch['summary'], max_length = 1024 , truncation= True)

        
        return {
            'input_id' : input_encoding['input_ids'],
            'attention_mask' : input_encoding['attention_mask'],
            'labels' : target_encoding['input_ids']
        }
    
    def convert(self):
        data_samsum = load_from_disk(self.config.data_path)
        data_samsum_pt = data_samsum.map(self.convert_example_to_features , batched = True)
        data_samsum_pt.save_to_disk(os.path.join(self.config.root_dir,"samsum_dataset"))