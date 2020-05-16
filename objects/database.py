from objects.customstring import CustomString
from objects.beatmap import Beatmap


class Database:
	def __init__(self, path):
		with open(path, "rb") as file:
			self.version = int.from_bytes(file.read(4), byteorder='little')
			self.folder_count = int.from_bytes(file.read(4), byteorder='little')
			file.read(1 + 8) # osu version + folder count + account unlocked + date time
			self.account_name = str(CustomString(file))
			self.beatmap_count = int.from_bytes(file.read(4), byteorder='little')
			beatmap = Beatmap(file, self.version)
			print(str(beatmap))