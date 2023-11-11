from SmartDevice import SmartDevice


class Shutters(SmartDevice):
    def __init__(self, location):
        device_type = "shutters"
        super().__init__(location, device_type)
        self.status = False                 #false == shutters are down, true == shutters are up
        print("Shutters registered! "
              "Location: " + self.location +
              " Id : ", self.id,
              " Complex Id = " + self.complex_id)
