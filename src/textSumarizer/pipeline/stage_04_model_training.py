from textSumarizer.config.configuration import ConfigurationManager
from textSumarizer.components.model_training import ModelTrainer
from textSumarizer.logging import logger

class ModelTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        model_trianing_config = config.get_model_trainer_config()
        model_training = ModelTrainer(config=model_trianing_config)
        model_training.train()