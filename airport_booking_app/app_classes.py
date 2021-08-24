import os
import json

# Change paths for your directories!!
parent_dir = os.path.dirname(__file__)
flight_trip_path = os.path.join(parent_dir + "\\flight_trips")


class Passenger:
    def __init__(self, name, passport_num):
        self.user_info = {"name": name, "passport_number": passport_num}


    def get_info(self):
        return self.user_info

    def is_passport_valid(self):  # valid as in is the passport number 9 numbers long, no letters
        if len(self.user_info["passport_number"]) == 9:  # and (isinstance(self.passport_num, int) is True):
            return True
        else:
            return False

    def write_to_register(self):
        with open(os.path.join(parent_dir + "\\Registers\\passenger_register.json"), 'r+') as file:
            passenger_register_data = json.load(file)
            passenger_register_data["passenger_register"].append(self.user_info)
            file.seek(0)
            json.dump(passenger_register_data, file, indent=2)


class FlightTrip:
    def __init__(self, destination):
        self.destination = destination
        self.plane = None

    def assign_plane(self, plane):
        self.plane = plane

    def fetch_passenger_list(self):
        with open(os.path.join(parent_dir + "\\Registers\\flight_trip_register.json"), 'r') as file:
            content  = json.load(file)
            register = content["flight_trip_register"][self.destination]
            return json.load(register)

    # check if plane is valid - has seating available etc.
    def check_plane(self):
        with open(os.path.join(parent_dir + "\\Registers\\flight_trip_register.json"), 'r') as file:
            flight_trip_list = json.load(file)
            passenger_count = len(flight_trip_list["flight_trip_register"][self.destination])
        if self.plane.capacity >= passenger_count:
            return True
        else:
            return False

    # Add a passenger to a flights json file
    def add_Passenger(self, passenger):  # Add destinations to list for each passenger?? ASK (passenger1 = [des1, des2])
        with open(os.path.join(parent_dir + "\\Registers\\flight_trip_register.json"), 'r+') as file:
            file_data = json.load(file)
            file_data["flight_trip_register"][self.destination].append(passenger.user_info)
            file.seek(0)
            json.dump(file_data, file, indent=2)

    # Write flight trip name to the flight trip register
    def write_to_register(self):
        with open(os.path.join(parent_dir + "\\Registers\\flight_trip_register.json"), 'r+') as file:
            flight_trip_register_data = json.load(file)
            flight_trip_register_data["flight_trip_register"].update({self.destination:[]})
            file.seek(0)
            json.dump(flight_trip_register_data, file, indent=2)


class Plane:
    def __init__(self, name, capacity):
        self.name = name
        self.capacity = int(capacity)

    def check_capacity(self):
        return self.capacity

    def write_to_register(self):
        with open(os.path.join(parent_dir + "\\Registers\\plane_register.json"), 'r+') as file:
            plane_register_data = json.load(file)
            plane_register_data["plane_register"].append({self.name: self.capacity})
            file.seek(0)
            json.dump(plane_register_data, file, indent=2)


###################

if __name__ == "__main__":
    pas1 = Passenger("Will", 123456789)
    print(pas1.get_info())
    pas2 = Passenger("Amy", 987654321)

    flight_trip = FlightTrip("Miami")
    flight_trip.add_Passenger(pas1)
    flight_trip.add_Passenger(pas2)

    plane1 = Plane(10)
    flight_trip.assign_plane(plane1)

    print(flight_trip.fetch_passenger_list())
    var = flight_trip.check_plane()
    print(var, type(var))
