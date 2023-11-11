from SmartDevice import SmartDevice

class WeatherPad(SmartDevice):
    """
    WeatherPad class represents a smart weather forecast pad device that extends the SmartDevice base class.

    Attributes:
        location (str): The location where the weather forecast pad is installed.

    Methods:
        __init__(self, location):
            Initializes a new instance of the WeatherPad class.

    Usage:
    weather_pad = WeatherPad("Living Room")
    """

    def __init__(self, location):
        """
        Initializes a new instance of the WeatherPad class.

        Parameters:
            location (str): The location where the weather forecast pad is installed.
        """
        device_type = "weather"
        super().__init__(location, device_type)
        print("Weather forecast pad registered! "
              "Location: " + self.location +
              " Id : ", self.id,
              " Complex Id = " + self.complex_id)
