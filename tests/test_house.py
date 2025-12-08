from lib.house import House
from lib.person import Person

def test_house_instantiates():
    house = House()

    assert house.door_open == False

def test_house_open_door():
    house = House()
    person = Person('Hunor', 3)

    house.open_door(person)

    assert house.door_open == True