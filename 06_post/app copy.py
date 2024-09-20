from flask import Flask, render_template, request # 고정

app = Flask(__name__) # 고정, 인스턴스 생성

@app.route("/")
def hello():
    return render_template('index.html')

# @app.route("/post", methods=['POST'])
# def post():
#     value = request.form['name']
#     msg = "%s님 환영합니다." %value
#     return msg

@app.route("/post", methods=['POST'])
def welcome():
    value = request.form['name']
    return render_template('welcome.html', name=value)

if __name__ == '__main__': # 고정
    app.run(debug=True) # 고정