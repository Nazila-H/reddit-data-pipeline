"""
ETL script
"""

import pandas as pd
from sqlalchemy import create_engine
from sqlalchemy import text
import pymongo 
import time
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from config import PG_CONFIGURATION




# we need two clients, mongo and postgres

# Connect to MongoDB
mongo_client = pymongo.MongoClient(host="mongodb", port=27017)
db = mongo_client.reddit

time.sleep(10)  # seconds


### POSTGRES STUFF###
# THE 🤚🏼 things needed to connect to PostgreSQL
PG_USER = PG_CONFIGURATION.get("PG_USERNAME")
PG_PASSWORD = PG_CONFIGURATION.get("PG_PASSWORD")
PG_HOST = PG_CONFIGURATION.get("PG_HOST")
PG_PORT = 5432 # defined in docker-compose.yml 
PG_DB = PG_CONFIGURATION.get("PG_DATABASE")


# Define connection string for PostrgreSQL
conn_str = f"postgresql://{PG_USER}:{PG_PASSWORD}@{PG_HOST}:{PG_PORT}/{PG_DB}"

# define a client for PostrgreSQL
pg_client = create_engine(conn_str)

# connect pg_client to PostgreSQL
pg_client_connect = pg_client.connect()

# create a postgres table
create_table = """
CREATE TABLE reddit_sql (
    _id VARCHAR,
    title TEXT,
    sentiment NUMERIC
);
"""
# execute create_table query with pg_client_connect and then commit
pg_client_connect.execute(text(create_table))
pg_client_connect.commit()

#extract: read from mongodb

import re


def clean_tweets(tweet):
    tweet = re.sub("\’", '', tweet)  #removes @mentions
    tweet = re.sub("\“", '', tweet)  #removes @mentions
    tweet = re.sub("\”", '', tweet)  #removes @mentions
    tweet = re.sub("\'", '', tweet)  #removes @mentions
    tweet = re.sub('''\"''', '', tweet)  #removes @mentions

   
    return tweet
#transform: cleaning + sentiment analsis
s = SentimentIntensityAnalyzer()
# insert into table
docs = db.posts.find()
for doc in docs:
    id = doc['_id'].replace("'", "").replace('"', "")
  #  title = doc['title'].replace("'", "").replace('"', "")
    title = clean_tweets(doc['title'])
    score = s.polarity_scores(title)
    sentiment = score['compound']
    query = f'''INSERT INTO reddit_sql (_id, title, sentiment) VALUES ('{id}', '{title}', {sentiment});'''
    pg_client_connect.execute(text(query))
    pg_client_connect.commit()



#load: load each title and sentiment into a table execute query into 

