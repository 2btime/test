from flask import Flask, redirect, render_template, url_for, request

app = Flask(__name__)

@app.errorhandler(404)
def page_not_found(error):
    app.logger.error('Page not found!') # 콘솔에 메시지 남기기
    return render_template('page_not_found.html', error=error), 404

@app.route('/')
def test():
    return '<h1>test</h1>'

if __name__ == "__main__":
    app.run(debug=True)
