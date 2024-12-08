from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.py")

app.run(debug=True)
