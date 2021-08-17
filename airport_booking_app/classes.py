
class Passenger:
    def __init__(self, name, passport_num):
        self.name = name
        self.passport_num = passport_num
        self.flight = None

    def add_flight(self):
        pass

    def get_info(self):
        pass

    def is_passport_valid(self):
        pass
# valid as in is the passport number 9 numbers long, no letters


class FlightTrip:
    def __init__(self, destination):
        self.destination = destination

    def assign_plane(self):
        pass

    def generate_passenger_list(self):
        pass

    def check_plane(self):
        pass
# check if plane is valid - has seating available etc.


class Plane:
    def __init__(self, capacity, range):
        self.capacity = capacity
        self.range = range




