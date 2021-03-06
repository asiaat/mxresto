
from flask import request
import logging as log

from flask_restful import Resource
from sqlalchemy import create_engine

from .ClassifierPlace import ClassifierPlace
from .SimpleStats import SimpleStats

from api.config import apiconf

config = apiconf.config

# postgres connection
conn_string = config['postgres']['conn_string']
engine      = create_engine(conn_string)

sstats = SimpleStats(engine)
cp     = ClassifierPlace(engine)

cp.make_features()
cp.make_labels()
cp.train(0.33)





class VRClassifPlacesAccuracy(Resource):

    def get(self):

        result = ""

        try:

            accuracy = cp.get_accuracy()
            d = {
                'description':'ClassifierPlace accuracy',
                'accuracy': accuracy
            }
            result = d
            log.info(result)

        except:
            msg = "Something is wrong"
            log.warning(msg)

        return result

todos = {}

class VRStats(Resource):


    def get(self):

        result = ""

        try:
            stats = sstats.get_rating_stats()

            d = {}
            for line in stats.split('\n')[1:]:
                measure,id,rating = line.split()
                d[measure] = rating

            result = {'rating_statistics':[d]}

            log.info(result)

        except:
            msg = "Something is wrong"
            log.warning(msg)

        return result


class VRTopPlaces(Resource):


    def get(self,inp_number):

        result = ""
        top_nr  = int(inp_number)


        try:
            if  top_nr > 0:
                stats = sstats.get_most_popular_places(top_nr)

                jmostp = []
                for index, row in stats.iterrows():
                    d = {
                        'name': row['name'],
                        'rating' : row['rating'],
                        'city': row['city']
                    }
                    jmostp.append(d)

                result = {'most_popular_places': jmostp, 'count': top_nr }


            elif top_nr < 0:
                stats = sstats.get_most_nonpopular_places(abs(top_nr))

                jmostp = []
                for index, row in stats.iterrows():
                    d = {
                        'name': row['name'],
                        'rating': row['rating'],
                        'city': row['city']
                    }
                    jmostp.append(d)

                result = {'most_nonpopular_places': jmostp,'count': abs(top_nr)}

            else:
                stats = sstats.get_most_popular_places(10)

                jmostp = []
                for index, row in stats.iterrows():
                    d = {
                        'name': row['name'],
                        'rating': row['rating'],
                        'city': row['city']
                    }
                    jmostp.append(d)


                result = {'top10_places': jmostp,'count': abs(top_nr)}

            log.info(result)

        except:
            msg = "Something is wrong"
            log.warning(msg)

        return result


class VRTop10Places(Resource):
    def get(self):

        result = ""

        try:

            stats = sstats.get_most_popular_places(10)

            jmostp = []
            for index, row in stats.iterrows():
                d = {
                    'name': row['name'],
                    'rating': row['rating'],
                    'city': row['city']
                }
                jmostp.append(d)

            result = {'top10_places': jmostp, 'count': 10}
            log.info(result)

        except:
            msg = "Something is wrong"
            log.warning(msg)

        return result


class VRClassifPlaces(Resource):

    def put(self):

        result = ""

        try:

            smoke          = request.form['smoke']
            dress_code     = request.form['dress_code']
            access         = request.form['access']
            price          = request.form['price']
            serv           = request.form['serv']
            parking        = request.form['parking']


            inp_features = {'parking': parking,
                            'access': access,
                            'smoke': smoke,
                            'serv': serv,
                            'price': price,
                            'dress_code': dress_code
                            }


            pred_class = cp.predict(inp_features)

            result = str(pred_class[0])

            log.info(result)

        except:
            msg = "Something is wrong"
            log.warning(msg)

        return result