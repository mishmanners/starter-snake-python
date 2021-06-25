"""
Home to hold my various experimental strategy code and appraoches. To be
used by the server.py code
"""
import random

import global_variables as var


def _predict_future_position(current_head, next_move):
    """
    Given the current snake head position, and a proposed move,
    returns what the new snake head position would be.
    """
    # Get a clean copy, otherwise will modify the current head!
    future_head = current_head.copy()

    if next_move in ["left", "right"]:
        # moving left means decreasing x by 1, right increase by 1
        future_head["x"] = current_head["x"] + var.MOVE_LOOKUP[next_move]
    elif next_move in ["up", "down"]:
        # moving up means increasing y by 1, down decrease by 1
        future_head["y"] = current_head["y"] + var.MOVE_LOOKUP[next_move]
    return future_head


def avoid_wall(future_head):
    """
    Return True if the proposed future_head avoids a wall, False if it means
    you will hit a wall.
    """
    result = True

    x = int(future_head["x"])
    y = int(future_head["y"])

    if x < 0 or y < 0 or x > var.BOARD_MAXIMUM_X or y > var.BOARD_MAXIMUM_Y:
        result = False
    return result


def avoid_snakes(future_head, snake_bodies):
    """
    Return True of the proposed move avoids running into any list of snakes,
    False if the next move exists in a snake body square.

    Recommend taking the default data from the board snakes as per the battlesnake
    API. Note that the list of board snakes includes yourself!

    TODO - this is basic, may want to add in a check to see if any heads are
    about to eat food, and may extend by a square! Does the tail grow first,
    or does the head grow? Find out what happens in the game and see if we need
    to check for if a snake suddenly grows.

    TODO - what about snake tails leaving in the next move? A tail may be a
    safe place to move into (assuming no food as in above scenario). In which
    case, this logic needs to be modified to exclude the tail, as that is a safe
    square to move into. LOOK INTO THIS LATER when implementing chicken snake
    approach, as that is a key concept with that!

    TODO - and on that note, what about anticipating another snakes head, and
    if you are destined to occupy the same square another snake is about to?
    That might be logic for somwhere else - I'll have to think about that.

    @:param: snake_bodies list of dictionary of snake bodies

       [ {'id': 'a', 'name': 'Snek', 'health': 42, 'body': [{'x': 1, 'y': 2}, {'x': 1, 'y': 3}, {'x': 1, 'y': 4}], 'head': {'x': 1, 'y': 2}, 'length': 3, 'shout': "ah!", 'squad': "1"],
         {'id': 'b', 'name': 'SNAKE' 'health': 42, 'body': [{'x': 4, 'y': 2}, {'x': 4, 'y': 3}, {'x': 4, 'y': 4}], 'head': {'x': 4, 'y': 3}, 'length': 3, 'shout': "ah!", 'squad': "2"],
         {'id': 'c', 'name': 'you' 'health': 42, 'body': [{'x': 1, 'y': 10}, {'x': 1, 'y': 9}, {'x': 1, 'y': 8}], 'head': {'x': 1, 'y': 9}, 'length': 3, 'shout': "ah!", 'squad': "3"]
        ]
    """
    for snake in snake_bodies:
        if future_head in snake["body"]:
            return False
    return True


def validate_move(your_body, snakes, next_move):
    """
    Basic set of logical checks that only prevent disaster. This function is not
    responsible for picking a move, it is responsible for saying if that move
    if safe.
    Return True if safe, False if not (and another move is needed).
    """
    current_head = your_body[0]
    future_head = _predict_future_position(current_head, next_move)
    print(f"Future head on a {next_move} is as follows: {future_head}")

    safe_wall = avoid_wall(future_head)
    safe_body = avoid_snakes(future_head, snakes)

    print(f"future_head {future_head}: safe_wall {safe_wall}, safe_body {safe_body}")
    is_safe = safe_wall and safe_body

    return is_safe


def choose_move_chaos(data):
    """
    The chaos strategy relies on randomly choosing a next move, any move, to
    keep the competition guessing!

    return a potential future_head of the snake as a dict {'x': 1, 'y': 1}
    """
    possible_moves = ["up", "down", "left", "right"]

    move = random.choice(possible_moves)
    return move
