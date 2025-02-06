from src.MoveEnum import MoveEnum
from src.logic.MoveIntents import MoveIntents
from src.logic import utils as u
import pandas as pd
import random

class Singleton:
    __obj = None

    def __init__(self):
        self.cpdf_csv = pd.read_csv("best_bb100_players_pvalues_updated.csv")
        
    @staticmethod
    def createInstance():
        if Singleton.__obj is None:
            print("Creating instance for first time")
            Singleton.__obj = Singleton()
        else:
            print("Reusing already created instance")

        return Singleton.__obj


def buyIn(botId, gameObj):
	# 100% of available limit
	return gameObj['maxBuyIn']

def get_finalMove_raiseAmount(game, botId, final_move):
	
	# when we want to raise
	raiseLimit = u.botPlayer(game, botId)['chips'] - u.amountToCall(game, botId)

	if final_move == 'CALL':
		final_move = MoveEnum.CALL
		raiseAmount = min(u.botPlayer(game, botId)['chips'], u.amountToCall(game, botId) )
	elif final_move == 'CHECK':
		final_move = MoveEnum.CHECK
		raiseAmount = 0
	elif final_move == 'RAISE': 
		final_move = MoveEnum.RAISE
		raiseAmount = min(raiseLimit, max(u.amountToCall(game, botId), random.randint(2,30)*5 ))
	elif final_move == 'ALL_IN' :
		final_move = MoveEnum.RAISE
		raiseAmount = min(raiseLimit, max(u.amountToCall(game, botId), random.randint(30,60)*5 ))
	else:
		final_move = MoveEnum.FOLD
		raiseAmount = 0
	
	return final_move, raiseAmount

def move(botId, gameObj, playOptions, hand):
 
	# convert AH, AS -> Ah, As (for postflop) -> AA (for preflop)
	bot_cards = "".join([i[0] + i[1].lower() for i in hand])
 
	community_cards = gameObj['communityCards']
 
	# convert AH, QH, KH -> AhQhKh
	if len(community_cards) > 0:
		community_cards = "".join([i[0] + i[1].lower() for i in community_cards])
 
	# get current phase
	current_phase = gameObj['phase']

	# eval hand strength
	if current_phase == 'PREFLOP':
		current_phase = 'PRE_FLOP'
		bot_cards = u.cards_to_range_updated(bot_cards)
		hs = u.eval_hand_preflop(bot_cards)
	else:
		hs = u.eval_hand_postflop(bot_cards, community_cards)
  
	# hand strength to bin
	hs_bin = u.hand_strength_bins(hs)
  
	# fetch action str
	if 'call' in playOptions:
		action_str = "CALL-RAISE-ALL_IN-FOLD"
	else:
		action_str = "CHECK-RAISE-ALL_IN-FOLD"
  
	# fetch move probabilities
	cpdfObj = Singleton.createInstance()
	cpdf = cpdfObj.cpdf_csv
	
	# fetch final move and raise amount
	final_move = u.get_req_move(cpdf, current_phase, hs_bin, action_str)
	final_move, raiseAmount = get_finalMove_raiseAmount(gameObj, botId, final_move)
	
	return final_move, raiseAmount