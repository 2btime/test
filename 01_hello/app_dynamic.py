from flask import Flask # 고정
from flask import url_for
app = Flask(__name__) # 고정

@app.route("/")
def hello():
    return "<h1>hello Page : home</h1>"

@app.route("/profile/<username>")
def get_profile(username):
    return "username? : " + username

# 주소에 있는 데이터를 가져오기 위해서는 test_request_context함수가 필요함
if __name__ == '__main__': # 고정
    with app.test_request_context():
        print(url_for('get_profile', username='flask'))
        app.run(debug=True) # 고정