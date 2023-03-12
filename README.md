# mp_lvgl_widgets

Collection of widgets I have created for the MicroPython port of LVGL. 
These are written in Python so no compiling needed to use them. If there is any 
portion of the code that relies on heavy math that code will be placed in a 
function and the viper code emitter is used. That bring the speed pretty close 
to what C code execution speed is.

These widgets are a subclass of actual lvgl objects so they will function 
much in the same manner. Some of the methods may have been overridden in order
to change the default behavior. If for some reason you need to access the 
original methods you can do so by prefixing the method name with an underscore.

## Widgets

* `arc_label`: Bends a string of text into an arc
* `tab_view`: nice looking "notebook" or tabbed style interface
* `bent_progress`: a progress bar that is bent, This can be used for a gauge'