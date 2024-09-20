# 데코레이터 사용하기

def check(func):
    def wrapper(): # 호출할 함수를 감싸는 함수
        print(func.__name__, '함수시작') # __name__으로 함수 이름 출력 의미 (함수이름, '함수시작')
        func() # 매개변수로 받은 함수를 호출
        print(func.__name__, '함수 끝')
    return wrapper

@check
def hello():
    print('hello1')

@check
def world():
    print('world1')

hello()

world()