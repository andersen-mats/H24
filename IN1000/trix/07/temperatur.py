class Temperature:
    def __init__(self, temperature, instance):
        
        instances = ["celcius", "fahrenheit", "kelvin"]

        instance = instance.lower()

        assert isinstance(temperature, (float, int))
        assert isinstance(instance, str)
        assert instance in instances

        if instance == instances[1]:
            self._temperature = (temperature - 32) * (5/9)
        elif instance == instances[2]:
            self._temperature = (temperature - 273.15)
        else:
            self._temperature = float(temperature)

        

    def get_celcius(self):
        return self._temperature

    def get_fahrenheit(self):
        return ((self._temperature * (9 / 5)) + 32)

    def get_kelvin(self):
        return (self._temperature + 273.15)

