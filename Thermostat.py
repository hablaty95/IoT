from SmartDevice import SmartDevice

class Thermostat(SmartDevice):
    """
    Thermostat class represents a smart thermostat device that extends the SmartDevice base class.

    Attributes:
        location (str): The location where the smart thermostat is installed.
        temp (float): The current temperature set on the thermostat.

    Methods:
        __init__(self, location):
            Initializes a new instance of the Thermostat class.

        get_temp(self):
            Retrieves the current temperature set on the thermostat.

        set_temp(self, n):
            Sets the temperature on the thermostat to the specified value.

        incr(self):
            Increases the temperature on the thermostat by 0.5 degrees.

        decr(self):
            Decreases the temperature on the thermostat by 0.5 degrees.

    Usage:
    thermostat = Thermostat("Living Room")
    print(thermostat.get_temp())
    thermostat.set_temp(25.0)
    thermostat.incr()
    thermostat.decr()
    """

    def __init__(self, location):
        """
        Initializes a new instance of the Thermostat class.

        Parameters:
            location (str): The location where the smart thermostat is installed.
        """
        device_type = "thermostat"
        super().__init__(location, device_type)
        self.temp = 24.5
        print("Thermostat registered! "
              "Location: " + self.location +
              " Id : ", self.id,
              " Complex Id = " + self.complex_id)

    def get_temp(self):
        """
        Retrieves the current temperature set on the thermostat.

        Returns:
            float: The current temperature on the thermostat.
        """
        return self.temp

    def set_temp(self, n):
        """
        Sets the temperature on the thermostat to the specified value.

        Parameters:
            n (float): The new temperature to set on the thermostat.
        """
        self.temp = n
        print(self.get_temp())

    def incr(self):
        """
        Increases the temperature on the thermostat by 0.5 degrees.
        """
        self.temp += 0.5
        print(self.get_temp())

    def decr(self):
        """
        Decreases the temperature on the thermostat by 0.5 degrees.
        """
        self.temp -= 0.5
        print(self.get_temp())
