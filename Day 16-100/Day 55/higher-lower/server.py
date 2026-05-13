from flask import Flask
import random

random_num = random.randint(0, 9)

print(f"The secret number is: {random_num}")

app = Flask(__name__)

@app.route("/")
def guess_number():
    return '<h1>Guess a number between 0 and 9</h1>'\
    '<img src="https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif" width =200>'

@app.route("/<int:number>")
def guess(number):
    if number < random_num:
        return '<h1 style="color: red;">Too low! Try a higher number.</h1>'\
               '<img src="https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif" width=200>'
    elif number > random_num:
        return '<h1 style="color: purple;">Too high! Try a lower number.</h1>'\
               '<img src="https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif" width=200>'
    else:
        return '<h1 style="color: green;">You found it! 🎉 The number was ' + str(random_num) + '!</h1>'\
               '<img src="https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif" width=200>'


if __name__ == "__main__":
    app.run(debug=True)