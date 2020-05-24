from objects.customstring import CustomString
from objects.beatmap import Beatmap


class Database:
	def __init__(self, path, beatmap_set_id = None, beatmap_id = None):
		self.beatmaps = []
		self.search_result = 0
		with open(path, "rb") as file:
			self.version = int.from_bytes(file.read(4), byteorder='little')
			self.folder_count = int.from_bytes(file.read(4), byteorder='little')
			file.read(1 + 8) # account unlocked + date time
			self.account_name = str(CustomString(file))
			self.beatmap_count = int.from_bytes(file.read(4), byteorder='little')

			for i in range(0, self.beatmap_count):
				currentbeatmap = Beatmap(file, self.version)
				self.beatmaps.append(currentbeatmap)
				if beatmap_set_id is not None and beatmap_id is not None:
					if currentbeatmap.beatmap_set_id == beatmap_set_id and currentbeatmap.beatmap_id == beatmap_id:
						self.search_result = currentbeatmap
						return
