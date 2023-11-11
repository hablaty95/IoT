import itertools

class SmartDevice:
    """
    SmartDevice class represents a base class for various smart devices in a smart home.

    Class Attributes:
        device_count (itertools.count): A counter to generate unique IDs for each smart device.
        devices (list): A list to store instances of all smart devices.

    Attributes:
        id (int): The unique identifier for the smart device.
        location (str): The location where the smart device is installed.
        device_type (str): The type of the smart device.
        complex_id (str): A combination of location, device_type, and ID to create a unique identifier.

    Methods:
        __init__(self, location, device_type):
            Initializes a new instance of the SmartDevice class.

        generate_id(self, location, device_type):
            Generates a unique complex ID for the smart device based on location, device type, and ID.

        to_dict(self):
            Converts the smart device information to a dictionary.

        get_devices(cls):
            Class method to retrieve a list of all smart devices.

        get_type(self):
            Retrieves the type of the smart device.

        get_location(self):
            Retrieves the location where the smart device is installed.

        get_id(self):
            Retrieves the unique identifier of the smart device.
    """

    device_count = itertools.count()
    devices = []

    def __init__(self, location, device_type):
        """
        Initializes a new instance of the SmartDevice class.

        Parameters:
            location (str): The location where the smart device is installed.
            device_type (str): The type of the smart device.
        """
        self.id = next(self.device_count)
        self.location = location
        self.device_type = device_type
        self.complex_id = self.generate_id(location, device_type)

        self.devices.append(self)
        # self.save_to_json(self.to_dict())

    def generate_id(self, location, device_type):
        """
        Generates a unique complex ID for the smart device based on location, device type, and ID.

        Parameters:
            location (str): The location where the smart device is installed.
            device_type (str): The type of the smart device.

        Returns:
            str: The generated complex ID.
        """
        return location + "_" + device_type + "_" + str(self.id)

    def to_dict(self):
        """
        Converts the smart device information to a dictionary.

        Returns:
            dict: A dictionary containing the smart device information.
        """
        return {
            "device_type": self.device_type,
            "id": self.id,
            "location": self.location,
            # "status": self.status
        }

    @classmethod
    def get_devices(cls):
        """
        Class method to retrieve a list of all smart devices.

        Returns:
            list: A list containing instances of all smart devices.
        """
        return cls.devices

    def get_type(self):
        """
        Retrieves the type of the smart device.

        Returns:
            str: The type of the smart device.
        """
        return self.device_type

    def get_location(self):
        """
        Retrieves the location where the smart device is installed.

        Returns:
            str: The location of the smart device.
        """
        return self.location

    def get_id(self):
        """
        Retrieves the unique identifier of the smart device.

        Returns:
            int: The unique identifier of the smart device.
        """
        return self.id
