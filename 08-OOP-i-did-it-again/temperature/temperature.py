'''
Get the mean average temperature from various temperature units

Class Celcius
    to_celcius
    from_celcius
    __add__
    __div__
    __eq__
    __str__

Class Fahrenheit
    to_celcius
    from_celcius
    __add__
    __div__
    __eq__
    __str__

Class Kelvin
    to_celcius
    from_celcius
    __add__
    __div__
    __eq__
    __str__

'''

# def avg_temp(temps):
#     return sum(temps, Celcius(0))/len(temps)



class Kelvin:
    def __init__(self, temp: int) -> None:
        self._temp = temp
    
    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Kelvin) and not isinstance(other, Celsius):
            raise NotImplementedError()
        return self._temp == other.to_kelvin()._temp 

    def __add__(self, other: "Kelvin") -> "Kelvin":
        return Kelvin(self._temp + other._temp)
    
    def __floordiv__(self, divisor: int) ->"Kelvin":
        return Kelvin(self._temp // divisor)
    
    def to_kelvin(self) -> "Kelvin":
        return self
    
class Celsius:
    def __init__(self, temp: int) -> None:
        self._temperature = temp

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Celsius) and not isinstance(other, Kelvin):
            raise NotImplementedError()
        self_in_kelvin = self.to_kelvin()
        other_in_kelvin = other.to_kelvin()
        return self_in_kelvin == other_in_kelvin
        #self.to_kelvin == other.to_kelvin

    def __add__(self, other: "Kelvin") -> "Kelvin":
        return Kelvin(self.to_kelvin() + other.to_kelvin())
    
    def to_kelvin(self) -> Kelvin:
        return Kelvin(self._temperature + 273)