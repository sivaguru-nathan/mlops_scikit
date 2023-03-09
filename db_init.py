from sqlalchemy import create_engine
from env_loader import db_url


class Database:
    def __init__(self):
        self.engine = create_engine(db_url)
        
    def read_all_from_table(self,table):
        return f'select * from "{table}"'