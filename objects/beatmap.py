from objects.customstring import CustomString
from objects.rankedstatus import RankedStatus
import struct
import math


class Beatmap:
	def __init__(self, file, osu_version):
		self.__file = file
		if osu_version < 20191106:
			file.read(4) # size of beatmap entry
		self.artist_name = str(CustomString(file))
		CustomString(file, True) # artist_name_unicoe
		self.song_title = str(CustomString(file))
		CustomString(file, True) # song title unicode
		self.creator_name = str(CustomString(file))
		self.difficulty_name = str(CustomString(file))
		CustomString(file, True) # audio file
		CustomString(file, True) # hash
		self.file_name = str(CustomString(file))
		self._ranked_status = RankedStatus(self.__parse_byte())
		file.read(2) # circle count
		file.read(2) # slider count
		file.read(2) # spinner count
		file.read(8) # modification time

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

		print("AR:", self.approach_rate, "HP:", self.hp_drain, "CS:", self.circle_size, "OD:", self.overall_difficulty)

		self.slider_velocity = self.__parse_double()
		self.star_rating = {}
		if osu_version >= 20140609:
			count = self.__parse_int()
			# TODO: parse the int double pars
			for j in range(0, count):
				assert(file.read(1) == b'\x08')
				mod_combination = self.__parse_int()
				assert(file.read(1) == b'\x0d')
				star_rating = self.__parse_double()
				self.star_rating[mod_combination] = star_rating

			for i in range(0,3): # skip the next 3 int-double pairs
				count = self.__parse_int()
				for j in range(0, count):
					file.read(14) # size of int-double pair: byte = 0x08, int, byte = 0x0d, double

		file.read(4) # drain time
		file.read(4) # total time
		file.read(4) # audio preview location time

		self.lowest_bpm = math.inf
		self.highest_bpm = -math.inf
		timing_point_count = self.__parse_int()
		for i in range(0, timing_point_count):
			bpm = self.__parse_double()
			bpm = 60 * 1000 / bpm
			file.read(8) # another double for offset and a boolean
			inherited = int(self.__parse_byte())
			if inherited == 1:
				self.lowest_bpm = min(self.lowest_bpm, bpm)
				self.highest_bpm = max(self.highest_bpm, bpm)

		print("BPM: " + str(self.lowest_bpm) + " - " + str(self.highest_bpm))

		file.read(4) # beatmap id
		file.read(4) # beatmap set id
		file.read(4) # thread id
		file.read(4 * 1) # grade for std, taiko, ctb, mania
		file.read(2) # local beatmap offset
		file.read(4) # stack leniency
		file.read(1) #

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
		return struct.unpack('f', self.__file.read(4))[0]

	def __parse_double(self):
		return struct.unpack('d', self.__file.read(8))[0]
