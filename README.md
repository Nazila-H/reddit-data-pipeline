
## Dockerized data pipeline that analyzes the sentiment of reddits titles.
The idea is creating a dockerized data pipeline than can extract title (or text) from a web-API, store data in the MongoDB database, doing some sentiment analysis then put them as table format on the postgres database, at the end creating a slackbot to post then in slack.


### Challenges:

Install Docker<br/>
Build a data pipeline with docker-compose yml file to orchestrate docker services (processes) <br/>
Collect data from reddit web-API <br/>
Store data from reddit in Mongo DB (Nosql database) <br/>
Create an ETL job transporting data from MongoDB to PostgreSQL <br/>
Run sentiment analysis on the text <br/>
Build a slack bot that publishes selected reddits <br/>


### Installation and requirements

Install Docker<br/>
Install MongoDB<br/>
Install PostgresDB<br/>
Install vaderSentiment<br/>

Create a Reddit account<br/>
Create an app in reddit: www.reddit.com/prefs/apps<br/>
Create a Slack Bot: https://api.slack.com/apps<br/>


## Getting Started
docker-compose build<br/>
docker-compose up<br/>
docker-compose down --> removing docker container<br/>

Check database on mongodb: ```docker exec mongodb mongosh```<br/>
Check table on postgresdb: ```docker exec -it tahinipost psql -U postgres -h localhost -p 5432 -d reddit_db```<br/>


```
The folder structure should be:


|__ reddit_collector
    |__ config.py
    |__ Dockerfile 
    |__ get_reddit.py
    |__ requirements.txt 
|__ etl_job
    |__ config.py
    |__ Dockerfile
    |__ etl.py
    |__ requirements.txt
|__slackbot
    |__ config.py
    |__ Dockerfile
    |__ requirements.txt
    |__ slackbot.py
|__ docker-compose.yml
 
```



