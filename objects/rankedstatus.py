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
