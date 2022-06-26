import argparse
from src.utils.common import read_yaml
from logger import Logger_class

STAGE = "STAGE_NAME" ## <<< change stage name


def main(config_path, params_path):
    ## read config files
    config = read_yaml(config_path)
    params = read_yaml(params_path)
    pass


if __name__ == '__main__':
    args = argparse.ArgumentParser()
    args.add_argument("--config", "-c", default="configs/config.yaml")
    args.add_argument("--params", "-p", default="params.yaml")
    parsed_args = args.parse_args()

    try:
        Logger_class("********************")
        Logger_class(f">>>>> stage {STAGE} started <<<<<")
        main(config_path=parsed_args.config, params_path=parsed_args.params)
        Logger_class(f">>>>> stage {STAGE} completed!<<<<<\n")
    except Exception:
        obj = Logger_class('some error')
        obj.log()
        raise