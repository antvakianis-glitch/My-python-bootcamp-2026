from flask import Flask

def make_bold(function):
    def wrapper():
        return f"<b>{function()}</b>"
    return wrapper

def emphasis(function):
    def wrapper():
        return f"<em>{function()}</em>"
    return wrapper

def make_underline(function):
    def wrapper():
        return f"<u>{function()}</u>"
    return wrapper

app = Flask(__name__)

@app.route("/")
def hello_world():
    return '<h1 style="text-align : center"> Hello, World!</h1> \
    <p> This is  my paragraph</p>'\
    '<img src="https://images.squarespace-cdn.com/content/v1/607f89e638219e13eee71b1e/1684821560422-SD5V37BAG28BURTLIXUQ/michael-sum-LEpfefQf4rU-unsplash.jpg" width =200>'

@app.route("/bye")
@make_bold
@emphasis
@make_underline
def bye():
    return "Bye"

@app.route("/username/<name>")
def greet(name):
    return f"(Hello {name})"

if __name__ == "__main__":
    app.run(debug=True)