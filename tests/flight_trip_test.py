from airport_booking_app.app_classes import FlightTrip, Plane

# C:\Users\Zeeshan\Documents\Deloitte\python_project\airport_booking_app\classes.py

ft = FlightTrip("Albania")


def test_assigned_plane():
    assert type(ft.plane) is Plane


def test_generate_passenger_dict():
    ft.generate_passenger_dict()
    assert type(ft.passenger_dict) is dict


def test_check_plane():
    assert ft.check_plane(ft.passenger_dict, ft.plane.capacity) is True
