from Lights import Lights
from SmartDevice import SmartDevice
from Controller import Controller

def iot():
    ctrl = Controller()

    light1 = Lights("01")
    light2 = Lights("01")
    light3 = Lights("02")
    light4 = Lights("02")

    SmartDevice.save_to_json()


if __name__ == '__main__':
    iot()
