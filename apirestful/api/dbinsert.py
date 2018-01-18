from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import configparser
import pandas as pd

from model import Place, Ratings, MeanRatings


config = configparser.ConfigParser()
config.read("../config.ini")

# postgres connection
conn_string = config['postgres']['conn_string']
engine      = create_engine(conn_string)


def insert_places():
    inp_csv_ratings = "/home/malle/proj/py/mxresto/data/normal/places_classes.csv"
    dfPlacesCL = pd.read_csv(inp_csv_ratings, sep=",")


    # get parking info
    inp_csv_parking = "/home/malle/proj/py/mxresto/data/normal/chefmozparking.csv"
    dfParking = pd.read_csv(inp_csv_parking, sep=",")
    dfParking.drop_duplicates(keep='first')

    lst_parking = {}
    for indx, r in dfParking.iterrows():
        #print(r['placeID'], r['parking_lot'])
        parking = dfParking[dfParking['placeID'] == r['placeID']]['parking_lot'].tolist()
        lst_parking[r['placeID']] = parking

    # create a configured "Session" class
    s = sessionmaker(bind=engine)()

    for index,row in dfPlacesCL.iterrows():
        print(row)
        p = Place(place_id          = row['placeID'],
                  name              = row['name'],
                  address           = row['address'],
                  city              = row['city'],
                  state             = row['state'],
                  alcohol           = row['alcohol'],
                  smoking_area      = row['smoking_area'],
                  dress_code        = row['dress_code'],
                  accessibility     = row['accessibility'],
                  price             = row['price'],
                  rambience         = row['Rambience'],
                  franchise         = row['franchise'],
                  area              = row['area'],
                  other_services    = row['other_services'],
                  rclass            = row['rclass'],
                  parking           = lst_parking[row['placeID']]
                  )
        s.add(p)
        s.commit()

    s.close()

def insert_ratings():
    inp_csv_ratings = "/home/malle/proj/py/mxresto/data/normal/rating_final.csv"
    dfRatings = pd.read_csv(inp_csv_ratings, sep=",")


    # create a configured "Session" class
    s = sessionmaker(bind=engine)()

    for index,row in dfRatings.iterrows():
        print(row)
        r = Ratings(user_id         = row['userID'],
                    place_id        = row['placeID'],
                    rating          = row['rating'],
                    food_rating     = row['food_rating'],
                    service_rating  = row['service_rating']

                  )
        s.add(r)
        s.commit()

    s.close()



def insert_mean_ratings():
    dfRatings     = pd.read_sql_query("select * from ratings", engine)
    sf            = dfRatings.groupby(by='place_id')['rating'].mean()


    df1 = pd.DataFrame(data=sf.index, columns=['place_id'])
    df2 = pd.DataFrame(data=sf.values, columns=['rating'])
    dfMean = pd.merge(df1, df2, left_index=True, right_index=True)

    print(dfMean.head())

    s = sessionmaker(bind=engine)()

    for index,row in dfMean.iterrows():
        print(row)
        m = MeanRatings(
            place_id = row['place_id'],
            rating   = row['rating']
        )

        s.add(m)
        s.commit()

    s.close()


if __name__ == '__main__':
    insert_places()
    insert_ratings()
    insert_mean_ratings()