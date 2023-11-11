from SmartDevice import SmartDevice

class SecurityCamera(SmartDevice):
    """
    SecurityCamera class represents a smart security camera device that extends the SmartDevice base class.

    Attributes:
        location (str): The location where the smart security camera is installed.
        status (bool): The current status of the security camera. False represents the camera being off, True represents the camera being on.

    Methods:
        __init__(self, location):
            Initializes a new instance of the SecurityCamera class.

    Usage:
    camera = SecurityCamera("Entrance")
    """

    def __init__(self, location):
        """
        Initializes a new instance of the SecurityCamera class.

        Parameters:
            location (str): The location where the smart security camera is installed.
        """
        device_type = "camera"
        super().__init__(location, device_type)
        self.status = False
        print("Security camera registered! "
              "Location: " + self.location +
              " Id : ", self.id,
              " Complex Id = " + self.complex_id)
