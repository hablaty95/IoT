from SmartDevice import SmartDevice

class Shutters(SmartDevice):
    """
    Shutters class represents a smart shutters device that extends the SmartDevice base class.

    Attributes:
        location (str): The location where the smart shutters are installed.
        status (bool): The current status of the shutters. False represents shutters down, True represents shutters up.

    Methods:
        __init__(self, location):
            Initializes a new instance of the Shutters class.

    Usage:
    shutters = Shutters("Bedroom")
    print(shutters.status)
    """

    def __init__(self, location):
        """
        Initializes a new instance of the Shutters class.

        Parameters:
            location (str): The location where the smart shutters are installed.
        """
        device_type = "shutters"
        super().__init__(location, device_type)
        self.status = False  # False == shutters are down, True == shutters are up
        print("Shutters registered! "
              "Location: " + self.location +
              " Id : ", self.id,
              " Complex Id = " + self.complex_id)
