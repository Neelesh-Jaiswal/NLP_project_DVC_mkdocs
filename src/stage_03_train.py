import os
from venv import create
from src.utils import read_yaml, create_directories
from logger import Logger_class
import argparse
import joblib
import numpy as np

from sklearn.ensemble import RandomForestClassifier

STAGE = "Training" 

def main(config_path,params_path):
        
    config = read_yaml(config_path)
    params = read_yaml(params_path)
    
    artifacts = config['artifacts']
    featurized_data_dir_path = os.path.join(artifacts['ARTIFACTS_DIR'],artifacts['FEATURIZED_DATA'])
    featurized_train_data_path = os.path.join(featurized_data_dir_path, artifacts['FEATURIZED_DATA_TRAIN'])

    model_dir = artifacts['MODEL_DIR']
    model_dir_path = os.path.join(artifacts['ARTIFACTS_DIR'], model_dir)
    create_directories([model_dir_path])

    model_name = artifacts['MODEL_NAME']
    model_path = os.path.join(model_dir_path, model_name)

    matrix = joblib.load(featurized_train_data_path) # fetching whole matrix: pid, label, text
    labels = np.squeeze(matrix[:,1].toarray()) # fetching label column
    X = matrix[:,2:]  # fetching text column

    Logger_class(f"Input matrix size: {matrix.shape}")
    Logger_class(f"X matrix size: {X.shape}")
    Logger_class(f"Y matrix size: {labels.shape}")

    seed = params['train']['seed']
    n_est = params['train']['n_estimators']
    min_split = params['train']['min_split']
    n_jobs = params['train']['n_jobs']

    model = RandomForestClassifier(n_estimators=n_est, 
                                    min_samples_split=min_split,
                                    n_jobs = n_jobs,
                                    random_state=seed)
    model.fit(X,labels)

    joblib.dump(model,model_path)
    
    Logger_class(f"Saved our model at path: {model_path}")

if __name__ == "__main__":
    args = argparse.ArgumentParser()
    args.add_argument("--config", "-c", default="configs/config.yaml")
    args.add_argument("--params", "-p", default="params.yaml")
    parsed_args = args.parse_args()

    try:
        Logger_class(f'>>>>>>>>STAGE:{STAGE} STARTED<<<<<<<<<<<')

        main(config_path=parsed_args.config, params_path=parsed_args.params)

        Logger_class(f'>>>>>>>>STAGE:{STAGE} ENDED<<<<<<<<<<<')

    except Exception:
        obj = Logger_class(f'>>>>>>>STAGE: {STAGE} got into error<<<<<<<<')
        obj.log()
        raise
