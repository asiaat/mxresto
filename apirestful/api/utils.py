from model import create_db
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
import configparser
from sqlalchemy import Column,Integer,Numeric,String,UniqueConstraint,Float,\
    ForeignKey,Sequence,Table,ForeignKeyConstraint



config = configparser.ConfigParser()
config.read("../config.ini")

# postgres connection
conn_string = config['postgres']['conn_string']

Base = declarative_base()



create_db()