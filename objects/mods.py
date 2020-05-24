from enum import Enum


class Mods(Enum):
	NO_MOD = 0
	EASY = 1 << 2
	HARD_ROCK = 1 << 4
	DOUBLE_TIME = 1 << 6
	HALF_TIME = 1 << 8
