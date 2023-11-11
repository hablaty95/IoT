import itertools


class SmartDevice:
    device_count = itertools.count()
    devices = []

    def __init__(self, location, device_type):
        self.id = next(self.device_count)
        self.location = location
        self.device_type = device_type
        self.complex_id = self.generate_id(location, device_type)

        self.devices.append(self)
        # self.save_to_json(self.to_dict())

    def generate_id(self, location, device_type):
        return location + "_" + device_type + "_" + str(self.id)

    def to_dict(self):
        return {
            "device_type": self.device_type,
            "id": self.id,
            "location": self.location,
            # "status": self.status
        }

    @classmethod
    def get_devices(cls):
        return cls.devices

    def get_type(self):
        return self.device_type

    def get_location(self):
        return self.location

    def get_id(self):
        return self.id
