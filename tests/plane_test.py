from typing import get_type_hints
from airport_booking_app.app_classes import Plane

plane1 = Plane(10, 10000)
plane2 = Plane(100, 15000)
plane3 = Plane(500, 600000)


def test_check_capacity():
    assert plane1.check_capacity() == 10

    assert plane2.check_capacity() == 100

    assert plane3.check_capacity() == 500


def test_check_range():
    assert plane1.check_range() == 10000

    assert plane2.check_range() == 15000

    assert plane3.check_range() == 600000