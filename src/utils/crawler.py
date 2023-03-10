import requests
import json
import pandas as pd
import yaml
import sys
sys.path.append('../../')
import config
import yaml

## offset là bỏ qua số lượng item, vậy thì mỗi vòng lặp sẽ lấy limit là 100 và thực hiện xong sẽ tăng 100 offset
## gọi 1000 item, với mỗi vòng lặp là 100 item sẽ phải thực hiện 10 vòng lặp
yaml_file = open("/home/ec2-user/thanhthuy/project_thanhthuy/config/config.yaml")
cfg = yaml.load(yaml_file, Loader=yaml.FullLoader)
def crawler():
    cate_list = cfg['data']['categories']
    offset = cfg['data']['offset']
    limit = cfg['data']['limit']
    href = cfg['href']
    data_crawl = []
    df = pd.DataFrame()
    for cate in range(len(cate_list)):
        offset_var = 0
        limit_var = 100
        categories = cate_list[cate]
        for i in range(0, 200):
            response_API = requests.get(href + "limit=" + str(offset) + "&o=" + str(limit) + "&cg=" + str(categories) + "&st=s,k")
            if response_API.status_code==200:
                data = response_API.text
                # json_load = json.loads(data.replace('}]}"},', '}]}"}'))
                json_load = json.loads(data)
                if df.shape[0] == 0:
                    df = pd.json_normalize(json_load['ads'])
                else:
                    new_df = pd.json_normalize(json_load['ads'])
                    df = df.append(new_df)
                offset_var = offset_var + limit_var
    cate = cate + 1
    return df
