# Cura
Simple python CuraEngine wrapper. You must have curaengine in your path to use this library.
You also need to download the cura definitions from their repo to use the slicer.

## Usage

**cura.slicer(model_file, definition_files, settings={})**

The model_file is simply the filename and path to the stl file to slice.
The definition_files is a list of filenames of the definitions you wish to use to slice the stl file.
Settings is a dictionary of slicer settings to apply to the slicing procedure.

Returns the sliced gcode as a bytes object.

**cura.estimate(model_file, definition_files, settings={})**

Same as above, except this returns a dict with time and filament usage estimates instead of gcode.
