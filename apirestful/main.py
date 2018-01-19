from flask import Flask
from flask_restful import Api
import logging as log

from api.config.apiconf import config

from api.views import VRStats,VRTopPlaces,\
    VRClassifPlaces,VRClassifPlacesAccuracy,VRTop10Places


app = Flask(__name__)
ap = Api(app)

ap.add_resource(VRStats,                    '/api/stats')
ap.add_resource(VRTopPlaces,                '/api/top_places/<string:inp_number>')
ap.add_resource(VRTop10Places,              '/api/top_places')
ap.add_resource(VRClassifPlaces,            '/api/classify')
ap.add_resource(VRClassifPlacesAccuracy,    '/api/classif_accuracy')


if __name__ == '__main__':



    log.basicConfig(filename=config['log']['file'], level=log.DEBUG)

    app.run(debug   = bool(config['flask']['debug']),
            host    = config['flask']['host'],
            port    = int(config['flask']['port'])
            )


    log.info("Flask Restful server is started ...")