"""
Home to hold my various experimental strategy code and approaches. To be
used by the server.py code
"""
import random

import global_variables as var


def predict_future_position(current_head, next_move):
    """
    Given the current position of my snake's head, and a proposed move,
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
    Return True if the proposed move avoids running into any list of snakes,
    False if the next move exists in a snake body square.

    # snake eats food, then grows head by 1 square the following move

    TODO - what about snake tails leaving in the next move? A tail may be a
    safe place to move into (assuming no food as in above scenario). In which
    case, this logic needs to be modified to exclude the tail, as that is a safe
    square to move into.

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

def predict_future_position_others(snakes):
    """
    Given the other snakes in the game, predict what the future position of
    the other snakes' heads will be, then don't go in those positions.
    """
    # Empty list so we can fill it with possible moves of where the other snakes' heads could be.
    future_head_others = []

    """The list of others includes us, so we need to filter out "you" before parsing the list"""
    enemies = [snake for snake in snakes if snakes["id"] != "you"]
    print(f"The enemies are: {enemies}")

    # enemies = [snake for snake in snakes if snake != your_body]
    #  Now we have a list of all the other snakes in the game, minus us.

    for snake in enemies:
        this_snake_head = snake["head"]
        # left [x-1,y], right [x+1,y], down [x, y-1] and up [x, y+1]
        
        # if the snake goes left, it will be at x-1, y
        potential_head = {"x": this_snake_head["x"] - 1, "y": this_snake_head["y"]}
        future_head_others.append(potential_head)
        
        # if the snake goes right, it will be at x+1, y
        potential_head = {"x": this_snake_head["x"] + 1, "y": this_snake_head["y"]}
        future_head_others.append(potential_head)
        
        # if the snake goes down, it will be at x, y-1
        potential_head = {"x": this_snake_head["x"], "y": this_snake_head["y"] - 1}
        future_head_others.append(potential_head)
        
        # if the snake goes up, it will be at x, y+1
        potential_head = {"x": this_snake_head["x"], "y": this_snake_head["y"] + 1}
        future_head_others.append(potential_head)
        
    return future_head_others
    print(f"Future head of others could be in these positions: {future_head_others}")
  
def avoid_hazards(future_head, data):
    """
    Return True if the proposed future_head avoids the hazards, False if it means
    you will hit a hazard.
    """
    result = True

    # Get the list of hazards
    hazards = data["hazards"]
    
    # If the future head is in a hazard, return False to mean you'll hit a hazard next turn.
    if future_head in hazards:
        result = False
    return result

def validate_move(your_body, snakes, next_move):
    """
    Basic set of logical checks that only prevent disaster. This function is not
    responsible for picking a move, it is responsible for saying if that move
    if safe.
    Return True if safe, False if not (and another move is needed).
    """
    current_head = your_body[0]
    future_head = predict_future_position(current_head, next_move)
    # print(f"Future head on a {next_move} is as follows: {future_head}")

    safe_wall = avoid_wall(future_head)
    safe_body = avoid_snakes(future_head, snakes)
    # TODO: avoid other snakes' future heads. Function to check other snakes' potential moves is built above.
    # This still doesn't work, so commenting out for the moment.
    # safe_others = future_head not in predict_future_position_others(snakes, your_body)
    
    # TODO: add avoid_hazards and predict_future_position_others to the list of checks.
    # safe_hazards = avoid_hazards(future_head)
    
    # print(f"future_head {future_head}: safe_wall {safe_wall}, safe_body {safe_body}")
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

def choose_move_food(data):
    """
    The food strategy relies on choosing the move that will lead to the closest food
    in the next turn.
    """
    # Get the list of food squares
    food_squares = data["board"]["food"]
    # Get the current snake head position
    current_head_x = data["you"]["head"]["x"]
    current_head_y = data["you"]["head"]["y"]
    current_health = data["you"]["health"]
    # print(f"Current head is at {current_head_x}, {current_head_y}")
    # print(f"Food squares are as follows: {food_squares}")

    # added len(food_squares) > 0 to show food is on the board.
    if int(current_health) < 30 and len(food_squares) > 0:
        # Find the closest food square
        closest_food_x = food_squares[0]["x"]
        closest_food_y = food_squares[0]["y"]

        # move to food
        if closest_food_x < current_head_x:
            move = "left"
        elif closest_food_x > current_head_x:
            move = "right"
        elif closest_food_y < current_head_y:
            move = "down"
        elif closest_food_y > current_head_y:
            move = "up"
        print("I'm hungry")
        return move    

    else:
        # If no food is found, move randomly.
        return choose_move_chaos(data)

