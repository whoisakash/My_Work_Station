from flask import Flask

# Hello,World website
app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello,World!</p>"

app.run(debug=True)