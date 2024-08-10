from textSumarizer.config.configuration import ConfigurationManager
from textSumarizer.components.model_evaluation import ModelEvaluation
from textSumarizer.logging import logger


class ModelEvalutionPipeline:

    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        model_evaluation_config = config.get_model_evaluation_config()
        model_evaluation_config = ModelEvaluation(config=model_evaluation_config)
        model_evaluation_config.evaluate()
