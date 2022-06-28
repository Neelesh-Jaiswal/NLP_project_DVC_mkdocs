from re import S
from src.utils.common import read_yaml
from logger import Logger_class
import argparse

STAGE = "STAGE_NAME" # change stage name as per your pipeline configuration

def main(config_path,
        # params_path=None
        ):
        
    config = read_yaml(config_path)
    # params = read_yaml(params_path)
    return config

if __name__ == "__main__":
    args = argparse.ArgumentParser()
    args.add_argument("--config", "-c", default="configs\config.yaml")
    args.add_argument("--params", "-p", default="params.yaml")
    parsed_args = args.parse_args()

    try:
        Logger_class(f'>>>>>>>>STAGE:{STAGE} STARTED<<<<<<<<<<<')

        # main(config_path=parsed_args.config, params_path=parsed_args.params)
            
        content = main(config_path = parsed_args.config)
        print(content)

        Logger_class(f'>>>>>>>>STAGE:{STAGE} ENDED<<<<<<<<<<<')

    except Exception:
        obj = Logger_class(f'>>>>>>>STAGE: {STAGE} got into error<<<<<<<<')
        obj.log()
        raise
