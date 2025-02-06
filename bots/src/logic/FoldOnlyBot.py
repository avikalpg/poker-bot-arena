from src.MoveEnum import MoveEnum

def buyIn(botId, gameObj):
	return gameObj['maxBuyIn']

def move(botId, gameObj, playOptions, hand):
	assert(MoveEnum.FOLD.value in playOptions)
	return MoveEnum.FOLD, 0