from SmartDevice import SmartDevice


class Thermostat(SmartDevice):
    def __init__(self, location):
        device_type = "thermostat"
        super().__init__(location, device_type)
        self.temp = 24.5
        print("Thermostat registered! "
              "Location: " + self.location +
              " Id : ", self.id,
              " Complex Id = " + self.complex_id)

    def get_temp(self):
        return self.temp

    def set_temp(self, n):
        self.temp = n
        print(self.get_temp())

    def incr(self):
        self.temp += 0.5
        print(self.get_temp())


    def decr(self):
        self.temp -= 0.5
        print(self.get_temp())
