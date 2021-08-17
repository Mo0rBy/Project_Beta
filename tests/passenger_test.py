from airport_booking_app.app_classes import Passenger

pas1 = Passenger("Ioana", 123456789)
pas2 = Passenger("Will", "987654321") # Passport num not an int
pas3 = Passenger("Amy", 15975365412) # 2 extra nums in passport_num


def test_add_flight():
    pas1.add_flight("Miami")
    assert pas1.flight == "Miami"

    pas2.add_flight("Budapest")
    assert pas2.flight == "Budapest"

    pas3.add_flight("London")
    assert pas3.flight == "London"


def test_is_passport_valid():
    assert pas1.is_passport_valid() == True

    assert pas2.is_passport_valid() == False

    assert pas3.is_passport_valid() == False