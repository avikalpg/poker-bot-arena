from enum import Enum, unique

@unique
class MoveEnum(Enum):
	FOLD = 'fold'
	CHECK = 'check'
	CALL = 'call'
	RAISE = 'raise'

	@classmethod
	def getMove(cls, value):
		return [item for item in MoveEnum if item.value == value][0]