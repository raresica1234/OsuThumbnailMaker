from objects.customstring import CustomString
from objects.rankedstatus import RankedStatus
import struct


class Beatmap:
	def __init__(self, file, osu_version):
		self.__file = file
		if osu_version < 20191106:
			file.read(4) # size of beatmap entry
		self.artist_name = str(CustomString(file))
		self.artist_name_unicode = str(CustomString(file))
		self.song_title = str(CustomString(file))
		self.song_title_unicode = str(CustomString(file))
		self.creator_name = str(CustomString(file))
		self.difficulty_name = str(CustomString(file))
		self.audio_file = str(CustomString(file))
		self.hash = str(CustomString(file))
		self.file_name = str(CustomString(file))
		self._ranked_status = RankedStatus(self.__parse_byte())
		self.circle_count = self.__parse_short()
		self.slider_count = self.__parse_short()
		self.spinner_count = self.__parse_short()
		self.modification_time = self.__parse_long()

		print(self.file_name)

		if osu_version < 20140609:
			self.approach_rate = float(file.read(1))
			self.circle_size = float(file.read(1))
			self.hp_drain = float(file.read(1))
			self.overall_difficulty = float(file.read(1))
		else:
			self.approach_rate = self.__parse_float()
			self.circle_size = self.__parse_float()
			self.hp_drain = self.__parse_float()
			self.overall_difficulty = self.__parse_float()

		self.slider_velocity = self.__parse_double()

	@property
	def ranked_status(self):
		return str(self._ranked_status).split(".")[1]

	def __str__(self):
		return self.artist_name + " - " + self.song_title + " [" + self.difficulty_name + "] " + str(self.ranked_status)

	def __parse_byte(self):
		return int.from_bytes(self.__file.read(1), byteorder='little')

	def __parse_short(self):
		return int.from_bytes(self.__file.read(2), byteorder='little')

	def __parse_int(self):
		return int.from_bytes(self.__file.read(4), byteorder='little')

	def __parse_long(self):
		return int.from_bytes(self.__file.read(8), byteorder='little')

	def __parse_float(self):
		return struct.unpack('f', self.__file.read(4))

	def __parse_double(self):
		return struct.unpack('d', self.__file.read(8))
