"""Module to list HF models"""
import pandas as pd
import time as ts
from huggingface_hub import list_models



class HFMODEL():
    """Class for fetching HF models"""

    def __init__(self) -> None:
        pass


    def fetch_models(self):
        """Method to fetch the specified no of models"""
        models = list_models(filter='medical')
        columns = ['Model_id','Author','Library_Name','Likes','Last_updated','Downloads']
        res_dfs = []
        for model in models:
            res_dfs.append(pd.DataFrame([[model.id,model.author, model.library_name, model.likes,model.last_modified ,model.downloads]]
                          ,columns=columns))
        print(pd.concat(res_dfs).sort_values('Downloads',ascending=False).head(10))





if __name__=='__main__':
    while True:
        HFMODEL().fetch_models()
        ts.sleep(60)
