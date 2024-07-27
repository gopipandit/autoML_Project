import os
import logging
from pathlib import Path

# Print current working directory
print(os.getcwd())

# List of files and directories to create
list_of_files = [
    'automl/__init__.py',
    'automl/main.py',
    'automl/config.py',
    'automl/data/__init__.py',
    'automl/data/data_loader.py',
    'automl/data/data_preprocessor.py',
    'automl/features/__init__.py',
    'automl/features/feature_engineer.py',
    'automl/features/feature_selector.py',
    'automl/models/__init__.py',
    'automl/models/model_trainer.py',
    'automl/models/model_evaluator.py',
    'automl/hyperparameter_tuning/__init__.py',
    'automl/hyperparameter_tuning/tuner.py',
    'automl/deployment/__init__.py',
    'automl/deployment/model_deployer.py',
    'automl/deployment/model_monitor.py',
    'automl/utils/__init__.py',
    'automl/utils/decorators.py',
    'automl/utils/logger.py',
    'automl/utils/helpers.py',
    'automl/cli/__init__.py',
    'automl/cli/cli_app.py',
    'tests/__init__.py',
    'tests/test_data_loader.py',
    'tests/test_data_preprocessor.py',
    'tests/test_feature_engineer.py',
    'tests/test_feature_selector.py',
    'tests/test_model_trainer.py',
    'tests/test_model_evaluator.py',
    'tests/test_tuner.py',
    'tests/test_model_deployer.py',
    'tests/test_model_monitor.py',
    'tests/test_helpers.py',
    'data_samples/sample_data.csv',
    'requirements.txt',
    '.env',
    'README.md'
]

# Setup logging
logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s')

for filepath in list_of_files:
    path = Path(filepath)
    filedir = path.parent

    try:
        # Create directory if it doesn't exist
        if filedir:
            os.makedirs(filedir, exist_ok=True)
            logging.info(f"Directory created: {filedir}")

        # Create file if it doesn't exist or is empty
        if not path.exists() or path.stat().st_size == 0:
            path.touch(exist_ok=True)
            logging.info(f"Empty file created: {filepath}")
        else:
            logging.info(f"File already exists: {filepath}")
    except Exception as e:
        logging.error(f"Failed to create {filepath}. Error: {e}")
