"""Greeting Flask app."""

from random import choice

from flask import Flask, request

# "__name__" is a special Python variable for the name of the current module
# Flask wants to know this to know what any imported things are relative to.
app = Flask(__name__)

AWESOMENESS = [
    'awesome', 'terrific', 'fantastic', 'neato', 'fantabulous', 'wowza',
    'oh-so-not-meh', 'brilliant', 'ducky', 'coolio', 'incredible',
    'wonderful', 'smashing', 'lovely']

INSULTS = [
    'a poopyhead', 'a bozo', 'a jerk', 'a cow', 'a butthead', 'a runnynose',
    'a babyfoot', 'a weirdo', 'a nasty fellow', 'an idiot', 'stupid',
    'a dumbhead', 'a four-eyes', 'a worm']


@app.route("/")
def start_here():
    """Home page."""

    return """
    <!doctype html>
    <html>
      <body>
        <a href="http://localhost:5000/hello">Hi!</a> This is the home page.
      </body>
    </html>
    """


@app.route("/hello")
def say_hello():
    """Say hello and prompt for user's name."""

    return """
    <!doctype html>
    <html>
      <head>
        <title>Hi There!</title>
      </head>
      <body>
        <h1>Hi There!</h1>
        <form action="/diss">
          What's your name? <input type="text" name="person">
          <input type="submit" value="Submit">
        </form>
      </body>
    </html>
    """


@app.route("/greet")
def greet_person():
    """Get user by name."""

    player = request.args.get("person")

    compliment = choice(AWESOMENESS)

    return """
    <!doctype html>
    <html>
      <head>
        <title>A Compliment</title>
      </head>
      <body>
        Hi, {}! I think you're {}!
      </body>
    </html>
    """.format(player, compliment)


@app.route("/diss")
def insult_person():
    """Insult user by name."""

    player = request.args.get("person")

    insult = choice(INSULTS)

    return """
    <!doctype html>
    <html>
      <head>
        <title>A Insult</title>
      </head>
      <body>
        Hi, {}! I think you are {}!
      </body>
    </html>
    """.format(player, insult)


@app.route("/allthewords")
def generate_HTML():
    """Generates a string of valid HTML from constant."""

    return """
    <!doctype html>
    <html>
      <body>{}</body>
    </html>
    """.format(INSULTS)


if __name__ == "__main__":
    # debug=True gives us error messages in the browser and also "reloads"
    # our web app if we change the code.
    app.run(debug=True, host="0.0.0.0")
