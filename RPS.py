# The example function below keeps track of the opponent's history and plays whatever the opponent played two plays ago. It is not a very good player so you will need to change the code to pass the challenge.

# def player(prev_play, opponent_history=[]):
#     opponent_history.append(prev_play)

#     guess = "R"
#     if len(opponent_history) > 2:
#         guess = opponent_history[-2]

#     return guess


import random

opponent_history = []

def beat(move):
    return {'R': 'P', 'P': 'S', 'S': 'R'}[move]

def player(prev_play):
    global opponent_history

    if prev_play == "":
        opponent_history = []

    if prev_play:
        opponent_history.append(prev_play)

    if len(opponent_history) < 5:
        return random.choice(['R', 'P', 'S'])

    transitions = {}
    for i in range(len(opponent_history) - 2):
        pair = (opponent_history[i], opponent_history[i + 1])
        next_move = opponent_history[i + 2]
        transitions.setdefault(pair, {'R': 0, 'P': 0, 'S': 0})
        transitions[pair][next_move] += 1

    last_pair = (opponent_history[-2], opponent_history[-1])
    if last_pair in transitions:
        prediction = max(transitions[last_pair], key=transitions[last_pair].get)
    else:
        freq = {'R': 0, 'P': 0, 'S': 0}
        for m in opponent_history:
            freq[m] += 1
        prediction = max(freq, key=freq.get)

    return beat(prediction)
