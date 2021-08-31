import os.path, json, csv
from .serial_reader import FLASH_TIMESTAMP
from .data_handling import TimeSeries
from copy import deepcopy

JSON_INDENT = None # "\t"

root = os.path.dirname(os.path.realpath(__file__))
root = os.path.normpath(os.path.join(root, "..", "data"))


def save_data_to_file_json(data, file):
	"""Write the data in a json file"""
	data = deepcopy(data)
	data = transform_json(data)
	file = os.path.join(root, file)
	with open(file, "w") as source: # valve
		json.dump(data, source, indent=JSON_INDENT)
		return file


def load_json(tm, path):
	tm.time_sync_state = FLASH_TIMESTAMP
	tm.start_time = None
	tm.stream_is_active = False
	with open(path, "r") as source:
		data = json.load(source)
		write_in_json(data, tm.data, tm)		


def transform_json(data):
	"""Transfrom a defaultdict from the telemetry to a dict JSON serializable"""
	if isinstance(data, dict):
		for key, item in data.items():
			data[key] = transform_json(item)
		return data
	elif isinstance(data, TimeSeries):
		data = data.pack()
		res = {"x" : [], "y" : []}
		res["x"] = data[0]
		res["y"] = data[1]
		return res
	else:
		print("A type of data is not managed")


def write_in_json(data, tmdata, tm):
	"""Write the data in a JSON file into the telemetery data"""
	if isinstance(data, dict):
		if len(data) == 2 and "x" in data and "y" in data and\
				isinstance(data["x"], list) and isinstance(data["y"], list):
			tmdata.x = data["x"]
			tmdata.y = data["y"]
			tm.last_timestamp = data["x"][-1] * 1000
		else:
			for key, item in data.items():
				write_in_json(item, tmdata[key], tm)
	else:
		print("A type of data is not managed")


def save_data_to_file_csv(data, file):
	"""Write the data in a json file"""
	data = deepcopy(data)
	data = transform_csv(data)
	max_len = 0
	for liste in data.values():
		max_len = max(max_len, len(liste))
	file = os.path.join(root, file)
	with open(file, "w", newline='') as source:
		writer = csv.DictWriter(source, fieldnames=data.keys(), delimiter=";")
		writer.writeheader()
		for k in range(max_len):
			writer.writerow(get_row(data, k))
		# writer.writerows(data)
		return file


def load_csv(tm, path):
	pass


def transform_csv(data, name=""):
	"""Transfrom a defaultdict from the telemetry to a dict used by save_data_to_file_csv"""
	if isinstance(data, dict):
		res = {}
		for key, item in data.items():
			name += key + "_"
			data_transformed = transform_csv(item, name)
			for new_key, new_item in data_transformed.items():
				res[new_key] = new_item
		return res

	elif isinstance(data, TimeSeries):
		data = data.pack()
		res = {}
		res[name + "x"] = data[0]
		res[name + "y"] = data[1]
		return res

	else:
		print("A type of data is not managed")
		return {}


def get_row(data, row_num):
	res = {}
	for key in data:
		if len(data[key]) > row_num:
			res[key] = data[key][row_num]
		else:
			res[key] = ""
	return res


def write_in_csv(data, tmdata, tm):
	pass
