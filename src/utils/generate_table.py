# from utils.crawler import *
import yaml
import sys
sys.path.append('../../')
import config
import yaml
import pandas as pd
yaml_file = open("/home/ec2-user/thanhthuy/project_thanhthuy/config/config.yaml")
cfg = yaml.load(yaml_file, Loader=yaml.FullLoader)

# print(type(cfg['table'].keys()))
# print(cfg['table'].get("user_profile"))
def create_table(DataFrame):
    lst_df = []
    keys = cfg['table'].keys()
    # print(keys)
    for k in keys:
        col = cfg['table'].get(k)
        table = k
        table = DataFrame[col]
        lst_df.append(table)
    return lst_df
    
