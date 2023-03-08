import yaml
import sys
sys.path.append('../../')
import config
from datetime import datetime, timedelta
# from crawler import *
# from generate_table import *

yaml_file = open("/home/ec2-user/thanhthuy/project_thanhthuy/config/config.yaml")
cfg = yaml.load(yaml_file, Loader=yaml.FullLoader)



def rename_col_remove_dup(df,dict_cols):
    new_df = df.rename(dict_cols,axis = 1)
    new_df = new_df.dropna(axis=0, how='all')
    new_df = new_df.drop_duplicates(subset = ['id'],keep = 'last')
    return new_df
def cal_size(df_property):
    df_property['sizes'] = df_property['price']/(df_property['price_million_per_m2']*1000) 
    return df_property
def cal_times(df_dates):
    df_dates['time'] = df_dates['id'].apply(lambda x: datetime.utcfromtimestamp(x / 1e3))
    df_dates['date'] = df_dates['time'].apply(lambda x: x.date())
    df_dates['day'] = df_dates['time'].apply(lambda x: x.day)
    df_dates['month'] = df_dates['time'].apply(lambda x: x.month)
    df_dates['year'] = df_dates['time'].apply(lambda x: x.year)
    return df_dates

def split_process_df(DataFrame):
    lst_df = []
    lst_replace = cfg['process']
    lst_key = list(cfg['process'].keys())
    for i in range(len(lst_key)):
        new_df = rename_col_remove_dup(DataFrame[i],lst_replace.get(lst_key[i]))
        if i ==0:
            new_df = cal_size(new_df)
        elif i==7:
            new_df = cal_times(new_df)
        lst_df.append(new_df)
    return lst_df
    