from flask import Flask, render_template

app = Flask(__name__)

all_projects = [
    {
        "title": "Text-to-Morse Code Converter",
        "description": "A command-line Python application that converts plain text into Morse code signals.",
        "technologies": ["Python", "CLI"],
        "image": "morse.jpg",
        "github_url": "https://github.com/antvakianis-glitch/My-python-bootcamp-2026/tree/master/Day%2016-100/Day%2082/Text%20to%20Morse%20Converter"
    },
    {
        "title": "Antonio's Blog",
        "description": "A full-stack Flask blog application featuring user registration, authentication, SQLAlchemy database relations, and comment functionality.",
        "technologies": ["Python", "Flask", "SQLite", "SQLAlchemy", "WTForms", "Bootstrap"],
        "image": "blog.jpg",
        "github_url": "https://github.com/antvakianis-glitch/My-python-bootcamp-2026/tree/master/Day%2016-100/Day%2070/Deploying%20Web%20Application"
    }
]

@app.route('/')
def home():
    return render_template('index.html', projects=all_projects)

if __name__ == '__main__':
    app.run(debug=False, port=5000)