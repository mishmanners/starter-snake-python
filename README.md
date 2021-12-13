# A Simple [Battlesnake](http://play.battlesnake.com) Written in Python

This repo has been cloned from the [Official Battlesnake Starter-Snake](https://github.com/BattlesnakeOfficial/starter-snake-python).

## Find my Battlesnake

Right now, I'm playing [Battlesnake](https://play.battlesnake.com/u/mishmanners/) 🐍 [Fork the repo](https://github.com/orgs/BattlesnakeOfficial/repositories) (choose from Python, Go, or Java starter snakes), make your snake, and come play with us!

If you are forking the repo, add "Battlesnake" to the tags and you'll appear on the [official Battlesnake tag](https://twitter.com/playbattlesnake/status/1470159791762796550). As of Dec 2021, there are over 1000 Battlesnake repos! 😲

<a href="https://play.battlesnake.com" target="blank"><img align="" src="https://github.com/mishmanners/starter-snake-python/blob/main/images/68747470733a2f2f6d656469612e626174746c65736e616b652e636f6d2f736f6369616c2f476974487562536f6369616c2e706e67.png" width="400" /></a>

This is a basic implementation of the [Battlesnake API](https://docs.battlesnake.com/references/api). It's a great starting point for anyone wanting to program their first Battlesnake using Python. It comes ready to use with [Repl.it](https://repl.it) and provides instructions below for getting started. It can also be deployed to [Heroku](https://heroku.com), or any other cloud provider you'd like.

### Technologies Used

* [Python3](https://www.python.org/)
* [CherryPy](https://cherrypy.org/)

## Prerequisites

* [Battlesnake Account](https://play.battlesnake.com) <!-- done !-->
* [Repl.it Account](https://repl.it) <!-- done !-->
* [GitHub Account](https://github.com) (Optional) <!-- done !-->

## Running Your Battlesnake on [Repl.it](https://repl.it)

[![Run on Repl.it](https://repl.it/badge/github/BattlesnakeOfficial/starter-snake-python)](https://repl.it/github/BattlesnakeOfficial/starter-snake-python)

Big note with Replit is to ensure you regularly check in on the server. If you don't, the server will go to sleep and your Battlesnake will not run. Learned this the hard way!

1. Login to your [Repl.it](https://repl.it) account.

2. Click the 'Run on Repl.it' button above, or visit the following URL: https://repl.it/github/BattlesnakeOfficial/starter-snake-python.

3. You should see your Repl being initialized - this might take a few moments to complete.

4. Once your Repl is ready to run, click `Run ▶️` at the top of the screen. You should see CherryPy (and any other dependencies) being installed. Once installation is complete, your Battlesnake server will start and you should see the following:

    ```
    Starting Battlesnake Server...
    ENGINE Serving on http://0.0.0.0:8080
    ```

5. Above the terminal window you'll see the live output from your Battlesnake server, including its URL. That URL will be the URL used to create your Battlesnake in the next step. If you visit that URL in your browser, you should see text similar to this:

    ```
    {"apiversion": "1", "author": "", "color": "#888888", "head": "default", "tail": "default"}
    ```

This means your Battlesnake is running correctly on Repl.it.

**At this point your Battlesnake is live and ready to enter games!**

We used Replit to run this Sneki Snek. However, considering changing it for next season due to timeouts and latency issues.

If you don't know what a Sneki Snek is (the name I gave to my Battlesnake), check out [Sneki Snek on the Razer website](https://www.razer.com/gear-accessories/razer-sneki-snek-plushie/).

<a href="https://www.razer.com/gear-accessories/razer-sneki-snek-plushie/" target="blank"><img align="" src="https://github.com/mishmanners/starter-snake-python/blob/main/images/plushie.jpg" width="400" /></a>

This adorable plushie has planted lots of trees! 🌳

## Registering and battling

**At this point you should have a registered Battlesnake and be able to create games!**

Sneki Snek has battled in:
- Summer League 2021

Sneki Snek is currently battling in:
- Global Arena

### Customised Battle Snake

Locate the `index` function inside [server.py](server.py#L15). At the end of that function you should see a line that looks like this:

```python
return {
    "apiversion": "1",
    "author": "",
    "color": "#888888",
    "head": "default",
    "tail": "default",
}
```

Sneki Sneki is red with a caffeine head and curly tail.

This function is called by the game engine periodically to make sure your Battlesnake is healthy, responding correctly, and to determine how your Battlesnake will appear on the game board. See [Battlesnake Personalization](https://docs.battlesnake.com/references/personalization) for how to customize your Battlesnake's appearance using these values.

Whenever you update these values, go to the page for your Battlesnake and select 'Refresh Metadata' from the option menu. This will update your Battlesnake to use your latest configuration and those changes should be reflected in the UI as well as any new games created.

### Changing Behavior

On every turn of each game your Battlesnake receives information about the game board and must decide its next move.

Locate the `move` function inside [server.py](server.py#L37). Possible moves are "up", "down", "left", or "right". To start your Battlesnake will choose a move randomly. Your goal as a developer is to read information sent to you about the board (available in the `data` variable) and decide where your Battlesnake should move next.

See the [Battlesnake Game Rules](https://docs.battlesnake.com/references/rules) for more information on playing the game, moving around the board, and improving your algorithm.

### Updating Your Battlesnake

After making changes to your Battlesnake, you can restart your Repl to have the change take effect (or in many cases your Repl will restart automatically).

Once the Repl has restarted you can [create a new game](https://play.battlesnake.com/account/games/create/) with your Battlesnake to watch your latest changes in action.

**At this point you should feel comfortable making changes to your code and starting new Battlesnake games to test those changes!**

## Developing Your Battlesnake Further

Now you have everything you need to start making your Battlesnake super smart!

### Early Development Goals

Here are some simple goals to help you develop your Battlesnake early on. Completing these will make your Battlesnake competitive against other Battlesnakes in multi-player games. Earn challenge medals for these:

- [x] Avoid colliding with walls
- [x] Avoid colliding with yourself
- [x] Try to move towards food
- [ ] Avoid colliding with other snakes

Once you have completed these steps you'll be ready to compete live against other Battlesnakes and start exploring and implementing more complex strategies.

### Helpful Tips

* Keeping your Repl open in a second window while games are running is helpful for watching server activity and debugging any problems with your Battlesnake.

* You can use the Python [print function](https://docs.python.org/3.8/library/functions.html#print) to output information to your server logs. This is very useful for debugging logic in your code during Battlesnake games.

* Review the [Battlesnake API Docs](https://docs.battlesnake.com/references/api) to learn what information is provided with each command.

* When viewing a Battlesnake game you can pause playback and step forward/backward one frame at a time. If you review your logs at the same time, you can see what decision your Battlesnake made on each turn.

## Joining a Battlesnake Arena

Once you've made your Battlesnake behave and survive on its own, you can enter it into the [Global Battlesnake Arena](https://play.battlesnake.com/arena/global) to see how it performs against other Battlesnakes worldwide.

Arenas will regularly create new games and rank Battlesnakes based on their results. They're a good way to get regular feedback on how well your Battlesnake is performing, and a fun way to track your progress as you develop your algorithm.

## TODO (Optional) Using a Cloud Provider

As your Battlesnake gets more complex, it might make sense to move it to a dedicated hosting provider such as Heroku or AWS. We suggest choosing a platform you're familiar with, or one you'd be interested in learning more about.

If you have questions or ideas, our developer community on [Slack](https://play.battlesnake.com/slack) and [Discord](https://play.battlesnake.com/discord) will be able to help out.


## (Optional) Running Your Battlesnake Locally

Can run Battlesnake locally, but I wouldn't trust Australian internet! :wink:

Eventually you might want to run your Battlesnake server locally for faster testing and debugging. You can do this by installing [Python 3.8](https://www.python.org/downloads/) and running:

```shell
python server.py
```

**Note:** You cannot create games on [play.battlesnake.com](https://play.battlesnake.com) using a locally running Battlesnake unless you install and use a port forwarding tool like [ngrok](https://ngrok.com/).


---

### Refer back to Battlesnake

All documentation is available at [docs.battlesnake.com](https://docs.battlesnake.com), including detailed Guides, API References, and Tips.

You can also join the Battlesnake Developer Community on [Slack](https://play.battlesnake.com/slack) and [Discord](https://play.battlesnake.com/discord). We have a growing community of Battlesnake developers of all skill levels wanting to help everyone succeed and have fun with Battlesnake :smile:

### Give Feedback to Battlesnake

* **Do you have an issue or suggestions for this repository?** Head over to our [Feedback Repository](https://play.battlesnake.com/feedback) today and let us know!
