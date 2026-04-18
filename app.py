from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def hello():
  return render_template("interpreter.html")

@app.route("/interpret/", methods=["POST"])
def interpret():
  code = request.json["code"]
  inp = request.json["input"]
  flag = request.json["flag"]
  return str([code, inp, flag])