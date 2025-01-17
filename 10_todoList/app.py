from flask import Flask, render_template, redirect, request, url_for
from flask_wtf import FlaskForm     # 폼 생성, 데이터 검증, CSRF 보호
from wtforms import StringField     # 주로 사용자로부터 텍스트 데이터를 입력받는 용도
from wtforms.validators import DataRequired
from pymongo import MongoClient
from bson import ObjectId      
# Binary JSON의 약자, MongoDB가 데이터를 저장하고 교환할 때 사용하는 포맷
# bson 모듈의 ObjectId는 MongoDB에서 사용되는 고유한 식별자를 생성하고 조작하는 데 사용되는 클래스
from datetime import datetime

# Config setting
app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret' # wtf 텍스트 필드를 위한 key 설정
connection = MongoClient('localhost', 27017)
db = connection.project     # 데이터베이스 project 생성
todos = db.todo         # todo 컬렉션 만듬

# 메모 입력을 위한 텍스트 필드 선언
class TextForm(FlaskForm):
    content = StringField('내용', validators=[DataRequired()])
# StringField() : 사용자로부터 텍스트 데이터를 입력받는 용도로 사용
# validators=[DataRequired()]로 메모가 존재하는지 검증한 후 content에 넣어준다

@app.route('/')
@app.route('/about')
def home():
    return render_template('about.html')

# 모든 목록 보기
@app.route('/all')
def all():
    stat = "All list"
    todolist = todos.find().sort('date', -1)       # 날짜 내림차순
    form = TextForm()
    return render_template('index.html', form=form, stat=stat, todolist=todolist)

@app.route('/action', methods=["GET", "POST"])
def action_add():
    form = TextForm()
    if form.validate_on_submit():
        contents = request.form['content']
        date = datetime.today()
        primary = request.values.get('primary')
        todos.insert_one({"contents":contents, "date":date, "primary":primary, "done":"no"})
        return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)