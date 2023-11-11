import webbrowser
import requests
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
from Controller import Controller


class Gui:
    """
    Gui class represents the graphical user interface for the smart home control panel.

    Attributes:
        ctrlr (Controller): The Controller instance managing the smart home devices.
        root (tk.Tk): The main Tkinter window for the GUI.

    Methods:
        __init__(self, ctrlr):
            Initializes a new instance of the Gui class.

        create_widgets(self):
            Creates the widgets for the GUI, including controls for lights, thermostat, shutters, and weather forecast.

        create_light_control(self, light_device):
            Creates a control panel for adjusting the brightness of a smart light.

        create_thermostat_control(self, thermostat_device):
            Creates a control panel for adjusting the temperature of a smart thermostat.

        create_shutters_control(self, shutters_device):
            Creates a control panel for opening and closing shutters.

        update_brightness(self, device, value):
            Updates the brightness of a smart light device.

        set_temperature(self, device, _entry):
            Sets the temperature of a smart thermostat device.

        open_shutters(self, device):
            Opens the shutters of a smart shutters device.

        close_shutters(self, device):
            Closes the shutters of a smart shutters device.

        show_weather_forecast(self):
            Fetches and displays the weather forecast.

        run(self):
            Runs the Tkinter main loop to start the GUI.
    """

    def __init__(self, ctrlr):
        """
        Initializes a new instance of the Gui class.

        Parameters:
            ctrlr (Controller): The Controller instance managing the smart home devices.
        """
        self.ctrlr = ctrlr
        self.root = tk.Tk()
        self.root.title("Smart Home Control Panel")
        self.create_widgets()

    def create_widgets(self):
        """
        Creates the widgets for the GUI, including controls for lights, thermostat, shutters, and weather forecast.
        """
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

        tk.Button(self.root, text="Show Weather Forecast", command=self.show_weather_forecast).pack()

    def create_light_control(self, light_device):
        """
        Creates a control panel for adjusting the brightness of a smart light.

        Parameters:
            light_device (Lights): The Lights instance representing the smart light.
        """
        frame = tk.Frame(self.root)
        frame.pack()

        tk.Label(frame, text=f"{light_device.get_location()} Light Brightness:").pack(side=tk.LEFT)
        scale = tk.Scale(frame, from_=0, to=1, resolution=0.1, orient=tk.HORIZONTAL,
                         command=lambda value, device=light_device: self.update_brightness(device, value))
        scale.set(light_device.brightness)
        scale.pack(side=tk.LEFT)

    def create_thermostat_control(self, thermostat_device):
        """
        Creates a control panel for adjusting the temperature of a smart thermostat.

        Parameters:
            thermostat_device (Thermostat): The Thermostat instance representing the smart thermostat.
        """
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
        """
        Creates a control panel for opening and closing shutters.

        Parameters:
            shutters_device (Shutters): The Shutters instance representing the smart shutters.
        """
        frame = tk.Frame(self.root)
        frame.pack()

        tk.Button(frame, text="Open Shutters", command=lambda device=shutters_device: self.open_shutters(device)).pack(
            side=tk.LEFT)
        tk.Button(frame, text="Close Shutters",
                  command=lambda device=shutters_device: self.close_shutters(device)).pack(side=tk.LEFT)

    def update_brightness(self, device, value):
        """
        Updates the brightness of a smart light device.

        Parameters:
            device (Lights): The Lights instance representing the smart light.
            value (float): The new brightness value.
        """
        device.brightness = float(value)
        print(device.get_brightness())

    def set_temperature(self, device, _entry):
        """
        Sets the temperature of a smart thermostat device.

        Parameters:
            device (Thermostat): The Thermostat instance representing the smart thermostat.
            _entry (str): The new temperature value.
        """
        try:
            device.temp = float(_entry)
            print(device.get_temp())
        except ValueError:
            print("Invalid temperature value")

    def open_shutters(self, device):
        """
        Opens the shutters of a smart shutters device.

        Parameters:
            device (Shutters): The Shutters instance representing the smart shutters.
        """
        print(f"Opening shutters at {device.get_location()}")
        device.status = True
        print(device.status)

    def close_shutters(self, device):
        """
        Closes the shutters of a smart shutters device.

        Parameters:
            device (Shutters): The Shutters instance representing the smart shutters.
        """
        print(f"Closing shutters at {device.get_location()}")
        device.status = False
        print(device.status)

    def show_weather_forecast(self):
        """
        Fetches and displays the weather forecast using wttr.in.
        """
        url = 'https://wttr.in/{}'.format('Budapest')
        try:
            data = requests.get(url)
            forecast = data.text
        except:
            forecast = "Error Occurred"
        print(forecast)

    def run(self):
        """
        Runs the Tkinter main loop to start the GUI.
        """
        self.root.mainloop()
