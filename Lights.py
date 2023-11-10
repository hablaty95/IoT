from SmartDevice import SmartDevice


class Lights(SmartDevice):
    def __init__(self, location):
        device_type = "01"
        super().__init__(location, device_type)
        print("Smart Light registered! Location: " + self.location + " Id : ", self.id, " Complex Id = " + self.complex_id)
