from flask import Flask, render_template
from random import sample

app = Flask(__name__)


@app.route('/')
def hello_world():
    return "여기는 메인페이지"


@app.route('/show')
def show():
    menu = ['짜장면.jpg', '짬뽕.jpg']
    pickme = ''.join(sample(menu, 1))
    return render_template('index2.html', food_img=pickme)


@app.route('/lunch/<int:num>')
def lunch(num):
    menu = ['짜장면', '치킨', '보쌈', '햄버거', '피자', '민트초코', '하와이안 피자', '스파게티', '닭칼국수', '한정식']
    return f'{sample(menu, num)}'


@app.route('/instagram')
def hello_hello():
    return render_template('index.html')


@app.route('/gugudan/<int:num>')
def gugu_dan(num):

    a = ""
    for i in range(1,10):
        a += f'{str(num)} * {str(i)} = {str(num * i)}'

    return a


if __name__ == "__main__":
    app.run(debug=1)
