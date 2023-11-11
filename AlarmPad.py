from SmartDevice import SmartDevice


class AlarmPad(SmartDevice):
    def __init__(self, location):
        device_type = "alarm"
        super().__init__(location, device_type)
        self.is_alarm_on = False
        self.is_alarm_activable = False
        print("Security alarm pad registered! "
              "Location: " + self.location +
              " Id : ", self.id,
              " Complex Id = " + self.complex_id)
