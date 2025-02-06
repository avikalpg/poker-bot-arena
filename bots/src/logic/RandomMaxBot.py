from src.MoveEnum import MoveEnum
from src.logic import utils as u
import random

def buyIn(botId, gameObj):
	# On searching for minimum buy in value on the web, I saw these two answes:
	# 1. 10-times the big-blind amount
	# 2. 20% of the max-buy-in amount
	minBuyIn =  min(10*gameObj['bigBlind'], int(0.2 * gameObj['maxBuyIn']))
	maxBuyIn = gameObj['maxBuyIn']
	return random.randint(minBuyIn, maxBuyIn)

def move(botId, gameObj, playOptions, hand):
	moveIndex = random.randint(0, len(playOptions)-1)
	move = MoveEnum.getMove(playOptions[moveIndex])

	if move == MoveEnum.RAISE:
		raiseLimit = u.botPlayer(gameObj, botId)['chips'] - u.amountToCall(gameObj, botId)
		raiseAmount = random.randint(1, raiseLimit)
		return move, raiseAmount

	return move, 0
