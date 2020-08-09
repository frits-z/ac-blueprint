# Blueprint
Blueprint modules to build an Assetto Corsa python app.

This is a set of modules that serve as a blueprint to build Assetto Corsa python apps on.

The modules include

* Config
* AppWindow
* Graphics Utilities
* Text Labels
* Data (Session and Car)

## Python apps in Assetto Corsa

A short explanation of how it works... `acMain`, `acUpdate` etcetera. 

## Blueprint workflow

Explanation of how its set up. Session class, within the session there are cars etc. Config, appwindow, aclabel, ac_gl_utils etc.

## Development Notes

This is a collection of quirks and other things I ran into when developing apps for Assetto Corsa, things that are useful to know about.

### Modules

Be careful about modules. In Assetto Corsa, all python apps appear to share the same python instance (?). If app A uses a module with the same name as app B does, only one gets used: the one that gets imported first. Therefore, modules like app_window.py etc. should be put in a unique folder so that it doesn't get triggered as the same name.

Therefore, the following directory tree structure is followed.

```
.
├── MyAppName.py
├── config_defaults.ini
├── MyAppNameLib
│   ├── config_handler.py
│   └── app_window.py
└── dll
    ├── stdlib
    └── stdlib64
```

### Graphics Drawing: Backface culling

When drawing a quad or a triangle using the `ac.gl` functions, make sure to specify the vertices in counter clockwise order. That is the winding order as seen from the center of the triangle (or quad). The winding order implies the front face and the back face of the triangle. To save performance, by default the back face is culled (not rendered). So the front face must be facing the correct way.

For example:
```
A
|\
| \
|  \
B---C
```
The vertices A, B and C should be specified in the order of A -> B -> C. 

### Graphics Drawing: Geometry rotation

When using trigonometry to rotate a shape you are drawing, remember that the greater the y (height), the lower on the app window. It is like an inverted y-axis. This makes normal trigonometry functions that rotate positive angle in counterclockwise direction, work in clockwise direction.

### Fonts

Issues with different font 'weights'. For example, Roboto has 100 (Thin), 300 (Light), ..., 900 (Black). By default no support for this. Only regular and bold. To workaround, made a custom font for each weight of Roboto. Shipped in the `content/fonts` folder.

### Text

Drawing a lot of different text labels is costly for performance.


### Data

#### Wind

The terminology Assetto Corsa uses for wind direction is wrong. Usually, the wind direction points to where the wind is coming from, in Assetto Corsa it points to where the wind is going.

#### Coordinates System

Assetto Corsa follows the convention of OpenGL in 3D graphics regarding the X,Y,Z coordinates system: it uses a right-handed system. Positive rotation is counterclockwise about the axis of rotation.

* The x-axis indicates longitude: the distance east (positive) or west (negative) from the origin point.
* The z-axis indicates latitude: the distance south (positive) or north (negative) from the origin point.
* The y-axis indicates elevation: the distance up (positive) or down (negative) from the origin point.