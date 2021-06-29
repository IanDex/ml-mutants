from flask import Flask, request, Response, json

from db import select_stats
from functions import is_mutant

app = Flask(__name__)


@app.route('/mutant/', methods=['POST'])
def mutant():
    json_data = request.json
    dna = json_data["dna"]
    board = []
    for i in dna:
        board.append(list(i))
    is_m = is_mutant(dna, board, 0)
    if is_m:
        return Response(status=200)
    else:
        return Response(status=403)


@app.route('/stats/', methods=['POST'])
def stats():
    (_mutant, human, ratio) = select_stats()
    return Response(response=json.dumps({
        "count_mutant_dna": _mutant,
        "count_human_dna": human,
        "ratio": ratio,
    }), status=200, mimetype='application/json')


if __name__ == '__main__':
    app.run()
