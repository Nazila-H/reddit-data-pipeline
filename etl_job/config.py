"""
The values of the following dictionary
corresponds to the ones defined in the postgres service defined
in the docker-compose.yml file
"""

PG_CONFIGURATION = {
    "PG_USERNAME":"postgres",
    "PG_PASSWORD":"postgres",
    "PG_DATABASE":"reddit_db",
    "PG_HOST":"tahinipost" # this is the container name defined in the postgres service
}