from SmartDevice import SmartDevice


class Lights(SmartDevice):
    def __init__(self, location):
        device_type = "lights"
        super().__init__(location, device_type)
        self.brightness = 0.5
        print("Smart Light registered! "
              "Location: " + self.location +
              " Id : ", self.id,
              " Complex Id = " + self.complex_id)

    def get_brightness(self):
        return self.brightness
