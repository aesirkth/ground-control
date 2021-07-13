import os.path, json
from .serial_reader import FLASH_TIMESTAMP
from .data_handling import TimeSeries
from copy import deepcopy

root = os.path.dirname(os.path.realpath(__file__))
root = os.path.normpath(os.path.join(root, "..", "data"))


def save_data_to_file_json(data, file):
	"""Write the data in a json file"""
	data = deepcopy(data)
	data = transform(data)
	file = os.path.join(root, file)
	with open(file, "w") as source: # valve
		json.dump(data, source)
		return file


def load_json(tm, path):
	tm.time_sync_state = FLASH_TIMESTAMP
	tm.start_time = None
	tm.stream_is_active = False
	with open(path, "r") as source:
		data = json.load(source)
		write_in(data, tm.data)		


def transform(data):
	"""Transfrom a defaultdict from the telemetry to a dict JSON serializable"""
	if isinstance(data, dict):
		for key, item in data.items():
			data[key] = transform(item)
		return data
	elif isinstance(data, TimeSeries):
		data = data.pack()
		return data
	else:
		print("A type of data is not managed")


def write_in(data, tmdata):
	"""Write the data in a JSON file into the telemetery data"""
	if isinstance(data, dict):
		for key, item in data.items():
			write_in(item, tmdata[key])
	elif isinstance(data, list) and len(data) == 2:
		if isinstance(data[0], list) and isinstance(data[1], list):
			tmdata.x = data[0]
			tmdata.y = data[1]
		else:
			print("A type of data is not managed")
	else:
		print("A type of data is not managed")
