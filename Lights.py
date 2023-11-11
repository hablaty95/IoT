from SmartDevice import SmartDevice

class Lights(SmartDevice):
    """
    Lights class represents a smart light device that extends the SmartDevice base class.

    Attributes:
        location (str): The location where the smart light is installed.
        brightness (float): The current brightness level of the smart light, ranging from 0.0 to 1.0.

    Methods:
        __init__(self, location):
            Initializes a new instance of the Lights class.

        get_brightness(self):
            Retrieves the current brightness level of the smart light.

    Usage:
    light = Lights("Living Room")
    print(light.get_brightness())
    """

    def __init__(self, location):
        """
        Initializes a new instance of the Lights class.

        Parameters:
            location (str): The location where the smart light is installed.
        """
        device_type = "lights"
        super().__init__(location, device_type)
        self.brightness = 0.5
        print("Smart Light registered! "
              "Location: " + self.location +
              " Id : ", self.id,
              " Complex Id = " + self.complex_id)

    def get_brightness(self):
        """
        Retrieves the current brightness level of the smart light.

        Returns:
            float: The current brightness level, ranging from 0.0 to 1.0.
        """
        return self.brightness
