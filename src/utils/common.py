import pandas as pd
import yaml
from logger import Logger_class
import os
import json

def read_yaml(path_to_yaml:str)->str:
    with open(path_to_yaml) as yaml_file:
        content = yaml.safe_load(yaml_file)
    
    Logger_class(f"yaml file: {path_to_yaml} loaded successfully")
    return content

def create_directories(path_to_directories: list) -> None:
    for path in path_to_directories:
        os.makedirs(path, exist_ok = True)
        
        Logger_class(f"directories: {path} created successfully")

def save_json(path:str, data:dict)->None:
    with open(path, "w") as f:
        json.dump(data, f, indent=4)
    
    Logger_class(f"json file: {path} saved successfully")

def get_df(path_to_data:str, 
            sep:str='\t',
            # column_names:list=['id','label','text'],
            encoding='utf-8')-> pd.DataFrame:
            
    df = pd.read_csv(
                    path_to_data, 
                    delimiter=sep, 
                    encoding=encoding
                    # ,header=None
                    # ,names = column_names
                    )

    Logger_class(f'The input dataframe from {path_to_data} of size {df.shape} is read')
    return df

# if __name__ == "__main__":
    # print(read_yaml("configs\config.yaml"))
    # create_directories(['src\qwerty','blahblah'])
    # save_json('configs\sample_json',{'q':'1','w':'2'})