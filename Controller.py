from Lights import Lights
import itertools
import json


class Controller:
    devices = []

    def __init__(self):
        self.read_devices()
        pass

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
                if tmp_device_type == "01":  # lights
                    saved_device = Lights(tmp_location)
