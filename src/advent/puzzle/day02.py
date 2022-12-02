from advent.io import read

ROCK = "A"
PAPER = "B"
SCISSORS = "C"

SHAPES_SCORES = {
    ROCK: 1,
    PAPER: 2,
    SCISSORS: 3
}

RESULTS_PLAYING_AGAINST = {
    ROCK: {
        ROCK: "draw",
        PAPER: "win",
        SCISSORS: "lose"
    },
    PAPER: {
        ROCK: "lose",
        PAPER: "draw",
        SCISSORS: "win"
    },
    SCISSORS: {
        ROCK: "win",
        PAPER: "lose",
        SCISSORS: "draw"
    },
}

MATCH_SCORES = {
    "win": 6,
    "draw": 3,
    "lose": 0
}

# puzzle 1
SHAPES_ALIAS = {
    "X": ROCK,
    "Y": PAPER,
    "Z": SCISSORS
}

# puzzle 2
MATCHS_RESULTS_ALIAS = {
    "X": "lose",
    "Y": "draw",
    "Z": "win"
}


class Puzzle(object):

    @classmethod
    def resolve_part_01(cls, data):
        score = 0
        for round in data:
            opponent_shape, player_shape = round.split(" ")
            player_shape = SHAPES_ALIAS[player_shape]
            shape_score = SHAPES_SCORES[player_shape]
            match_result = RESULTS_PLAYING_AGAINST[opponent_shape][player_shape]
            match_score = MATCH_SCORES[match_result]
            score += shape_score + match_score
        return score

    @classmethod
    def resolve_part_02(cls, data):
        score = 0
        for round in data:
            opponent_shape, match_result = round.split(" ")
            match_result = MATCHS_RESULTS_ALIAS[match_result]
            match_score = MATCH_SCORES[match_result]
            possible_player_shapes = RESULTS_PLAYING_AGAINST[opponent_shape]
            player_shape = [
                shape
                for shape, result in possible_player_shapes.items()
                if result == match_result
            ][0]
            shape_score = SHAPES_SCORES[player_shape]
            score += shape_score + match_score
        return score

