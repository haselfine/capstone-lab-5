from peewee import *

db = SqliteDatabase('record_holder.sqlite')

class Record_Holder(Model):
    name = CharField()
    country = CharField()
    catches = IntegerField()

    class Meta:
        database = db

    def __str__(self):
        return f'{self.name} from {self.country} holds a record of {self.catches} catches'

def add_record_holder():
    '''Creates record holder. Obviously would need validation and try/except block if you were to actually use it'''
    new_rh_name = input('Enter the name of the record holder you would like to add: ')
    new_rh_country = input('Enter the home country of the record holder: ')
    new_rh_catches = int(input('Enter top number of catches by the record holder: '))
    new_rh = Record_Holder(name=new_rh_name, country=new_rh_country, catches=new_rh_catches)
    new_rh.save()

def search_record_holder():
    name_to_search = input('Which record holder would you like to find? ')
    searched_rh = Record_Holder.select().where(Record_Holder.name == name_to_search)
