# Blueprint
Blueprint modules to build an Assetto Corsa python app.

This is a set of modules that serve as a blueprint to build Assetto Corsa python apps on.

The modules include

* Config
* AppWindow
* Graphics Utilities
* Text Labels
* Data (Session and Car)

## Assetto Corsa Python App Development Notes

Below are all the quirks of Assetto Corsa python app development I know about.

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

### Graphics Drawing 

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

### Fonts

Issues with different font 'weights'. For example, Roboto has 100 (Thin), 300 (Light), ..., 900 (Black). By default no support for this. Only regular and bold. To workaround, made a custom font for each weight of Roboto. Shipped in the `content/fonts` folder.