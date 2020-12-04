# Cura
Simple python CuraEngine wrapper.

Usage:
cura.slicer(model_file, definition_file)

The model_file is simply the filename and path to the stl file to slice.
The definition_file is the filename of the definition you wish to use to slice the stl file.

Returns the sliced gcode as a bytes object.

cura.estimate(model_file, definition_file)

Same as above, except this returns a dict with time and filament usage estimates instead of gcode.
