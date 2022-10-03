from pico2d import *

XSIZE = 800
YSIZE = 600

open_canvas(XSIZE, YSIZE)

tuk_ground = load_image('TUK_GROUND.png')
# grass = load_image('grass.png')
character = load_image('animation_sheet.png')


running = True # 실행중 여부

playerx = 400 # 플레이어 x좌표 위치
playery = 90 # 플레이어 y좌표 위치

frame = 0 # 애니메이션 프레임

LEFT = 0 # x 이동방향
RIGHT = 1 # x 이동방향
LEFTSTOP = 2 # x 이동방향
RIGHTSTOP = 3 # x 이동방향

YSTOP = 0 # y 이동방향
UP = 1 # y 이동방향
DOWN = 2 # y 이동방향

keypressing = 0 # 키보드 누르고 있는 여부

characterdirx = RIGHTSTOP # 현재 x 이동방향
characterdiry = YSTOP # 현재 y 이동방향

# 키 입력된 여부
keypressedleft = 0
keypressedright = 0
keypressedup = 0
keypresseddown = 0

def handle_events():

    ### global을 빼면 함수 내의 지역변수로 선언된다

    global running # 실행중 여부
    global playerx, playery # 플레이어 좌표

    global characterdirx # 현재 x 이동방향
    global characterdiry # 현재 y 이동방향

    global frame # 애니메이션 프레임

    global keypressing # 키보드 입력중 여부

    global keypressedleft # 키 입력된 여부
    global keypressedright  # 키 입력된 여부
    global keypressedup  # 키 입력된 여부
    global keypresseddown  # 키 입력된 여부

    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False

        # 키보드 눌렀을 때
        elif event.type == SDL_KEYDOWN:

            keypressing = 1

            if event.key == SDLK_LEFT:
                keypressedleft = 1

            elif event.key == SDLK_RIGHT:
                keypressedright = 1

            elif event.key == SDLK_UP:
                keypressedup = 1

            elif event.key == SDLK_DOWN:
                keypresseddown = 1

            # esc키 눌렸을 때
            elif event.key == SDLK_ESCAPE:
                running = False

        # 키보드 뗐을 때
        elif event.type == SDL_KEYUP:

            keypressing = 0

            if event.key == SDLK_LEFT:
                keypressedleft = 0;

            elif event.key == SDLK_RIGHT:
                keypressedright = 0;

            elif event.key == SDLK_UP:
                keypressedup = 0;

            elif event.key == SDLK_DOWN:
                keypresseddown = 0;
    pass


while running: # 실행중일 경우

    clear_canvas() # 화면 초기화

    tuk_ground.draw(400, 300) # 그리는 중심 좌표
    # grass.draw(400, 30) # 그리는 중심 좌표

    # 플레이어 그리기
    character.clip_draw(frame * 100, characterdirx * 100, 100, 100, playerx, playery)
    update_canvas()

    handle_events() # 이벤트 핸들러

    frame = (frame + 1) % 8 # 프레임 표시
    delay(0.035) # 프레임간 지연

    # 현재 눌린 방향에 따라 이동 및 방향 지정
    if keypressedleft == 1:
        characterdirx = LEFT  # 캐릭터 방향
        playerx -= 10
    elif keypressedright == 1:
        characterdirx = RIGHT  # 캐릭터 방향
        playerx += 10
    if keypressedup == 1:
        characterdiry = UP  # 캐릭터 방향
        playery += 10
    elif keypresseddown == 1:
        characterdiry = DOWN  # 캐릭터 방향
        playery -= 10

    # 플레이어 위치 넘어가지 않게 하기
    if playerx < 25:
        playerx = 25
    elif playerx > XSIZE - 25:
        playerx = XSIZE - 25
    if playery < 25:
        playery = 25
    elif playery > YSIZE - 25:
        playery = YSIZE - 25

    # 키보드를 누르고 있지 않을 경우 정지동작으로 표시
    if keypressing == 0:

        # 현재 0프레임일 경우 플레이어 이동동작 -> 정지동작
        if frame == 0:
            if characterdirx == LEFT:
                characterdirx = LEFTSTOP
            elif characterdirx == RIGHT:
                characterdirx = RIGHTSTOP

        # Y축 이동중 -> 정지 상태
        if characterdiry == UP or characterdiry == DOWN:
            characterdiry = YSTOP

close_canvas()
