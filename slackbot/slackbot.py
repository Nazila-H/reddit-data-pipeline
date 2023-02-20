"""
SLACKBOT script
"""

import requests
from sqlalchemy import create_engine
from sqlalchemy import text
import logging
import time
import pandas as pd
from config import PG_CONFIGURATION

# wait until finishing tweet_collector and etl_job to start 
time.sleep(30)  # seconds 

# url get from slack developer webpage
webhook_url = "webhook_url"

# # This part is only used when you want to post python joke on slack instead of tweets
# # If want to use this part requirements.txt should include pyjoke

# pip install pyjokes
# import pyjokes
# joke = pyjokes.get_joke()
# data = {'text': joke}
# requests.post(url=webhook_url, json = data)


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


# get the content of reddit_sql table in postgresdb
query = 'SELECT * FROM reddit_sql;'
result = pg_client_connect.execute(text(query))


data_all = result.fetchall()
print('------This is the data from postgresql ------')
print(type(data_all)) # list of tuples [(ind, text, score), (ind, text, score), ...]
print(data_all)
print('--------------------------------------')


for data in subset:
    text = data[1]
    score = data[2]
    if score >= 0.05 :
        image_url ='https://i.pinimg.com/originals/35/40/07/354007e18492f5a684e1628b7a38d0b2.jpg'
 
    elif score <= - 0.05 :
        image_url = 'https://i.pinimg.com/564x/89/d2/47/89d2471b17b44cea66b74dcae30a3bae.jpg'
 
    else :
        image_url = 'https://i.pinimg.com/736x/1f/f8/fb/1ff8fbee9cb65e819ff6c9c539dd1866.jpg'


    item = {'blocks': [{
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": f" Title from reddit:\n {text} \n According to vader it has the sentiment score of: \n {score} \n \n \n"
            },
            "accessory": {
                "type": "image",
                "image_url": f"{image_url}",
                "alt_text": "alt text for image"
                }
                }]
                }
    # post on slack
    requests.post(url=webhook_url, json = item)
    time.sleep(3)
    #print(item)
