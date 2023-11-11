from SmartDevice import SmartDevice


class SecurityCamera(SmartDevice):
    def __init__(self, location):
        device_type = "camera"
        super().__init__(location, device_type)
        self.status = False
        print("Security camera registered! "
              "Location: " + self.location +
              " Id : ", self.id,
              " Complex Id = " + self.complex_id)
