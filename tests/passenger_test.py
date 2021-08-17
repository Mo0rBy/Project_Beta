from airport_booking_app.app_classes import Passenger

pas1 = Passenger("Ioana", 100900000)
pas2 = Passenger("Will", 540001765)
pas3 = Passenger("David", 654000102)


def test_add_flight():
    pas1.add_flight("Miami")
    assert pas1.flight == "Miami"

    pas2.add_flight("Budapest")
    assert pas2.flight == "Budapest"

def test_is_passport_valid():
    assert pas1.is_passport_valid() == True

