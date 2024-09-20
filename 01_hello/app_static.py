from flask import Flask # 고정
app = Flask(__name__) # 고정

@app.route("/")
def home():
    return "<h1>Hello world : home<h1>"

@app.route("/hello")
def hello():
    return "<h1>Hello world : hello2<h1>"

if __name__ == '__main__': # 고정
    app.run(debug=True) # 고정