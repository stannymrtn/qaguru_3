def test_rectangle():

    a = 10
    b = 20

    perimeter = (a + b)*2
    print("Периметр=", perimeter)

    assert perimeter == 60

    area = a*b
    print("Площадь равна=", area)

    assert area == 200
