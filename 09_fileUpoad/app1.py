from flask import Flask, redirect, render_template, url_for, request
from werkzeug.utils import secure_filename
import os
from pathlib import Path # 한글 파일 이름을 인코딩하기 위해 사용

app = Flask(__name__)

@app.route('/')
def upload():
    return render_template('upload.html')

@app.route("/fileUpoad", methods=['GET', 'POST'])
def upload_file():
    if not os.path.exists('upload'):
        os.makedirs('upload')
    if request.method == 'POST':
        f = request.files['file']
        if f:
            # 파일이름이 한글인 경우 secure_filename()는 처리하지 못한다
            filename = f.filename
            # 파일 저장 경로 설정
            file_path = Path('./upload/') / filename
            f.save(file_path)
            return render_template('check.html')
        else:
            return redirect(url_for('upload')) # 함수 호출
    else:
        return "Not"

if __name__ == "__main__":
    # 서버 실행
    app.run(debug=True)