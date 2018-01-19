import unittest
from apirestful.api.config import apiconf
import logging as log

from sqlalchemy import create_engine

from  apirestful.api.ClassifierPlace import ClassifierPlace

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