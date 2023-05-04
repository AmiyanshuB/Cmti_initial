from pony.orm import *
db = Database()
db.bind(provider = 'sqlite', filename = 'databsase.sqlite', create_db = True)
class Person(db.Entity):
    id = PrimaryKey(int,auto = True)
    name = Required(str)
    age = Required(int)
    cars = Set('Car')
class Car (db.Entity):
    make = Required(str)
    model = Required(str)
    owner = Required(Person)
show(Person)
