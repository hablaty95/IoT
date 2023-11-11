from AlarmPad import AlarmPad
from Lights import Lights
from SecurityCamera import SecurityCamera
from Shutters import Shutters
from SmartDevice import SmartDevice
from Thermostat import Thermostat
from WeatherPad import WeatherPad
from tkinter import *
import json
from enum import Enum

# Enum to represent different locations in the house
Locations = Enum('Locations', ['First Bedroom', 'SECOND_BEDROOM', 'KITCHEN', 'HALL', 'BATHROOM', 'BALCONY'])

class Controller:
    """
    Controller class manages the smart home devices and provides methods to read and save device information.

    Methods:
        __init__(self):
            Initializes a new instance of the Controller class.

        read_devices(self):
            Reads device information from a JSON file and creates instances of the corresponding device classes.

        save_to_json(self):
            Saves the current state of smart devices to a JSON file.
    """

    def __init__(self):
        """
        Initializes a new instance of the Controller class.
        Reads the existing devices from a JSON file during initialization.
        """
        self.read_devices()

    def read_devices(self):
        """
        Reads device information from a JSON file and creates instances of the corresponding device classes.
        """
        with open("MyHome.json", "r") as file:
            data = json.load(file)

        for device in data:
            print(device)
            tmp_device_type = device['device_type']
            tmp_id = device['id']
            tmp_location = device['location']

            if tmp_id in data:
                print("This shouldn't have happened! Device already listed!")
            else:
                if tmp_device_type == "lights":
                    Lights(tmp_location)
                if tmp_device_type == "thermostat":
                    Thermostat(tmp_location)
                if tmp_device_type == "camera":
                    SecurityCamera(tmp_location)
                if tmp_device_type == "alarm":
                    AlarmPad(tmp_location)
                if tmp_device_type == "weather":
                    WeatherPad(tmp_location)
                if tmp_device_type == "shutters":
                    Shutters(tmp_location)

    def save_to_json(self):
        """
        Saves the current state of smart devices to a JSON file.
        """
        with open("MyHome.json", "w") as file:
            json.dump([device.to_dict() for device in SmartDevice.get_devices()], file, indent=3)
