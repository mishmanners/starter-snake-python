import os

import cherrypy

import global_variables
import strategy

"""
This is a simple Battlesnake server written in Python.
For instructions see https://github.com/BattlesnakeOfficial/starter-snake-python/README.md
"""

# Code for the Sneki Snek Battlesnake.

class Battlesnake(object):
    @cherrypy.expose
    @cherrypy.tools.json_out()
    def index(self):
        # This function is called when you register your Battlesnake on play.battlesnake.com
        # It controls your Battlesnake appearance and author permissions.
        # TIP: If you open your Battlesnake URL in browser you should see this data
        return {
            "apiversion": "1",
            "author": "mishmanners", # BattleSnake Username
            "color": "#E0115F",  # Personalize
            "head": "caffeine",  # Personalize
            "tail": "curled",  # Personalize
        }

    @cherrypy.expose
    @cherrypy.tools.json_in()
    def start(self):
        # This function is called everytime your snake is entered into a game.
        # cherrypy.request.json contains information about the game that's about to be played.
        
        """
        Treat this as game initialization - should only set global_variables
        here.

        { "game":  { "id":  "unique-game-id", "timeout" : 500 }
          "turn": 123
          "board": "height": 1, "width", 1, "food": [ ], "hazards": [ ], "snakes" : [ ],
          "you": { }
        """
        
        data = cherrypy.request.json

        print(f"~~  START NEW GAME ~~~{data['game']['id']}")
        # maximum x and y coordinates are one less than the size (zero index)
        global_variables.BOARD_MAXIMUM_X = data["board"]["width"] - 1
        global_variables.BOARD_MAXIMUM_Y = data["board"]["height"] - 1
        global_variables.GAME_ON = True

        print("START")
        return "ok"

    @cherrypy.expose
    @cherrypy.tools.json_in()
    @cherrypy.tools.json_out()
    def move(self):
        # This function is called on every turn of a game. It's how your snake decides where to move.
        # Valid moves are "up", "down", "left", or "right".
        # TODO: Use the information in cherrypy.request.json to decide your next move.
        data = cherrypy.request.json

        # Enter data
        your_health = data["you"]["health"]
        your_body = data["you"]["body"]
        snakes = data["board"]["snakes"]
        print(f"Data in move is: {data}")

        while global_variables.GAME_ON and your_health > 0:
            move = strategy.choose_move_food(data)
            safe = strategy.validate_move(your_body, snakes, move)
            if safe:
                break

        print(f"Huzzah! I move : {move}")
        return {"move": move }

    @cherrypy.expose
    @cherrypy.tools.json_in()
    def end(self):
        # This function is called when a game your snake was in ends.
        # It's purely for informational purposes, you don't have to make any decisions here.
        data = cherrypy.request.json

        global_variables.GAME_ON = False

        print("Yay we finished the game! Did we win? We totally won right?")
        return "ok"


if __name__ == "__main__":
    server = Battlesnake()
    cherrypy.config.update({"server.socket_host": "0.0.0.0"})
    cherrypy.config.update(
        {"server.socket_port": int(os.environ.get("PORT", "8080")),}
    )
    print("Entering the server of Snakes...")
    cherrypy.quickstart(server)


