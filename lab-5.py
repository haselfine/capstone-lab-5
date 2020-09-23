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
    print(f'Okay. {new_rh}. Got it.')

def search_record_holder():
    name_to_search = input('What is the record holder\'s name? ')
    searched_rh = Record_Holder.get_or_none(Record_Holder.name == name_to_search)
    return searched_rh

def update_record_holder():
    rh_to_update = search_record_holder()
    new_catch_record = int(input(f'What is the new catch record for {rh_to_update.name}? '))
    updated_rh = Record_Holder.update(catches=new_catch_record).where(Record_Holder.name == rh_to_update.name).execute()
    print(f'{rh_to_update.name}\'s new catch record is {new_catch_record}.')

def delete_record_holder():
    rh_to_delete = search_record_holder()
    confirmation = input('Would you like to delete? Press y . Otherwise enter any other letter to keep record holder. ')
    if confirmation == 'y':
        deleted_rh = Record_Holder.delete().where(Record_Holder.name == rh_to_delete.name).execute()
        print(f'{rh_to_delete.name} was deleted.')
    else:
        print(f'{rh_to_delete.name} was not deleted.')

def main():
    db.connect()
    db.create_tables([Record_Holder])
    print('Practicing adding record holder...')
    add_record_holder()
    print('\nPracticing searching for a record holder...')
    result = search_record_holder()
    print(result)
    print('\nPracticing updating record holder...')
    update_record_holder()
    print('\nPracticing deleting a record holder...')
    delete_record_holder()

if __name__ == '__main__':
    main()