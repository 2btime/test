from flask import Flask, render_template, request # 고정

app = Flask(__name__) # 고정, 인스턴스 생성

@app.route("/", methods=['GET', 'POST'])
@app.route("/post", methods=['GET', 'POST'])
def hello():
    if(request.method == 'GET'):
        return render_template('index.html')
    elif(request.method == 'POST'):
        value = request.form['name']
        return render_template('welcome.html', name=value)

if __name__ == '__main__': # 고정
    app.run(debug=True) # 고정