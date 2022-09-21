from pico2d import *

import math # 삼각함

# open_canvas() 로 열고 close_canvas()로 캔버스 닫기
# img = load_image('name.png') : 이미지를 불러와 img에 저장한다
# img.draw_now(x, y) : x, y 좌표에 이미지를 그린다
# clear_canvas_now() : 캔버스를 지운다
# delay(t) : t초동안 대기한다

# ----------- 코드 -----------

open_canvas() # 캔버스 열기

grass = load_image('grass.png')
character = load_image('character.png')

startx = 400 # 출발 x지점
starty = 90 # 출발 y지점

x = 400 # x지점
y = 90 # y지점

nowstat = 'movesquare' # 현재 이동상황
nowstat_sq = 'right' # 현재 이동상황 (사각형)

ticktime = 0.04 # 캔버스가 다시 그려지는 간격 (초 단위)

sqentered = 0 # 사각형 이동 진입여부
circleentered = 0 # 원 이동 진입여부

while(1):
    
    clear_canvas_now() # 그리기 전에 캔버스를 지우고 그려야 한다

    # 현재 플레이어 이동상황 확인

    # 사각형 이동
    if nowstat == 'movesquare' :
        
        if nowstat_sq == 'right' :
            x += 50
            if x == 700 :
                nowstat_sq = 'up'
            
        elif nowstat_sq == 'up' :
            y += 50
            if y == 490 :
                nowstat_sq = 'left'

        elif nowstat_sq == 'left' :
            x -= 50
            if x == 100 :
                nowstat_sq = 'down'
            
        elif nowstat_sq == 'down' :
            y -= 50
            if y == 90 :
                nowstat_sq = 'right'

        if x == startx and y == starty :
            # 출발지로 돌아왔다면 '원 이동'으로 전환한다
            nowstat = 'movecircle'
            circleentered = 1

    # 원 이동
    if nowstat == 'movecircle' :

        # 원 이동에 처음 진입시
        if circleentered == 1 :
            circleentered = 0
            nowdir = 0 # 현재 각도

        # y는 출발 y좌표에서 원 이동이 출발하도록 수정하였습니다
        x = startx + 200 * math.sin((360+nowdir)%360 / 360 * 2 * math.pi)
        y = (starty + 200) + 200 * math.cos((180+nowdir)%360 / 360 * 2 * math.pi)

        nowdir += 30

        if nowdir > 360 : # 한 바퀴 다 돌았을 경우 '사각형 이동'으로 전환한다
            nowstat = 'movesquare'

    # 이미지 그리기
    
    grass.draw_now(400, 30) # 풀밭은 고정
    
    character.draw_now(x, y) # x, y 위치에 캐릭터 표시
 
    delay(ticktime)  # ticktime만큼 이동 지연


#close_canvas() # 캔버스 닫기












