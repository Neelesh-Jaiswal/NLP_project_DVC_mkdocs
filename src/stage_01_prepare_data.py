import os
from fsutil import create_dir
# from src.utils.common import read_yaml, create_directories
# from src.utils.data_mgmt import process_posts
from src.utils import read_yaml, create_directories, process_posts
from logger import Logger_class
import argparse
import random

STAGE = "Prepare_data"

def main(config_path,params_path):
        
    config = read_yaml(config_path)
    params = read_yaml(params_path)

    source_data_dir = config['source_data']['data_dir']
    source_data_file = config['source_data']['data_file']
    source_data_path = os.path.join(source_data_dir,source_data_file)

    split = params['prepare']['split']
    seed = params['prepare']['seed']
    tag = params['prepare']['tag']

    random.seed(seed)

    artifacts = config['artifacts']
    prepared_data_dir_path = os.path.join(artifacts['ARTIFACTS_DIR'],artifacts['PREPARED_DATA'])
    create_directories([prepared_data_dir_path])

    train_data_path = os.path.join(prepared_data_dir_path,artifacts['TRAIN_DATA'])
    test_data_path = os.path.join(prepared_data_dir_path,artifacts['TEST_DATA'])

    encode = 'utf-8'
    with open(source_data_path,"r", encoding=encode) as fd_in: # actual input data that we are reading
        with open(train_data_path,"w", encoding=encode) as fd_out_train: # writing train data
            with open(test_data_path,"w", encoding=encode) as fd_out_test: # writing test data
                process_posts(fd_in, fd_out_train, fd_out_test, tag, split)

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
