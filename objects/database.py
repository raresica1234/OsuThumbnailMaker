from objects.customstring import CustomString
from objects.beatmap import Beatmap


class Database:
	def __init__(self, path):
		self.beatmaps = []
		with open(path, "rb") as file:
			self.version = int.from_bytes(file.read(4), byteorder='little')
			self.folder_count = int.from_bytes(file.read(4), byteorder='little')
			file.read(1 + 8) # account unlocked + date time
			self.account_name = str(CustomString(file))
			self.beatmap_count = int.from_bytes(file.read(4), byteorder='little')

			for i in range(0, self.beatmap_count):
				self.beatmaps.append(Beatmap(file, self.version))
