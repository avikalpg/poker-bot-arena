from datetime import datetime
from flask import Flask, Response, jsonify, request
from src.PokerBotInterface import AIBotMove, AIBotBuyIn
from src.BotVariants import BotVariants
from src.VariantAssigner import getVariants

app = Flask(__name__)

@app.route("/", methods=['GET'])
def ping() -> Response:
	return 'PONG timestamp: ' + datetime.now().strftime("%m/%d/%Y, %H:%M:%S:%f")

@app.route('/variants/<int:num_bots>', methods=['GET'])
def get_bot_variants(num_bots: int) -> Response:
	variant_list = [variant.value for variant in getVariants(num_bots)]
	return jsonify(variant_list)

@app.route('/buyIn/<string:variant>', methods=['POST'])
def bot_buyIn(variant: str) -> Response:
	if not BotVariants.has_value(variant):
		return "Invalid value for bot-variant", 400
	variant = BotVariants.get_member_from_value(variant)

	data = request.get_json()
	buyInAmount = AIBotBuyIn(data['botId'], variant, data['game'])
	return jsonify(buyInAmount)

@app.route('/bot/<string:variant>', methods=['POST'])
def bot_play(variant: str) -> Response:
	if not BotVariants.has_value(variant):
		return "Invalid value for bot-variant", 400
	variant = BotVariants.get_member_from_value(variant)

	data = request.get_json()
	move, raiseAmount = AIBotMove( data['botId'], variant, data['game'], data['playOptions'], data['hand'])
	return {
		'move': move,
		'raiseAmount': raiseAmount
	}

if __name__ == '__main__':
	app.run()