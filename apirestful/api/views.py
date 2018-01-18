
#from api import app, log
import configparser
import logging as log

from flask_restful import Resource
from sqlalchemy import create_engine

from .ClassifierPlace import ClassifierPlace
from .SimpleStats import SimpleStats

config = configparser.ConfigParser()
config.read("./config.ini")

# postgres connection
conn_string = config['postgres']['conn_string']
engine  = create_engine(conn_string)

sstats = SimpleStats(engine)
cp     = ClassifierPlace(engine)

cp.make_features()
cp.make_labels()
cp.train(0.33)



class VRClassifPlaces(Resource):

    def get(self, inp_features):

        result = ""

        try:
            #res    = find_both_db_employee(id)
            prediction = cp.predict([[0, 2, 0, 1, 1, 1]])
            result = str(prediction)
            log.info(result)

        except:
            msg = "Something is wrong"
            log.warning(msg)

        return result

class VRClassifPlacesAccuracy(Resource):

    def get(self):

        result = ""

        try:

            accuracy = cp.get_accuracy()
            result = accuracy
            log.info(result)

        except:
            msg = "Something is wrong"
            log.warning(msg)

        return result


class VRPlace(Resource):
    """
    View Resource Place
    """

    def get(self, id):

        result = ""

        try:
            #res    = find_both_db_employee(id)
            result = "Put this place into test!"
            log.info(result)

        except:
            msg = "Something is wrong"
            log.warning(msg)

        return result


class VRStats(Resource):


    def get(self):

        result = ""

        try:
            result = sstats.get_rating_stats()
            log.info(result)

        except:
            msg = "Something is wrong"
            log.warning(msg)

        return result


class VRTopPlaces(Resource):


    def get(self,inp_number):

        result = ""
        top_nr  = int(inp_number)
        print (top_nr)

        try:
            if  top_nr > 0:
                result = sstats.get_most_popular_places(top_nr)
            elif top_nr < 0:
                result = sstats.get_most_nonpopular_places(abs(top_nr))
            else:
                result = sstats.get_most_popular_places(10)

            log.info(result)

        except:
            msg = "Something is wrong"
            log.warning(msg)

        return result

"""
@app.route('/')
def index():
    log.info('index loaded')
    return 'Hello World!'
"""
