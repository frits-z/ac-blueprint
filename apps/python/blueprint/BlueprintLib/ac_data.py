import ac
import acsys
import os
import sys
import platform
import math

# Import Assetto Corsa shared memory library.
# It has a dependency on ctypes, which is not included in AC python version.
# Point to correct ctypes module based on platform architecture.
# First, get directory of the app, then add correct folder to sys.path.
app_dir = os.path.dirname(os.path.dirname(__file__))

if platform.architecture()[0] == "64bit":
    sysdir = os.path.join(app_dir, 'dll', 'stdlib64')
else:
    sysdir = os.path.join(app_dir, 'dll', 'stdlib')
# Python looks in sys.path for modules to load, insert new dir first in line.
sys.path.insert(0, sysdir)
os.environ['PATH'] = os.environ['PATH'] + ";."

from BlueprintLib.sim_info import info

class Session:
    """Handling all data from AC that is not car-specific.
    
    Args:
        cfg (obj:Config): App configuration.
    """
    def __init__(self, cfg):
        # Config object
        self.cfg = cfg

        # Initialize session data attributes
        self.focused_car_id = 0

        # Initialize focused car object
        self.focused_car = Car(cfg, self.focused_car_id)

    def update(self):
        """Update session data."""
        self.focused_car_id = ac.getFocusedCar()
        self.replay_time_multiplier = info.graphics.replayTimeMultiplier

        self.focused_car.set_id(self.focused_car_id)
        self.focused_car.update()

class Car:
    """Handling all data from AC that is car-specific.
    
    Args:
        cfg (obj:Config): App configuration.
        car_id (int, optional): Car ID number to retrieve data from.
            Defaults to own car.
    """
    def __init__(self, cfg, car_id=0):
        self.cfg = cfg
        self.id = car_id

        # Initialize car data attributes
        self.speed = 0
        self.gear = 0
        self.gear_text = "N"
    
    def set_id(self, car_id):
        """Update car ID to retrieve data from.
        
        Args:
            car_id (int): Car ID number."""
        self.id = car_id

    def update(self):
        """Update data."""
        self.gear = ac.getCarState(self.id, acsys.CS.Gear)

        if self.cfg.use_kmh:
            self.speed = ac.getCarState(self.id, acsys.CS.SpeedKMH)
        else:
            self.speed = ac.getCarState(self.id, acsys.CS.SpeedMPH)

        # Gear label
        if self.gear == 0:
            self.gear_text = "R"
        elif self.gear == 1:
            self.gear_text = "N"
        else:
            self.gear_text = str(self.gear - 1)