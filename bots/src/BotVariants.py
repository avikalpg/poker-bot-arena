from enum import Enum, unique
from src.logic import FoldOnlyBot, RandomMaxBot, InHandFaceCardOnlyBot, RuleBasedBot01, ProBot

@unique
class BotVariants(Enum):
	FOLD_ONLY = 'FoldOnly'
	RANDOM_MAX = 'RandomMax'
	IN_HAND_ROYAL_ONLY = 'InHandRoyalCardOnly'
	PAIR_AND_FLUSH = 'PairAndFlushBettor'
	PRO_BOT = 'Pro'

	@classmethod
	def has_value(cls, value):
		values = [item.value for item in BotVariants]
		return value in values

	@classmethod
	def get_member_from_value(cls, value):
		return [item for item in BotVariants if item.value == value][0]

def getBotFromVariant(variant: BotVariants):
	variantToBotMap = {
		BotVariants.FOLD_ONLY: FoldOnlyBot,
		BotVariants.RANDOM_MAX: RandomMaxBot,
		BotVariants.IN_HAND_ROYAL_ONLY: InHandFaceCardOnlyBot,
		BotVariants.PAIR_AND_FLUSH: RuleBasedBot01,
		BotVariants.PRO_BOT: ProBot
	}
	if variant in variantToBotMap.keys():
		return variantToBotMap[variant]
	else:
		raise NotImplementedError("No implemention found for variant: " + variant)
