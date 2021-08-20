import os

# Change paths for your directories!!
parent_dir = os.path.dirname(__file__)
flight_trip_path = os.path.join(parent_dir + "\\flight_trips")


class Passenger:
    def __init__(self, name, passport_num):
        self.name = name
        self.passport_num = passport_num
        # self.flight = None

    def add_flight(self, destination):
        self.flight = destination
        with open(os.path.join(flight_trip_path + "\\" + destination + ".txt"), 'a+') as flight_list:
            flight_list.write(self.name + ", " + str(self.passport_num) + "\n")

    # def add_flight(self, destination):
    #     self.flight = destination   # This needs to change
    #     with open(os.path.join(flight_trip_path + "\\" + destination + ".txt"), 'a+') as flight_list:
    #         flight_list.write(self.name + ", " + str(self.passport_num) + "\n")

    def get_info(self):
        return self.name, self.passport_num

    def is_passport_valid(self):  # valid as in is the passport number 9 numbers long, no letters
        if len(self.passport_num) == 9:  # and (isinstance(self.passport_num, int) is True):
            return True
        else:
            return False


class FlightTrip:
    def __init__(self, destination):
        self.destination = destination
        self.passenger_dict = {}
        self.plane = None

    def assign_plane(self, plane):
        self.plane = plane

    def fetch_passenger_list(self):
        with open(os.path.join(flight_trip_path + self.destination + ".txt"), 'r') as flight_list:
            return flight_list  # Duplication detection

    # check if plane is valid - has seating available etc.
    def check_plane(self):
        with open(os.path.join(flight_trip_path + "\\" + self.destination + ".txt"), 'r') as flight_list:
            line_count = 0
            for line in flight_list:
                if line != "\n":
                    line_count += 1

        if self.plane.capacity >= line_count:
            print("The assigned plane is valid")
            return True
        else:
            print("Please assign a new plane")
            return False

    # check if plane is valid - has seating available etc.

    def add_Passenger(self, passenger):  # Add destinations to list for each passenger?? ASK (passenger1 = [des1, des2])
        with open(os.path.join(flight_trip_path + "\\" + self.destination + ".txt"), 'a+') as flight_list:
            flight_list.write(passenger.name + ", " + str(passenger.passport_num) + "\n")


class Plane:
    def __init__(self, capacity):
        self.capacity = capacity

    def check_capacity(self):
        return self.capacity
