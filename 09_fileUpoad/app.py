from flask import Flask, render_template, request, send_file, redirect
from werkzeug.utils import secure_filename
from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired
import os
import datetime
import time

app = Flask(__name__)
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024     # 파일 업로드 용량 제한 단위 : 바이트
app.config['SECRET_KEY'] = "secret"     # app.config를 통해서 'SECRET_KEY'환경변수에 "secret"데이터를 넣어서 환경변수 등록

# 현재 작업 디렉토리 출력
print("Current working directory:", os.getcwd())

# 업로드 폴더가 존재(exists)하지 않으면 생성
if not os.path.exists('uploads'):
  os.makedirs('uploads')

# 파일 검증을 한 후 기본 폼 등록
class FileForm(FlaskForm):
  files = FileField(validators=[FileRequired('업로드할 파일을 넣어주세요')])

def steam2real(stamp):
  return datetime.datetime.fromtimestamp(stamp)

def info(filename):
  ctime = os.path.getctime(filename)    # 만든시간
  mtime = os.path.getmtime(filename)    # 수정시간
  # atime = os.path.getatime(filename)    # 마지막 엑세스 시간
  size = os.path.getsize(filename)      # 파일크기(단위 : bytes)
  return ctime, mtime, size

# HTML 렌더링
@app.route("/", methods=['GET', 'POST'])
def upload_page():
  form = FileForm()
  if form.validate_on_submit():
    f = form.files.data
    # f.save('./uploads/' + secure_filename(f.filename))
    # 한글 파일명을 처리하고, 저장할 때 사용
    f.save('./uploads/' + (f.filename))
    return render_template('check.html', pwd = os.getcwd() + "/uploads")
  filelist = os.listdir('./uploads')
  infos = []
  for name in filelist :
    fileinfo = {}
    ctime, mtime, size = info('./uploads/' + name)
    fileinfo['name'] = name
    fileinfo["create"] = steam2real(ctime)
    fileinfo["modify"] = steam2real(mtime)
    # fileinfo["access"] = steam2real(atime)
    # fileinfo["size"] = steam2real(size)
    if(size <= 1000000):
      fileinfo["size"] = "%.2f KB" %(size / 1024)
    else: 
      fileinfo["size"] = "%.2f MB" %(size / (1024*1024))
    infos.append(fileinfo)
  return render_template('upload.html', form=form, pwd = os.getcwd() + "/uploads", infos=infos)

@app.route('/down/<path:filename>')
def down_page(filename):
  return send_file('uploads/'+filename, download_name=filename, as_attachment=True)
# download_name : 어떤 이름으로 다운로드 받을 것인지 여기에서는 파일이름 그대로
# as_attachment=True : 파일을 브라우저에서 열지 않고 다운로드 하도록 한다. 

@app.route('/del/<path:filename>')
def delete_page(filename):
  os.remove('uploads/' + filename)
  return redirect('/')

@app.errorhandler(404)
def page_not_found(error):
  return render_template('deny.html', pwd=os.getcwd() + "/uploads"), 404

if __name__ == "__main__" :
  # 서버 실행
  app.run(debug=True)