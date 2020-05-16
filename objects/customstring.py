import leb128


class CustomString:
	def __init__(self, file, skip: bool = False):
		byte = file.read(1)
		if byte == b'\x00':  # Next two parts are not present
			self._str = ""
		elif byte == b'\x0b':
			length = leb128.u.decode_reader(file)
			# print(length)
			characters = file.read(length[0])
			self._str = str(characters, "utf-8")
		else:
			raise ValueError("Could not parse String")

	def __str__(self):
		return self._str

