import unittest

import requests
from  ClassifierPlace import ClassifierPlace
from config import apiconf
from sqlalchemy import create_engine

from status import *

cnf = apiconf.config
conn_string = cnf['postgres']['conn_string']
engine      = create_engine(conn_string)

class TestClassifier(unittest.TestCase):


    def test_some_accuracy(self):

        cp = ClassifierPlace(engine)
        cp.make_features()
        cp.make_labels()
        cp.train(0.33)


        self.assertGreater(cp.get_accuracy(),0.1)

    def test_classify(self):

        cp = ClassifierPlace(engine)
        cp.make_features()
        cp.make_labels()
        cp.train(0.33)

        inp_features = {'parking': '{"valet parking"}', 'access': 'no_accessibility',
               'smoke': 'none', 'serv': 'none', 'price': 'high', 'dress_code': 'formal'}


        pred_class = cp.predict(inp_features)

        self.assertIsNotNone(pred_class)



class TestRestApi(unittest.TestCase):
    """
    NB!
    To run these tests the service must be run  localhost at  port 5000
    """

    def test_get_wrong_api_query(self):
        r = requests.get('http://localhost:5000/qwer/1')
        assert r.status_code == HTTP_404_NOT_FOUND

    def test_get_ok_status(self):
        r = requests.get('http://localhost:5000/api/stats')
        assert r.status_code == HTTP_200_OK


if __name__ == '__main__':
    unittest.main()


