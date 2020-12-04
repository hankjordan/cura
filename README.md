# Cura
Simple python CuraEngine wrapper.

## Usage

**cura.slicer(model_file, definition_files)**

The model_file is simply the filename and path to the stl file to slice.
The definition_files is a list of filenames of the definitions you wish to use to slice the stl file.

Returns the sliced gcode as a bytes object.

**cura.estimate(model_file, definition_files)**

Same as above, except this returns a dict with time and filament usage estimates instead of gcode.
