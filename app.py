from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello_world():
  return "<p>Hello, World!</p>"

@app.route("/api/pizza")
def pizza_api():
  return {
    "location": "Cici's",
    "size": "Giant",
    "toppings": "Mac & Cheese",
  }

