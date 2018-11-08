from peewee import (CharField,
                    SqliteDatabase,
                    Model,
                    TextField,
                    IntegerField,
                    OperationalError,
                    IntegrityError,
                    DateTimeField)
db = SqliteDatabase("polling.db")
import datetime
pollings = [
    {'id': 1,'understand_index':3, 'reccomendations': 'Ivy'},
    {'id': 2,'understand_index':4, 'reccomendations': 'Khamisi'}
    
    
    
]



class Polling(Model):
    
    time_made=DateTimeField(default=datetime.datetime.now)
    understand_index= CharField(max_length=100)
    reccomendations= CharField(max_length=100)
    
    

    class Meta:
        database = db

def initialize():
    try:
        Polling.create_table()
    except OperationalError:
        pass
    for polling in pollings:
      try:
        Polling.create(
            
            understand_index=polling.get('understand_index'),
            reccomendations=polling.get('reccomendations'),
           
            )
      except IntegrityError:
        pass

def model_test():
         Polling.create(
            understand_index=5,
            reccomendations="reading",
           
            )

    


