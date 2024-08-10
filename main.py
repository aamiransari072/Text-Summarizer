from textSumarizer.logging import logger
from textSumarizer.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline 
from textSumarizer.pipeline.stage_02_data_validation import DataValidationPipeline
from textSumarizer.pipeline.stage_03_data_transformation import DataTransformationPipeline
from textSumarizer.pipeline.stage_04_model_training import ModelTrainingPipeline
from textSumarizer.pipeline.stage_05_model_evaluation import ModelEvalutionPipeline

STAGE_NAME = "Data Ingestion stage"
try:
   logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<") 
   data_ingestion = DataIngestionTrainingPipeline()
   data_ingestion.main()
   logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
        logger.exception(e)
        raise e

STAGE_NAME = "Data Validation stage"
try:
   logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<") 
   data_validation = DataValidationPipeline()
   data_validation.main()
   logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
        logger.exception(e)
        raise e

STAGE_NAME = "Data Transformation stage"
try:
   logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<") 
   data_transformation = DataTransformationPipeline()
   data_validation.main()
   logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
        logger.exception(e)
        raise e


# STAGE_NAME = "Model Training stage"
# try:
#    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<") 
#    model_training = ModelTrainingPipeline()
#    model_training.main()
#    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
# except Exception as e:
#         logger.exception(e)
#         raise e


STAGE_NAME = "Model Evalution stage"
try:
   logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<") 
   model_training = ModelEvalutionPipeline()
   model_training.main()
   logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
        logger.exception(e)
        raise e