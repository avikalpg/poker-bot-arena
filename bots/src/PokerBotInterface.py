from typing import Tuple
from src.BotVariants import BotVariants, getBotFromVariant

def AIBotBuyIn(botId: str, variant: BotVariants, gameObj: dict) -> int:
	buyInAmount = getBotFromVariant(variant).buyIn(botId, gameObj)
	return buyInAmount

def AIBotMove(botId: str, variant: BotVariants, gameObj: dict, playOptions: list[str], hand: list[str]) -> Tuple[str, int]:
	move, raiseAmount = getBotFromVariant(variant).move(botId, gameObj, playOptions, hand)
	return move.value, raiseAmount