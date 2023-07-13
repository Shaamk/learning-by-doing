# from temperature import avg_temp


# def test_temperature_func_exists():
#     assert avg_temp

# def test_avg_1_temp():
#     result = avg_temp([2])
#     assert result == 2

# def test_avg_2_temps():
#     result = avg_temp([2, 4])
#     assert result == 3

# def test_avg_2_temps_celc_faren():
#     result = avg_temp([Celcius(0), Fahrenheit(32)])
#     assert result == Celcius(0)

'''
result = avg_temp([Celcius(0), Fahrenheit(32)])
result = avg_temp([celcius object 0, Fahrenheit(32)])
result = avg_temp([celcius object 0, farehnheit object 32]) -> returns a celcuis object

'''

# def test_celcius_fahrenheit_calc():
#     result = calc_conversion(0)
#     assert result == 32

from temperature import Kelvin, Celsius


def test_kelvin_exists() -> None:
    assert Kelvin(0)

def test_comparing_kelvin() -> None:
    assert Kelvin(3) == Kelvin(3)

def test_comparing_kelvin_that_do_not_match() -> None:
    assert not Kelvin(3) == Kelvin(8)

def test_adding_kelvins() -> None:
    assert Kelvin(3) + Kelvin(4) == Kelvin(7)

def test_dividing_kelvin() -> None:
    assert Kelvin(20) // 4 == Kelvin(5)

def test_celsius_exists() -> None:
    assert Celsius(14)

def test_comparing_celsius() -> None:
    assert Celsius(25) == Celsius(25)

def test_comparing_celsius_to_kelvin() -> None:
    assert Celsius(0) == Kelvin(273)

def test_comparing_kelvin_to_celsius() -> None:
    assert Kelvin(283) == Celsius(10)

def test_adding_celsius_to_kelvin() -> None:
    assert Celsius(10) + Kelvin(283) == Kelvin(293)

# def test_division_celsius_to_kelvin() -> None:

# def test_average_() -> None: