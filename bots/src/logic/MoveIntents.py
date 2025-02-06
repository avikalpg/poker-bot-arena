from enum import Enum, auto, unique

@unique
class MoveIntents(Enum):
	ATTACK = auto()
	BET = auto()
	STAY = auto()
	PASSIVE = auto()
