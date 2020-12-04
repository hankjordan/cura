import requests
import os
import tempfile
import subprocess


CURA_CONFIG_URL = "https://raw.githubusercontent.com/Ultimaker/Cura/4.4/resources/definitions/"
FDMPRINTER_CONFIG = "fdmprinter.def.json"
FDMEXTRUDER_CONFIG = "fdmextruder.def.json"


def _download(url, output):
	data = requests.get(url).text
	open(output, "w").write(data)


def slicer(model_file, config_file="prusa_i3.def.json"):
	temp_dir = tempfile.gettempdir() + "/"

	if not os.path.isfile(config_file):
		config_file_long = temp_dir + config_file

		_download(CURA_CONFIG_URL+config_file, config_file_long)

		config_file = config_file_long

	if not os.path.isfile(temp_dir+FDMPRINTER_CONFIG):
		_download(CURA_CONFIG_URL + FDMPRINTER_CONFIG, temp_dir+FDMPRINTER_CONFIG)

	if not os.path.isfile(temp_dir+FDMEXTRUDER_CONFIG):
		_download(CURA_CONFIG_URL + FDMEXTRUDER_CONFIG, temp_dir+FDMEXTRUDER_CONFIG)

	cmd = ["CuraEngine", "slice", "-p", "-j", temp_dir+FDMPRINTER_CONFIG, "-j", config_file,"-l", model_file]

	process = subprocess.Popen(cmd, stdout=subprocess.PIPE)
	output = process.communicate()[0]
	print("Output:", output)
	process.wait()
	print('Done')
