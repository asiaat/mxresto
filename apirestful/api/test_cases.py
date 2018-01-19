import unittest


from config import apiconf

from sqlalchemy import create_engine

from  ClassifierPlace import ClassifierPlace

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


if __name__ == '__main__':
    unittest.main()


