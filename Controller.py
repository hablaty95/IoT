from AlarmPad import AlarmPad
from Lights import Lights
from SecurityCamera import SecurityCamera
from Shutters import Shutters
from SmartDevice import *
import json
from enum import Enum

from Thermostat import Thermostat
from WeatherPad import WeatherPad
from tkinter import *

Locations = Enum('Locations', ['First Bedroom', 'SECOND_BEDROOM', 'KITCHEN', 'HALL', 'BATHROOM', 'BALCONY'])


class Controller:

    def __init__(self):
        self.read_devices()

    def read_devices(self):
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
        with open("MyHome.json", "w") as file:
            json.dump([device.to_dict() for device in SmartDevice.get_devices()], file, indent=3)
