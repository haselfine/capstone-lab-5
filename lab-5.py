from peewee import *

db = SqliteDatabase('record_holder.sqlite')

class InputError(Exception):
    pass

class Record_Holder(Model):
    name = CharField()
    country = CharField()
    catches = IntegerField()

    class Meta:
        database = db

    def __str__(self):
        return f'{self.name} from {self.country} holds a record of {self.catches} catches'

def add_record_holder(self):
    try:
        new_rh_name = input('Enter the name of the record holder you would like to add: ')
        
    except InputError():
