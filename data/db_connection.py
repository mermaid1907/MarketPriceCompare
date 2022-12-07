import pandas as pd
from typing import Optional
from sqlmodel import Field, Session, SQLModel, create_engine
import mysql.connector
SQLModel.metadata.clear()



db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="root",
    database="carrefour_records"
)
cursor = db.cursor()
cursor.execute("CREATE TABLE Carrefour (name VARCHAR(120), price VARCHAR(10), source_id int PRIMARY KEY AUTO_INCREMENT)")

cursor.execute("INSERT INTO Carrefour (name, price) VALUES()")
    
cursor.execute("CREATE TABLE Migros (name VARCHAR(120), price VARCHAR(10), source_id int PRIMARY KEY AUTO_INCREMENT)")
'''


## Create table model
class carrefour_records(SQLModel, table=True):
    source_id: Optional[str] = Field(default=None, primary_key=True)
    name: str
    price: str
    #foreign key olarak verilecek
    #market_id : 

class migros_records(SQLModel, table=True):
    source_id: Optional[str] = Field(default=None, primary_key=True)
    name: str
    price: str

class market(SQLModel, table=True):
    id: Field(primary_key=True)
    
    

## Connect to database
engine = create_engine("mysql+mysqlconnector://root@localhost:3307/test", echo=True, future=False)
SQLModel.metadata.create_all(engine)

     
## Add record to database
df = pd.read_csv('./carrefour_data.csv')
for row in range(len(df)):
    try:
        record = carrefour_records(name=df["name"][row], 
                          price=df["price"][row], )
        with Session(engine) as session:
            session.add(record)
            session.commit()            
    except Exception as e:
        pass
  
#df2.to_sql("carrefour_records", engine, index=False, if_exists='append')    
''' 