from collections import defaultdict
from src.logic import utils as u
from src.logic.MoveIntents import MoveIntents

def buyIn(botId, gameObj):
	return gameObj['maxBuyIn']

def calculateRaiseAmount(game, botId, intent):
	intentToRaiseAmount = {
		MoveIntents.ATTACK: game['bigBlind'] * 10,
		MoveIntents.BET: game['bigBlind'],
	}
	raiseLimit = u.botPlayer(game, botId)['chips'] - u.amountToCall(game, botId)
	raiseAmount = min(raiseLimit, max(u.amountToCall(game, botId), intentToRaiseAmount[intent]))
	return raiseAmount

def isFlush(cards):
	suitCount = defaultdict(int)
	for card in cards:
		suitCount[card[1]] += 1
	return max(suitCount.values()) >= 5

def move(botId, gameObj, playOptions, hand):
	community_cards = gameObj['communityCards']
	if (len(community_cards) == 0):
		return u.playByIntent(MoveIntents.STAY, playOptions, 0)

	if isFlush(community_cards + hand):
		raiseAmount = calculateRaiseAmount(gameObj, botId, MoveIntents.ATTACK)
		return u.playByIntent(MoveIntents.ATTACK, playOptions, raiseAmount)

	if u.isRoyalCard(hand[0]) and u.isNumberOfCardsMatch(hand[0], hand[1]):
		raiseAmount = calculateRaiseAmount(gameObj, botId, MoveIntents.ATTACK)
		return u.playByIntent(MoveIntents.ATTACK, playOptions, raiseAmount)

	for c_card in community_cards:
		if u.isRoyalCard(c_card) and (u.isNumberOfCardsMatch(c_card, hand[0]) or u.isNumberOfCardsMatch(c_card, hand[1])):
			# high pair or more
			raiseAmount = calculateRaiseAmount(gameObj, botId, MoveIntents.ATTACK)
			if u.amountToCall(gameObj, botId) <= raiseAmount:
				return u.playByIntent(MoveIntents.ATTACK, playOptions, raiseAmount)
			else:
				return u.playByIntent(MoveIntents.STAY, playOptions, raiseAmount)

		if (u.isNumberOfCardsMatch(c_card, hand[0]) or u.isNumberOfCardsMatch(c_card, hand[1])):
			raiseAmount = calculateRaiseAmount(gameObj, botId, MoveIntents.BET)
			if u.amountToCall(gameObj, botId) <= raiseAmount:
				return u.playByIntent(MoveIntents.BET, playOptions, raiseAmount)

	if u.isRoyalCard(hand[0]) or u.isRoyalCard(hand[1]):
		if u.amountToCall(gameObj, botId) <= calculateRaiseAmount(gameObj, botId, MoveIntents.BET):
			return u.playByIntent(MoveIntents.STAY, playOptions)

	return u.playByIntent(MoveIntents.PASSIVE, playOptions)