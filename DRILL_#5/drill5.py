import turtle

movelength = 50 # 한 번에 이동하는 거리

nowmoving = 0

turtle.reset() # 화면 초기화
turtle.shape('turtle') # 거북이 모양을 'turtle'로 변경

turtle.stamp() # 현위치에 스탬프 찍기

# 이동 함수들 - nowmoving 변수는 이동중에 키를 입력받아 중간에 경로가 바뀌는 것을 막기 위한 변수입니다
# 이동 도중에는 키를 눌러도 움직이지 않는 것을 실행시 확인할 수 있습니다

def moveleft():
    global nowmoving
    
    if nowmoving == 0 :
        nowmoving = 1
        turtle.setheading(180)
        turtle.forward(movelength)
        turtle.stamp() # 현위치에 스탬프 찍기
        nowmoving = 0

def moveright():
    global nowmoving
    
    if nowmoving == 0 :
        nowmoving = 1
        turtle.setheading(0)
        turtle.forward(movelength)
        turtle.stamp() # 현위치에 스탬프 찍기
        nowmoving = 0

def moveup():
    global nowmoving
    
    if nowmoving == 0 :
        nowmoving = 1
        turtle.setheading(90)
        turtle.forward(movelength)
        turtle.stamp() # 현위치에 스탬프 찍기
        nowmoving = 0


def movedown():
    global nowmoving
    
    if nowmoving == 0 :
        nowmoving = 1
        turtle.setheading(270)
        turtle.forward(movelength)
        turtle.stamp() # 현위치에 스탬프 찍기
        nowmoving = 0


def restart():
    turtle.reset()

# 입력받아 실행

turtle.onkey(moveup, 'w')
turtle.onkey(moveleft, 'a')
turtle.onkey(movedown, 's')
turtle.onkey(moveright, 'd')

turtle.onkey(exit, 'Escape') # Esc 누르면 종료

turtle.onkey(restart, 'Tab') # Tab 누르면 재시작

turtle.listen()
