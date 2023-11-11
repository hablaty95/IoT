from AlarmPad import AlarmPad
from Lights import Lights
from SecurityCamera import SecurityCamera
from Shutters import Shutters
from SmartDevice import *
import json
from enum import Enum

from Thermostat import Thermostat
from WeatherPad import WeatherPad
import tkinter as tk
from tkinter import ttk
from Controller import *

import tkinter as tk
from Lights import Lights
from Shutters import Shutters
from Thermostat import Thermostat
from Controller import Controller


class Gui:
    def __init__(self, ctrlr):
        self.ctrlr = Controller()

        self.root = tk.Tk()
        self.root.title("Smart Home Control Panel")

        self.create_widgets()

    def create_widgets(self):
        tk.Label(self.root, text="Lights Brightness Control").pack()

        for device in SmartDevice.devices:
            if isinstance(device, Lights):
                self.create_light_control(device)

        tk.Label(self.root, text="Thermostat Temperature Control").pack()
        for device in SmartDevice.devices:
            if isinstance(device, Thermostat):
                thermostat_device = device
                self.create_thermostat_control(thermostat_device)

        tk.Label(self.root, text="Shutters Control").pack()
        for device in SmartDevice.devices:
            if isinstance(device, Shutters):
                shutters_device = device
                self.create_shutters_control(shutters_device)

        # tk.Button(self.root, text="Save to JSON", command=self.ctrlr.save_to_json).pack()

    def create_light_control(self, light_device):
        frame = tk.Frame(self.root)
        frame.pack()

        tk.Label(frame, text=f"{light_device.get_location()} Light Brightness:").pack(side=tk.LEFT)
        scale = tk.Scale(frame, from_=0, to=1, resolution=0.1, orient=tk.HORIZONTAL,
                         command=lambda value, device=light_device: self.update_brightness(device, value))
        scale.set(light_device.brightness)
        scale.pack(side=tk.LEFT)

    def create_thermostat_control(self, thermostat_device):
        frame = tk.Frame(self.root)
        frame.pack()

        tk.Label(frame, text=f"{thermostat_device.get_location()} Thermostat Temperature:").pack(side=tk.LEFT)
        entry = tk.Entry(frame)
        entry.insert(0, str(thermostat_device.get_temp()))
        entry.pack(side=tk.LEFT)

        tk.Button(frame, text="Set Temperature",
                  command=lambda device=thermostat_device, _entry=entry:
                  self.set_temperature(device, _entry.get())).pack(side=tk.LEFT)

    def create_shutters_control(self, shutters_device):
        frame = tk.Frame(self.root)
        frame.pack()

        tk.Button(frame, text="Open Shutters", command=lambda device=shutters_device: self.open_shutters(device)).pack(
            side=tk.LEFT)
        tk.Button(frame, text="Close Shutters",
                  command=lambda device=shutters_device: self.close_shutters(device)).pack(side=tk.LEFT)

    def update_brightness(self, device, value):
        device.brightness = float(value)
        print(device.get_brightness())

    def set_temperature(self, device, _entry):
        try:
            device.temp = _entry
            print(device.temp)
        except ValueError:
            print("Invalid temperature value")

    def open_shutters(self, device):
        print(f"Opening shutters at {device.get_location()}")
        device.status = True
        print(device.status)

    def close_shutters(self, device):
        print(f"Closing shutters at {device.get_location()}")
        device.status = False
        print(device.status)

    def run(self):
        self.root.mainloop()

