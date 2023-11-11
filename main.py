from AlarmPad import AlarmPad
from Lights import Lights
from SecurityCamera import SecurityCamera
from Shutters import Shutters
from SmartDevice import SmartDevice
from Controller import Controller
from Thermostat import Thermostat
from WeatherPad import WeatherPad
from Gui import Gui
import tkinter as tk
from tkinter import ttk
def iot():
    # ctrl = Controller()
    #
    # # light1 = Lights("HALL")
    # # light2 = Lights("KITCHEN")
    # # light3 = Lights("FIRST_BEDROOM")
    # # light4 = Lights("SECOND_BEDROOM")
    # # thermo = Thermostat('HALL')
    # # cam = SecurityCamera('HALL')
    # # alarm = AlarmPad('HALL')
    # # weather = WeatherPad('HALL')
    # # weather_bed = WeatherPad('FIRST_BEDROOM')
    # # shutter = Shutters('FIRST_BEDROOM')
    #
    # ctrl.save_to_json()
    root = tk.Tk()
    app = Gui(root)
    root.mainloop()


if __name__ == '__main__':
    iot()
