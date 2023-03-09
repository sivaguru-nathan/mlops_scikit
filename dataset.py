import pandas as pd
from db import Database

random_state=23

class Dataset:
    
    def __init__(self,columns,target,file=None,table=None,from_db=False):
        if not from_db:
            assert file!=None, "file path to read not given"
            self.df=self.load_from_file(file)
            
        else:
            assert table!=None, "table to read not given"
            self.db=Database()
            self.df=load_from_db(table)
        self.reduce_columns(columns,target)    
            
            
    def load_from_file(self,file):
        # load data from the csv file
        df = pd.read_csv(file)
        return df
    
    def load_from_db(self,table):
        #load data from the database
        query=self.db.read_all_from_table(table)
        df = pd.read_sql_query(query,con=self.db.engine)
        return df
    
    def reduce_columns(self,columns,target):
        # remove columns in df other than given columns
        self.X=self.df[columns]
        self.Y=self.df[target]

    def train_test_split(self,test_ratio=0.2):
        #train test split
        from sklearn.model_selection import train_test_split
        X_train, X_test, y_train, y_test = train_test_split(self.X, self.Y, test_size=test_ratio, random_state=random_state)
        return X_train, X_test, y_train, y_test