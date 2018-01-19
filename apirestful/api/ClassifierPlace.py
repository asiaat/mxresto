import pandas as pd
import numpy  as np

from sklearn.naive_bayes import GaussianNB
from sklearn import preprocessing as prep
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

class ClassifierPlace():

    def __init__(self,inp_db_engine):

        self.engine     = inp_db_engine
        self.dfPlaces   = pd.read_sql_query("select * from place", self.engine)
        self.dfFeatures = pd.DataFrame(self.dfPlaces,
         columns=['smoking_area','dress_code','accessibility','price','other_services','parking'])

        self.dfLabels = pd.DataFrame(self.dfPlaces, columns=['rclass'])

        self.features   = None
        self.labels     = None
        self.classifier = GaussianNB()
        self.accuracy   = None

        self.leDress    = None

    def make_features(self):
        leSmoke     = prep.LabelEncoder().fit(self.dfFeatures['smoking_area'].values)
        self.leDress     = prep.LabelEncoder().fit(self.dfFeatures['dress_code'].values)
        leAccess    = prep.LabelEncoder().fit(self.dfFeatures['accessibility'].values)
        lePrice     = prep.LabelEncoder().fit(self.dfFeatures['price'].values)
        leServ      = prep.LabelEncoder().fit(self.dfFeatures['other_services'].values)
        leParking   = prep.LabelEncoder().fit(self.dfFeatures['parking'].values)


        lstFeatures = self.dfFeatures.values

        indx = 0
        for a in lstFeatures:

            lstFeatures[indx] = leSmoke.transform([a[0]])[0], self.leDress.transform([a[1]])[0],\
                                leAccess.transform([a[2]])[0],lePrice.transform([a[3]])[0], \
                                leServ.transform([a[4]])[0], leParking.transform([a[5]])[0]
            indx +=  1

        self.features = lstFeatures.tolist()

    def make_labels(self):
        self.labels = np.array([lab[0] for lab in self.dfLabels.values])

    def train(self,inp_test_size):
        train, test, train_labels, test_labels = train_test_split(self.features,
                                                                  self.labels,
                                                                  test_size=inp_test_size,
                                                                  random_state=25)

        self.classifier.fit(train, train_labels)

        preds           = self.classifier.predict(test)
        self.accuracy   = accuracy_score(test_labels, preds)

    def get_accuracy(self):
        return self.accuracy

    def predict(self,inp_features):
        dress_code = self.leDress.transform(['informal'])
        #print(dress_code)
        #print(list(self.leDress.classes_))
        return self.classifier.predict([[0, 2, 0, 1, 1, 1]])


