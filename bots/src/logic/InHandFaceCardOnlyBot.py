from src.MoveEnum import MoveEnum
from src.logic.MoveIntents import MoveIntents
from src.logic import utils as u

def buyIn(botId, gameObj):
	# just choosing to buy in with 80% of available limit
	return int(0.8 * gameObj['maxBuyIn'])

def calculateRaiseAmount(game, botId):
	# when we want to raise
	raiseLimit = u.botPlayer(game, botId)['chips'] - u.amountToCall(game, botId)
	raiseAmount = min(raiseLimit, max(u.amountToCall(game, botId), 10))
	return raiseAmount

def move(botId, gameObj, playOptions, hand):
	raiseAmount = calculateRaiseAmount(gameObj, botId)
	if (u.isRoyalCard(hand[0]) and u.isRoyalCard(hand[1]) and (hand[0][0] == hand[1][0])):
		return u.playByIntent(MoveIntents.ATTACK, playOptions, raiseAmount)
	elif (u.isRoyalCard(hand[0]) and u.isRoyalCard(hand[1])):
		return u.playByIntent(MoveIntents.BET, playOptions, raiseAmount)
	elif (u.isRoyalCard(hand[0]) or u.isRoyalCard(hand[1])):
		return u.playByIntent(MoveIntents.STAY, playOptions, raiseAmount)
	else:
		return u.playByIntent(MoveIntents.PASSIVE, playOptions, raiseAmount)
