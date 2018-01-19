

Installation
=================================================================


Clone on github
git clone https://github.com/asiaat/mxresto.git

Create virtual environment
python3 -m venv mxresto/

Run the virtualenvironment

mxresto/bin$  	source activate
(mxresto) pip install -r requirements.txt

Configuration
================================================================
../config/config.ini ile set postgres connection
for example
conn_string = postgres://postgres:postgres@localhost:5432/resto


Database preparation
================================================================
Create database
(mxresto) python utils.py


Pipelines
================================================================

After the database schema is created run the data pipes

Rating tables
(mxresto)python pipelines.py --local-scheduler RatingDB

For statistics
(mxresto)python pipelines.py --local-scheduler MeanRatingDB

For places
python pipelines.py --local-scheduler PlacesDB


Tests
================================================================
run the testcases

python test_cases.py

..
-----------------------------------------------
Ran 2 tests in 0.097s

OK




REST API usage
================================================================

start the flask server
(mxresto)python main.py

user curl to make some REST API queris

1. Simple statistics for places ratings

curl 'http://localhost:5000/api/stats'
{
    "rating_statistics": [
        {
            "75%": "1.400000",
            "count": "130.000000",
            "50%": "1.181820",
            "25%": "1.000000",
            "max": "2.000000",
            "min": "0.250000",
            "mean": "1.179622",
            "std": "0.349354"
        }
    ]
}

2. Top
curl 'http://localhost:5000/api/top_places'
{
    "top10_places": [
        {
            "rating": 2.0,
            "city": "Cuernavaca",
            "name": "Restaurant Las Mananitas"


...

        {
            "rating": 1.71429,
            "city": "San Luis Potosi",
            "name": "la Cochinita Pibil Restaurante Yucateco"
        },
        {
            "rating": 1.69231,
            "city": "San Luis Potosi",
            "name": "Mariscos El Pescador"
        }
    ],
    "count": 10
}

3. Top x places by given number
curl 'http://localhost:5000/api/top_places/4'
{
    "most_popular_places": [
        {
            "rating": 2.0,
            "city": "san luis potos",
            "name": "emilianos"
        },
        {
            "rating": 2.0,
            "city": "San Luis Potosi",
            "name": "Michiko Restaurant Japones"
        },
        {
            "rating": 2.0,
            "city": "Cuernavaca",
            "name": "Restaurant Las Mananitas"
        },
        {
            "rating": 1.83333,
            "city": "?",
            "name": "cafe punta del cielo"
        }
    ],
    "count": 4
}

4. Not so popular places
curl 'http://localhost:5000/api/top_places/-5'
{
    "most_nonpopular_places": [
        {
            "rating": 0.25,
            "city": "San Luis Potosi",
            "name": "Restaurant los Compadres"
        },
        {
            "rating": 0.25,
            "city": "victoria ",
            "name": "Carnitas Mata  Calle 16 de Septiembre"
        },
        {
            "rating": 0.5,
            "city": "San Luis Potosi",
            "name": "Abondance Restaurante Bar"
        },
        {
            "rating": 0.5,
            "city": "victoria",
            "name": "tacos abi"
        },
        {
            "rating": 0.5,
            "city": "victoria",
            "name": "puesto de gorditas"
        }
    ],
    "count": 5
}

5. Classifier accuracy
curl 'http://localhost:5000/api/classif_accuracy'
{
    "description": "ClassifierPlace accuracy",
    "accuracy": 0.46511627906976744
}

6.Classify a restoran by features
curl 'http://localhost:5000/api/classify' -d "smoke=none" -d "access=completely"  -d "dress_code=informal" -d "serv=Internet" -d "price=medium" -d "parking={\"valet parking\"}" -X PUT
"2"



TODO
================================================================




