from src.MoveEnum import MoveEnum
from src.logic.MoveIntents import MoveIntents
from pokerface import StandardEvaluator, parse_cards
import random


def botPlayer(gameObj, botId):
	return next((p for p in gameObj['players'] if p['username'] == botId), None)

def isBotPlaying(game, botId):
	return botPlayer(game, botId) != None

def checkTurn(game, botId):
	return isBotPlaying(game, botId) and botPlayer(game, botId)['isTurn']

def playerBet(game, botId):
	if not isBotPlaying(game, botId):
		return False
	bet = next((b for b in game['bets'] if b['playerId'] == botId), None)
	return bet['amount'] if bet else False

def largestBet(game):
	if not game or len(game['bets']) == 0:
		return 0
	return max([bet['amount'] for bet in game['bets']])

def amountToCall(game, botId):
	pBet = playerBet(game, botId) or 0
	return largestBet(game) - pBet

def isRoyalCard(card):
	faceCardNum = ['T', 'J', 'Q', 'K', 'A']
	return card[0] in faceCardNum

def isNumberOfCardsMatch(card1,card2):
	return card1[0] == card2[0]

def isSuitOfCardsMatch(card1, card2):
	return card1[1] == card2[1]

def getOrderFromIntent(intent):
	if intent == MoveIntents.ATTACK:
		return [MoveEnum.RAISE, MoveEnum.CALL, MoveEnum.CHECK, MoveEnum.FOLD]
	elif intent == MoveIntents.BET:
		return [MoveEnum.CALL, MoveEnum.RAISE, MoveEnum.CHECK, MoveEnum.FOLD]
	elif intent == MoveIntents.STAY:
		return [MoveEnum.CHECK, MoveEnum.CALL, MoveEnum.FOLD]
	elif intent == MoveIntents.PASSIVE:
		return [MoveEnum.CHECK, MoveEnum.FOLD]
	else:
		# No other order makes any sense
		print("[getOrderFromIntent] received a value that is not handled")
		return [MoveEnum.FOLD]

def playInPriorityOrder(order, playOptions, raiseAmount=0):
	for move in order:
		if move.value in playOptions:
			return move, raiseAmount

def playByIntent(intent, playOptions, raiseAmount=0):
	return playInPriorityOrder(getOrderFromIntent(intent), playOptions, raiseAmount)

def cards_to_range_updated(bot_cards):
    # cards
    c1 = bot_cards[:2]
    c2 = bot_cards[2:]
    
    # card ranks
    card_range = ['A', 'K', 'Q', 'J', 'T', '9', '8', '7', '6', '5', '4', '3', '2']
    
    # pocket pair
    if c1[:-1] == c2[:-1]:
        return c1[:-1]+c2[:-1]
    # suited
    elif c1[-1] == c2[-1]:
        if card_range.index(c1[:-1]) < card_range.index(c2[:-1]):
            return c1[:-1]+c2[:-1]+'s'
        else:
            return c2[:-1]+c1[:-1]+'s'
    # off suited
    else:
        if card_range.index(c1[:-1]) < card_range.index(c2[:-1]):
            return c1[:-1]+c2[:-1]+'o'
        else:
            return c2[:-1]+c1[:-1]+'o'

def hand_strength_bins(hand_strength):
    
    if hand_strength <= 0.1:
        return 'b01'
    elif hand_strength <= 0.2:
        return 'b02'
    elif hand_strength <= 0.3:
        return 'b03'
    elif hand_strength <= 0.4:
        return 'b04'
    elif hand_strength <= 0.5:
        return 'b05'
    elif hand_strength <= 0.6:
        return 'b06'
    elif hand_strength <= 0.7:
        return 'b07'
    elif hand_strength <= 0.8:
        return 'b08'
    elif hand_strength <= 0.9:
        return 'b09'
    else:
        return 'b10'

# normalize sum matrix b/w 1 to 0
def normalize_hand_eval(actual_val):
    
    max_val = 7461
    norm_val = 1 - (actual_val/max_val)
    return norm_val

def eval_hand_postflop(player_cards, comm_cards):
    
    evaluator = StandardEvaluator()
    
    actual_val = evaluator.evaluate_hand(parse_cards(player_cards), parse_cards(comm_cards),).index
    norm_val = normalize_hand_eval(actual_val)
    
    return norm_val

def eval_hand_preflop(player_cards):
    
    preflop_lut = {"AA": 1.0, "AKs": 0.3473919003724204, "AQs": 0.316147687290385, "AJs": 0.3337572786568178, "ATs": 0.2712518132342956, "A9s": 0.28894563640665827, "A8s": 0.2436588238925127, "A7s": 0.24471397193473376, "A6s": 0.2376838310940106, "A5s": 0.2218141730622829, "A4s": 0.23597443982634125, "A3s": 0.22646364015143727, "A2s": 0.19428419682722586, "AKo": 0.36694589617497586, "KK": 0.9305878479866669, "KQs": 0.296967269191992, "KJs": 0.25645112754881605, "KTs": 0.22962329736013676, "K9s": 0.20787702413530584, "K8s": 0.2339795606057491, "K7s": 0.20500767731116665, "K6s": 0.15894927573506712, "K5s": 0.1756246013456514, "K4s": 0.1502451081253473, "K3s": 0.1599661658196334, "K2s": 0.1290566294932204, "AQo": 0.35984374035513667, "KQo": 0.30016325538569166, "QQ": 0.8765065276434642, "QJs": 0.20006532787391218, "QTs": 0.23113464743523815, "Q9s": 0.21386648422871957, "Q8s": 0.20218462583074415, "Q7s": 0.1695448010329006, "Q6s": 0.1458583028126993, "Q5s": 0.13397229480874895, "Q4s": 0.09774779582724635, "Q3s": 0.1337408180901628, "Q2s": 0.09783138464229146, "AJo": 0.3335071552025679, "KJo": 0.2448618598382749, "QJo": 0.2120686817143682, "JJ": 0.8436705906257073, "JTs": 0.22481694049505174, "J9s": 0.1698071413139648, "J8s": 0.1449137492026915, "J7s": 0.15078939990946705, "J6s": 0.12648177249439319, "J5s": 0.12128512016213677, "J4s": 0.09705561613958558, "J3s": 0.06210070266043921, "J2s": 0.09239103876463439, "ATo": 0.28441576562210646, "KTo": 0.2505018543857124, "QTo": 0.22444111232279162, "JTo": 0.2010002366206458, "TT": 0.7635397805600708, "T9s": 0.17530696384848055, "T8s": 0.10865034927264883, "T7s": 0.13474677732968454, "T6s": 0.08585985885064107, "T5s": 0.09239361072817454, "T4s": 0.09024023425443928, "T3s": 0.0867706554391885, "T2s": 0.06072470216662229, "A9o": 0.2622968791794409, "K9o": 0.24751033929343025, "Q9o": 0.20543365877245345, "J9o": 0.17486233565152987, "T9o": 0.1714252278759698, "99": 0.7123152687187506, "98s": 0.1444639770786611, "97s": 0.13957563887574342, "96s": 0.13277954671714576, "95s": 0.10154980093002208, "94s": 0.09872353449517501, "93s": 0.04757007314664308, "92s": 0.06354807514248695, "A8o": 0.25493109709676776, "K8o": 0.23604227536470446, "Q8o": 0.1837600435176232, "J8o": 0.17821971255735491, "T8o": 0.18970095779922225, "98o": 0.16770070317483188, "88": 0.6752838161766219, "87s": 0.12848501059648987, "86s": 0.11270279932511673, "85s": 0.10053355383634088, "84s": 0.0597492849941359, "83s": 0.07609507777617763, "82s": 0.05330233688607233, "A7o": 0.24535535534248287, "K7o": 0.19926094627682578, "Q7o": 0.17481604030781261, "J7o": 0.1600677583794573, "T7o": 0.15250811454496827, "97o": 0.13185556881545657, "87o": 0.13006001676920242, "77": 0.6146423813296022, "76s": 0.10198285529104334, "75s": 0.0919322647682147, "74s": 0.06839944136951914, "73s": 0.04464253564741483, "72s": 0.04163976821464588, "A6o": 0.2706355064710604, "K6o": 0.19492525873953204, "Q6o": 0.17321531449970184, "J6o": 0.1354097009320796, "T6o": 0.12663126787514678, "96o": 0.1442279994238802, "86o": 0.11164636530112548, "76o": 0.10790705180963367, "66": 0.5579842750149173, "65s": 0.06730667836052773, "64s": 0.07269301300384778, "63s": 0.04829440237855209, "62s": 0.019626332277113745, "A5o": 0.24276956749861123, "K5o": 0.20924498724306084, "Q5o": 0.12894989300631676, "J5o": 0.10649922326701111, "T5o": 0.10800575091047515, "95o": 0.11052884714306299, "85o": 0.12029394971296892, "75o": 0.08158879189728618, "65o": 0.08618424775210398, "55": 0.49485800189296514, "54s": 0.057608446842657646, "53s": 0.02536245396185266, "52s": 0.03325452408386653, "A4o": 0.24196229244254253, "K4o": 0.1842577184625832, "Q4o": 0.10356814931791536, "J4o": 0.11520371237217353, "T4o": 0.1153358469990331, "94o": 0.08930436102137818, "84o": 0.09628209810497723, "74o": 0.05506670387440593, "64o": 0.08053171488240984, "54o": 0.05634207629472643, "44": 0.4551041259439106, "43s": 0.040521285570255694, "42s": 0.03332557457665497, "A3o": 0.21453873119894662, "K3o": 0.16026965751733502, "Q3o": 0.14251635768811355, "J3o": 0.0721885866545956, "T3o": 0.08438515925598267, "93o": 0.061899446513446255, "83o": 0.0638891818069588, "73o": 0.07325434404641895, "63o": 0.07379895732598096, "53o": 0.045878042632867655, "43o": 0.07597580296701734, "33": 0.40455861247710967, "32s": 0.0, "A2o": 0.23240101798316903, "K2o": 0.172191351515401, "Q2o": 0.09847341104092533, "J2o": 0.09240196960967895, "T2o": 0.09210780127980922, "92o": 0.08881118701261315, "82o": 0.05699760550194466, "72o": 0.05022626849241807, "62o": 0.050429775107508235, "52o": 0.05723840558836257, "42o": 0.034847534001358205, "32o": 0.02562704471101429, "22": 0.34086393541285154}
    return preflop_lut[player_cards]


def get_req_move(cpdf, ct: str, hsb: str, acst: str) -> (str):
    
    r = random.random()
    # ct = 'FLOP'
    # hsb = 'b07'
    # acst = 'CALL-RAISE-ALL_IN-FOLD'

    rdf = cpdf[(cpdf.current_turn == ct) & (cpdf.hs_bin == hsb) & (cpdf.action_str == acst)]

    pval_call = rdf['pCALL'].item()
    pval_check = rdf['pCHECK'].item()
    pval_raise = rdf['pRAISE'].item()
    pval_fold = rdf['pFOLD'].item()

    if r <= pval_call:
        req_move = 'CALL'
    elif (r > pval_call) & (r <= pval_check):
        req_move = 'CHECK'
    elif (r > pval_check) & (r <= pval_raise):
        req_move = 'RAISE'
    elif (r > pval_raise) & (r <= pval_fold):
        req_move = 'FOLD'
    else:
        req_move = 'ALL_IN'
        
    return req_move
