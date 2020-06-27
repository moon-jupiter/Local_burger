
#!/usr/bin/env python
import sys
import pandas as pd
import pymongo
import json
import os



def import_content(filepath):
    client = MongoClient('mongodb://test:test@localhost',27017) db = client.dbsparta
    mng_db = mng_client['dbsparta'] #Replace mongo db name
    collection_name = 'localburger' #Replace mongo db collection name
    db_cm = mng_db[collection_name]
    cdir = os.path.dirname(__file__)
    file_res = os.path.join(cdir, filepath)

    data = pd.read_csv(file_res)
    data_json = json.loads(data.to_json(orient='records'))
    db_cm.remove()
    db_cm.insert(data_json)

if __name__ == "__main__":
  filepath = './local_burger raw data.csv'  #pass csv file path
  import_content(filepath)