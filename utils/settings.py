import os.path


class Settings:
	def __init__(self, path):
		self._path = path
		self._args = {}

		if os.path.isfile(path):
			with open(self._path) as file:
				line = file.readline()
				line = line.split("=")
				self._args[line[0]] = line[1]

	def __getitem__(self, item):
		if item not in self._args.keys():
			return None
		return self._args[item]

	def __setitem__(self, key, value):
		self._args[key] = value

	def save(self):
		with open(self._path, "w") as file:
			for key, value in self._args.items():
				file.write(str(key) + "=" + str(value))
