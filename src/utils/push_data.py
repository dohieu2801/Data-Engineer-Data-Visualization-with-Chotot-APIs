import requests
import json
import pandas as pd
import yaml
import sys
sys.path.append('../../')
import config
import psycopg2
import pandas as pd
from sqlalchemy import create_engine
from sqlalchemy.sql import text
from sqlalchemy.engine import Engine
import psycopg2.extras as extras


yaml_file = open("/home/ec2-user/thanhthuy/project_thanhthuy/config/config.yaml")
cfg = yaml.load(yaml_file, Loader=yaml.FullLoader)


class push_data:
    def __init__(self, user, host, port,passwd, db):
        self.user = user
        self.host = host
        self.port = port
        self.passwd = passwd
        self.db = db
        # conn_string = 'postgreslq://' + self.user + ':' + self.passwd + '@' + self.host + ':' + str(self.port) + '/' + self.db
        conn_string =  f"postgresql://{user}:{passwd}@{host}:{port}/{db}"
        self.conn_string = conn_string
    def create_table(self,list_df,dict_to_map_tb):
        
        db = create_engine(self.conn_string, echo = True)
        conn = db.connect()
        for i in range(len(list_df)):
            table_name = dict_to_map_tb.get(i)
            list_df[i].to_sql(table_name,con = conn, method='multi',index=False)
        # list_df.to_sql(dict_to_map_tb,con = conn, method='multi',index=False)
        # conn.commit() 
        conn.close()
    def querry(self,table_name):
        conn = psycopg2.connect(self.conn_string)
        conn.autocommit = True
        cursor = conn.cursor()
        sql = '''SELECT * FROM {table_name}'''
        cursor.execute(sql)
        for i in cursor.fetchall():
            print(i)
    def insert_data(self,df,table):
        conn = psycopg2.connect(self.conn_string)
        tuples = [tuple(x) for x in df.to_numpy()]

        cols = ','.join(list(df.columns))
        # SQL query to execute
        query = "INSERT INTO %s(%s) VALUES %%s on conflict do nothing" % (table, cols)
        cursor = conn.cursor()
        try:
            extras.execute_values(cursor, query, tuples)
            conn.commit()
        except (Exception, psycopg2.DatabaseError) as error:
            print("Error: %s" % error)
            conn.rollback()
            cursor.close()
            return 1
        print("the dataframe is inserted")
        cursor.close()
                
