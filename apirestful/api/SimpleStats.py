import pandas as pd


class SimpleStats():

    def __init__(self,inp_db_engine):

        self.engine     = inp_db_engine
        self.dfRatings  = pd.read_sql_query("select * from ratings", self.engine)
        #self.dfMean     = pd.read_sql("select * from mean_ratings ",self.engine)


    def get_rating_stats(self):

        df = pd.read_sql("select * from mean_ratings ",self.engine)
        rating_stats = df.describe()
        return str(rating_stats)


    def get_most_popular_places(self,inp_count):
        df = pd.read_sql("select * from mean_ratings order by rating desc",self.engine)

        return df.head(inp_count)

    def get_most_nonpopular_places(self, inp_count):
        df = pd.read_sql("select * from mean_ratings order by rating asc", self.engine)
        return df.head(inp_count)





