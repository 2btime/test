from flask import Flask, render_template # 고정

app = Flask(__name__) # 고정, 인스턴스 생성

@app.route("/<username>")
def get_profile(username):
    length = len(username)
    return render_template('index.html', name=username, leng=length)


if __name__ == '__main__': # 고정
    app.run(debug=True) # 고정