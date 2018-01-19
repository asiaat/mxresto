from model import create_db
from config import apiconf

from sqlalchemy.ext.declarative import declarative_base



# postgres connection
conn_string = apiconf.config['postgres']['conn_string']

Base = declarative_base()



create_db()