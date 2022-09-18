import turtle

row = 5 # 가로 행
column = 5 # 세로 열

size = 100 # 정사각형 하나의 크기
angle = 360 # 한바퀴의 각도

i = 0; j = 0

while (i < row):

    j = 0

    while (j < column):

        turtle.penup()
        turtle.goto(i * size - 300, j * size - 300) # 사각형 그릴 출발지
        turtle.pendown()

         # 사각형을 그린다

        turtle.forward(size)
        turtle.left(angle/4)
        turtle.forward(size)
        turtle.left(angle/4)
        turtle.forward(size)
        turtle.left(angle/4)
        turtle.forward(size)
        turtle.left(angle/4)

        turtle.penup()

        j+=1 

    i+=1 
