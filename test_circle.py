import math

def test_circle():

    PI = math.pi
    r = 23

    area = PI * r ** 2

    assert area == 1661.9025137490005

    length = 2 * PI * r

    assert length == 144.51326206513048
    print("Площадь=", area)
    print("Длина=", length)


