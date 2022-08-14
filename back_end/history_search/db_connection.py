import psycopg2
from psycopg2 import Error

# Postgres username, password, and database name
def connect():
    
    POSTGRES_ADDRESS = 'localhost'
    POSTGRES_PORT = '5432'
    POSTGRES_USERNAME = 'postgres'
    POSTGRES_PASSWORD = '1234'
    POSTGRES_DBNAME = 'postgres'

    # Create the connection
    connection = psycopg2.connect(user=POSTGRES_USERNAME,
                                  password=POSTGRES_PASSWORD,
                                  host=POSTGRES_ADDRESS,
                                  port=POSTGRES_PORT,
                                  database=POSTGRES_DBNAME)

    return connection
