# The example function below keeps track of the opponent's history and plays whatever the opponent played two plays ago. It is not a very good player so you will need to change the code to pass the challenge.

# def player(prev_play, opponent_history=[]):
#     opponent_history.append(prev_play)

#     guess = "R"
#     if len(opponent_history) > 2:
#         guess = opponent_history[-2]

#     return guess


import random

def player(prev_play, opponent_history=[]):
    opponent_history.append(prev_play)

    # Only use actual moves
    moves = [m for m in opponent_history if m]

    if len(moves) < 5:
        return "R"  # Start with R a few times

    # Build a move sequence pattern dictionary
    pattern_length = 3
    pattern_dict = {}

    for i in range(len(moves) - pattern_length):
        pattern = tuple(moves[i:i + pattern_length])
        next_move = moves[i + pattern_length]
        if pattern not in pattern_dict:
            pattern_dict[pattern] = {"R": 0, "P": 0, "S": 0}
        pattern_dict[pattern][next_move] += 1

    # Get the most recent pattern
    last_pattern = tuple(moves[-pattern_length:])

    # Predict opponent's next move
    if last_pattern in pattern_dict:
        predicted_move = max(pattern_dict[last_pattern], key=pattern_dict[last_pattern].get)
    else:
        predicted_move = "R"

    # Counter the predicted move
    counter = {"R": "P", "P": "S", "S": "R"}
    return counter[predicted_move]

