from utils.crawler import *
from utils.generate_table import *
from utils.process import *
from utils.push_data import *
import yaml
import sys
sys.path.append('../../')
import config

import logging

logging.basicConfig(filename="/home/ec2-user/thanhthuy/project_thanhthuy/log/logging.log",
                    format='%(asctime)s %(message)s',
                    filemode='w')
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

yaml_file = open("/home/ec2-user/thanhthuy/project_thanhthuy/config/config.yaml")
cfg = yaml.load(yaml_file, Loader=yaml.FullLoader)

server_info = cfg['postgre']
user = server_info['user']
host = server_info['host']
port = server_info['port']
passwd = server_info['passwd']
db = server_info['db']
map_info = cfg['user_map']


def main():
    try:
        df = crawler()
        logger.info(f'Crawl sucessful -------------------------')
        list_dataframe= create_table(df)
        logger.info(f'generate sucess -------------------------')
        list_dataframe_process = split_process_df(list_dataframe)
        logger.info(f'Process complete -------------------------')
        a = push_data(user,host,port,passwd,db)
        for i in range(len(list_dataframe_process)):
            a.insert_data(list_dataframe_process[i],map_info[i])
            logger.info(f'Successully insert {map_info[i]}')
    except Exception as e:
        logger.error(f'Fail with error {e}')
        # logger.error(f'Fail to insert {map_info[i]} with error {e}')
        pass
if __name__ == "__main__":
    main()