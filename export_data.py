import pandas as pd
from sqlalchemy import create_engine
from dotenv import load_dotenv
import os

load_dotenv()

user = os.getenv('MYSQL_USER')
password = os.getenv('MYSQL_PASSWORD')
host = os.getenv('MYSQL_HOST')
port = int(os.getenv('MYSQL_PORT'))
database = os.getenv('MYSQL_DATABASE')

connection_string = f"mysql+mysqlconnector://{user}:{password}@{host}:{port}/{database}"

engine = create_engine(connection_string)

df = pd.read_csv("pizza_sales.csv")

df.to_sql(
    name='PowerGenration',       
    con=engine,             
    if_exists='replace',   
    index=False             
)

print("✅ Data imported successfully into MySQL using to_sql()!")