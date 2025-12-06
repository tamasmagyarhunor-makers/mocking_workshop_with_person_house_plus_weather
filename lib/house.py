class House:
    def __init__(self):
        self.door_open = False

    def open_door(self, person):
        if person.try_open_door():
            self.door_open = True