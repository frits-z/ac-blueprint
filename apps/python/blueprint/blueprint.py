import ac

from BlueprintLib.color_palette import Colors
from BlueprintLib.config_handler import Config
from BlueprintLib.ac_data import Session, Car 
from BlueprintLib.app_window import AppWindow
from BlueprintLib.ac_label import ACLabel
from BlueprintLib.ac_gl_utils import Point

# Initialize general object variables
cfg = None
session = None
app_window = None

# Timers
timer_30_hz = 0
PERIOD_30_HZ = 1 / 30

# Text labels
label_speed = 0
label_gear = 0


def acMain(ac_version):
    """Run upon startup of Assetto Corsa.
    
    Args:
        ac_version (str): Version of Assetto Corsa.
            AC passes this argument automatically.
    """
    # Read config
    global cfg
    cfg = Config()

    # Initialize session data object
    global session
    session = Session(cfg)

    # Set up app window
    global app_window
    app_window = AppWindow(cfg)
    ac.addRenderCallback(app_window.id, app_render)

    # Initialize fonts
    ac.initFont(0, 'ACRoboto300', 0, 0)
    ac.initFont(0, 'ACRoboto700', 0, 0)

    # Set up labels
    global label_speed, label_gear
    label_speed = ACLabel(app_window.id, font='ACRoboto300', alignment='center')
    label_speed.fit_height(
        Point(cfg.app_width * 0.5,
              cfg.app_height * cfg.app_padding),
        cfg.app_scale * 100)

    # Speed unit selection
    if cfg.use_kmh:
        label_speed.set_postfix(" km/h")
    else:
        label_speed.set_postfix(" mph")

    label_gear = ACLabel(app_window.id, font='ACRoboto700', alignment='center')
    label_gear.fit_height(
        Point(cfg.app_width * 0.5,
              cfg.app_scale * 200),
        cfg.app_scale * 250)


def acUpdate(deltaT):
    """Run every physics tick of Assetto Corsa.
    
    Args:
        deltaT (float): Time delta since last tick in seconds.
            Assetto Corsa passes this argument automatically.

    Important: Function gets called regardless of app being visible.
    """
    pass


def app_render(deltaT):
    """Run every rendered frame of Assetto Corsa.

    Args:
        deltaT (float): Time delta since last tick in seconds.
            Assetto Corsa passes this argument automatically.

    Important: Function only gets called if the app is visible.
    """
    # TODO change this to draw.
    app_window.render(deltaT)

    global timer_30_hz

    # Update timer
    timer_30_hz += deltaT

    # Run on 10hz
    if timer_30_hz > PERIOD_30_HZ:
        timer_30_hz -= PERIOD_30_HZ

        # Update ac global data
        session.update()

        # Update text labels
        label_speed.set_text("{:.0f}".format(session.focused_car.speed))
        label_gear.set_text("{}".format(session.focused_car.gear_text))

def acShutdown():
    """Run on shutdown of Assetto Corsa"""
    # Update config if necessary
    if cfg.update_cfg:
        cfg.save()