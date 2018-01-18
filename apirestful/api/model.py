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


class Place(Base):
    __tablename__ = 'place'

    place_id      = Column(Integer, primary_key=True)
    name            = Column(String(150),nullable=False,index=True)
    address         = Column(String(250))
    city            = Column(String(250))
    state           = Column(String(150))
    alcohol         = Column(String(50))
    smoking_area    = Column(String(50))
    dress_code      = Column(String(50))
    accessibility   = Column(String(50))
    price           = Column(String(50))
    rambience       = Column(String(50))
    franchise       = Column(String(50))
    area            = Column(String(50))
    other_services  = Column(String(50))
    parking         = Column(String(250))
    rclass          = Column(Integer) # rating class

class Ratings(Base):
    """
    userID,placeID,rating,food_rating,service_rating
    """

    __tablename__ = 'ratings'

    ratings_id      = Column(Integer, primary_key=True)
    user_id         = Column(String(10), nullable=False)
    place_id        = Column(String(10))
    rating          = Column(Integer)
    food_rating     = Column(Integer)
    service_rating  = Column(Integer)


class MeanRatings(Base):
    """
    userID,placeID,rating,food_rating,service_rating
    """

    __tablename__ = 'mean_ratings'

    ratings_id      = Column(Integer, primary_key=True)
    place_id        = Column(String(20))
    rating          = Column(Float(2,4))

class Parking(Base):
    __tablename__ = 'parking'

    parking_id   = Column(Integer, primary_key=True)
    place_id     = Column(String(20))
    parking_lot  = Column(String(20))



def create_db():

    engine  = create_engine(conn_string)

    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)







