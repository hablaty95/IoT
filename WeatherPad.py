from SmartDevice import SmartDevice


class WeatherPad(SmartDevice):
    def __init__(self, location):
        device_type = "weather"
        super().__init__(location, device_type)

        print("Weather forecast pad registered! "
              "Location: " + self.location +
              " Id : ", self.id,
              " Complex Id = " + self.complex_id)
