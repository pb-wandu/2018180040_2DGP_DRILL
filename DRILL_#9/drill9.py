import random

from pico2d import *

XSIZE = 800
YSIZE = 600

UNSET = -999 # 정해지지 않은 값

open_canvas(XSIZE, YSIZE)

tuk_ground = load_image('TUK_GROUND.png')
arrow = load_image('hand_arrow.png')
character = load_image('animation_sheet.png')


running = True # 실행중 여부
playerx = XSIZE / 2 # 플레이어 x좌표 위치
playery = YSIZE / 2 # 플레이어 y좌표 위치

startx = UNSET # 시작 x좌표 위치
starty = UNSET # 시작 y좌표 위치

playermovespd = 0.03 # 플레이어 이동속도

sx = 0
sy = 0
t = 0 # 시간에 따라 이동한 거리


arrowx = playerx # 화살표 x좌표 위치
arrowy = playery # 화살표 y좌표 위치
frame = 0 # 애니메이션 프레임
hide_cursor() # 마우스 숨기기

LEFT = 0 # x 이동방향
RIGHT = 1 # x 이동방향
LEFTSTOP = 2 # x 이동방향
RIGHTSTOP = 3 # x 이동방향

YSTOP = 0 # y 이동방향
UP = 1 # y 이동방향
DOWN = 2 # y 이동방향

characterdirx = RIGHT # 현재 x 이동방향



# 화살표 위치를 랜덤으로 지정하는 함수
def randarrowset():
    global arrowx, arrowy
    global t, sx, sy

    global startx, starty, playerx, playery

    # 플레이어 이동 시작위치
    startx, starty = playerx, playery

    # 이전 위치와 무조건 50픽셀 이상의 차이가 나게 하기
    tmpx, tmpy = arrowx, arrowy
    while arrowx - 50 < tmpx < arrowx + 50:
        tmpx = random.randint(0, XSIZE)
    while arrowy - 50 < tmpy < arrowy + 50:
        tmpy = random.randint(0, YSIZE)

    arrowx, arrowy = tmpx, tmpy

    t = 0
    sx, sy = playerx, playery

    pass

# 플레이어를 이동시키는 함수
def playermove():
    global playerx, playery
    global t, sx, sy

    t += playermovespd # 플레이어 이동속도만큼 증가

    # 화살표까지의 거리를 playermovespd로 나눠 그만큼 이동을 반복한다

    playerx = (1 - t) * sx + t * arrowx
    playery = (1 - t) * sy + t * arrowy

    # 만약 플레이어가 목적지에 도착하면 화살표 위치를 재지정한다
    if t >= 1.0:
        randarrowset()


# 이벤트 핸들러
def handle_events():

    global running # 실행중 여부
    global playerx, playery # 플레이어 좌표

    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False

        # 키보드 눌렀을 때
        elif event.type == SDL_KEYDOWN:

            # esc키 눌렸을 때
            if event.key == SDLK_ESCAPE:
                running = False
        # 마우스
        elif event.type == SDL_MOUSEMOTION:
            x, y = event.x, XSIZE - 1 - event.y
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False
    pass

# ------------ 실행 메인 코드 ------------

randarrowset() # 화살표 방향 임의로 지정

while running: # 실행중일 경우

    clear_canvas() # 화면 초기화

    playermove() # 플레이어 이동

    # 플레이어 현재 바라보는 위치
    if playerx >= arrowx:
        characterdirx = LEFT
    elif playerx < arrowx:
        characterdirx = RIGHT

    tuk_ground.draw(400, 300) # 배경 그리기
    character.clip_draw(frame * 100, characterdirx * 100, 100, 100, playerx, playery)  # 플레이어 그리기
    arrow.draw(arrowx, arrowy) # 화살표 그리기

    update_canvas() # 화면 업데이트

    handle_events() # 이벤트 핸들러

    frame = (frame + 1) % 8 # 프레임 표시

    # 애니메이션 보정 - x좌표 y좌표 떨어진 거리 합산하여 지연속도 변경
    delay(0.0001 * (abs(arrowx - startx) + abs(arrowy - starty)) ) # 프레임간 지연

close_canvas()
