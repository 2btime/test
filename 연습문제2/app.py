from flask import Flask, redirect, render_template, url_for, request

app = Flask(__name__)

@app.route('/')
@app.route('/<int:num>')
def inputTest(num=None, error=None):
    return render_template('index.html', num=num, error=error)

@app.route("/gugudan", methods=["POST"])
def gugudan():
    # 사용자가 입력한 값을 받아오기
    temp = request.form.get('num', '').strip()  # 입력값이 없을 때 빈 문자열로 처리
    
    if not temp:
        # 입력값이 없는 경우
        return redirect(url_for('inputTest', error='숫자를 입력해주세요.'))
    
    try:
        num = int(temp)
    except ValueError:
        # 숫자로 변환할 수 없는 경우
        return redirect(url_for('inputTest', error='유효한 숫자를 입력해주세요.'))
    
    return redirect(url_for('inputTest', num=num))

if __name__ == "__main__":
    app.run(debug=True)
