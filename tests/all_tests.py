from airport_booking_app.app_classes import FlightTrip, Plane, Passenger
import os

# Change path for you directory!!
flight_trip_path = os.path.join("E:\\GDrive\\Sparta Global\\12 Week Training Course\\Week 4\\Python_Project_(Project Beta)\\airport_booking_app" + "\\flight_trips")



# project_beta_path = os.path.dirname(os.path.dirname(__file__))
# flight_trip_path = os.path.join(project_beta_path + "\\airport_booking_app\\flight_trips")



pas1 = Passenger("Ioana", 123456789)
pas2 = Passenger("Kieron", 123456987)
pas3 = Passenger("Amy", 321456789)


def test_add_flight():
    pas1.add_flight("Miami")
    assert pas1.flight == "Miami"
    
    with open(os.path.join(flight_trip_path + "\\Miami.txt"), 'r') as flight_list:
        file_contents = flight_list.read()
        if (pas1.name in file_contents) and (str(pas1.passport_num) in file_contents):
            boolvar1 = True
        else:
            boolvar1 = False

    assert boolvar1 == True

    print(pas1.name, type(pas1.name))
    print(pas1.passport_num, type(pas1.passport_num))
    assert boolvar1 == True


    pas2.add_flight("Miami")
    assert pas2.flight == "Miami"
    
    with open(os.path.join(flight_trip_path + "\\Miami.txt"), 'r') as flight_list:
        file_contents = flight_list.read()
        if (pas2.name in file_contents) and (str(pas2.passport_num) in file_contents):
            boolvar2 = True
        else:
            boolvar2 = False

    assert boolvar2 == True


    pas3.add_flight("London")
    assert pas3.flight == "London"
    
    # This will be incorrect, returning False
    with open(os.path.join(flight_trip_path + "\\Miami.txt"), 'r') as flight_list:
        file_contents = flight_list.read()
        if (pas3.name in file_contents) and (str(pas3.passport_num) in file_contents):
            boolvar3 = True
        else:
            boolvar3 = False

    assert boolvar3 == False

# def test_add_flight():
#     pas1.add_flight("Miami")
#     assert pas1.flight == "Miami"
    
#     with open(os.path.join(flight_trip_path + "\\Miami.txt"), 'r') as flight_list:
#         file_contents = flight_list.read()
#         if (pas1.name in file_contents) and (str(pas1.passport_num) in file_contents):
#             boolvar1 = True
#         else:
#             boolvar1 = False

#     assert boolvar1 == True

#     print(pas1.name, type(pas1.name))
#     print(pas1.passport_num, type(pas1.passport_num))
#     assert boolvar1 == True


#     pas2.add_flight("Miami")
#     assert pas2.flight == "Miami"
    
#     with open(os.path.join(flight_trip_path + "\\Miami.txt"), 'r') as flight_list:
#         file_contents = flight_list.read()
#         if (pas2.name in file_contents) and (str(pas2.passport_num) in file_contents):
#             boolvar2 = True
#         else:
#             boolvar2 = False

#     assert boolvar2 == True


#     pas3.add_flight("London")
#     assert pas3.flight == "London"
    
#     # This will be incorrect, returning False
#     with open(os.path.join(flight_trip_path + "\\Miami.txt"), 'r') as flight_list:
#         file_contents = flight_list.read()
#         if (pas3.name in file_contents) and (str(pas3.passport_num) in file_contents):
#             boolvar3 = True
#         else:
#             boolvar3 = False

#     assert boolvar3 == False




def test_is_passport_valid():
    assert pas1.is_passport_valid() == True

    assert pas2.is_passport_valid() == True

    assert pas3.is_passport_valid() == True






ft = FlightTrip("Miami")
boeing = Plane(100, 100)



ft = FlightTrip("test_Miami")
boeing = Plane(100, 100)


def test_add_Passenger():

    ft.add_Passenger(pas1)
        
    with open(os.path.join(flight_trip_path + "\\test_Miami.txt"), 'r') as flight_list:
        file_contents = flight_list.read()
        if (pas1.name in file_contents) and (str(pas1.passport_num) in file_contents):
            boolvar1 = True
        else:
            boolvar1 = False

    assert boolvar1 == True


def test_assigned_plane():
    ft.assign_plane(boeing)
    assert type(ft.plane) is Plane


def test_check_plane():
    assert ft.check_plane() is True
