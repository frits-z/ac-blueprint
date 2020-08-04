# ac_blueprint
Blueprint modules to build an Assetto Corsa python app.

This is a set of modules that serve as a blueprint to build Assetto Corsa python apps on.

The modules include

* Config
* AppWindow
* Graphics Utilities
* Text Labels
* Data (Session and Car)

Below are all the quirks of Assetto Corsa python app development I know about.

* Be careful about modules. If one app uses a module with the same name as another app does, only one gets used: the one that gets loaded the first. Therefore, modules like app_window.py etc. should be put in a unique folder so that it doesn't get triggered as the same name.



## Drawing 

Counter clockwise specification. Backface culling.