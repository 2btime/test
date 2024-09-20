from flask import Flask, request # 고정

app = Flask(__name__) # 고정

@app.route('/')
def user_juso():
    temp = request.args.get('name','홍길동')
    temp1 = request.args.get('juso','성남시')
    return temp + " : " + temp1 

# http://127.0.0.1:5000/?name=정다룡&juso=분당

if __name__ == '__main__': # 고정
    app.run(debug=True) # 고정