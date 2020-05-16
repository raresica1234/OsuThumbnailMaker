from enum import Enum


class RankedStatus(Enum):
	UNKNOWN = 0
	UNSUBMITTED = 1
	PENDING_WIP_GRAVEYARD = 2
	UNUSED = 3
	RANKED = 4
	APPROVED = 5
	QUALIFIED = 6
	LOVED = 7
'''
	def __str__(self):
		print(self.value)
		if self.value == RankedStatus.UNKNOWN:
			return "UNKNOWN"
		if self.value in [RankedStatus.UNSUBMITTED, RankedStatus.PENDING_WIP_GRAVEYARD, RankedStatus.UNUSED]:
			return "UNRANKED"
		if self.value == RankedStatus.RANKED:
			return "RANKED"
		if self.value == RankedStatus.APPROVED:
			return "APPROVED"
		if self.value == RankedStatus.QUALIFIED:
			return "QUALIFIED"
		if self.value == RankedStatus.LOVED:
			return "LOVED"
'''