import os
import subprocess
import sys
import math
import datetime
import re


def __slice(model_file, definition_files, settings=None):
	if settings is None:
		settings = {}

	cmd = ["CuraEngine", "slice"]

	for definition in definition_files:
		cmd.append("-j")
		cmd.append(definition)

	for key, val in settings.items():
		cmd.append("-s")
		cmd.append(str(key)+"="+str(val))

	cmd.append("-l")
	cmd.append(model_file)

	cmd.append("-v")

	process = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
	output = process.communicate()[0]
	err_output = process.communicate()[1]

	process.wait()

	return output, err_output


def slicer(model_file, definition_files, settings=None, verbose=False):
	output, err_output = __slice(model_file, definition_files, settings)

	if verbose:
		print(err_output)

	return output


def estimate(model_file, definition_files, settings=None, verbose=False):
	output, err_output = __slice(model_file, definition_files, settings)

	if verbose:
		print(err_output)

	record = False

	output_lines = err_output.decode("utf8").split(os.linesep)
	header = []

	for line in output_lines:
		if line.startswith("Gcode header after slicing:"):
			record = True

		if record:
			header.append(line)

	if verbose:
		print("Header:", header)

	time = -1
	filament = -1

	for line in header:
		if line.startswith(";TIME:"):
			time = int(line.split(":")[-1])
		if line.startswith(";Filament used: "):
			filament = float(line.split(" ")[-1].replace("m",""))

	return {"time": time, "filament": filament}
