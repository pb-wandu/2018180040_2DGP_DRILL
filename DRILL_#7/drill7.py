from pico2d import *

open_canvas() # 캔버스 열기

character = load_image('greenclothesnotzelda.png')
# 초록옷 입은 사람은 젤다가 아닙니다

y = 0 # 시작 y축 위치
frame = 0 # 현재 프레임
rooped = 0 # 현재 루프 돈 횟수

yline = 1 # 현재 진행중인 세로줄
spnum = 0 # 그 줄의 스프라이트 개수

# 8번째 줄까지 스프라이트를 읽어와 애니메이션 출력
for yline in range(9):

    if yline == 6: yline = 7 # 리소스가 하나뿐인 줄 넘기기

    # 각 줄의 스프라이트 개수
    if yline == 1: spnum = 10
    elif yline == 2: spnum = 10
    elif yline == 3: spnum = 10
    elif yline == 4: spnum = 10
    elif yline == 5: spnum = 3
    # elif yline == 6: spnum = 1 # 애니메이션의 의미가 없는 줄이므로 생략
    elif yline == 7: spnum = 3
    elif yline == 8: spnum = 3

    frame = 0
    rooped = 0

    # 각 애니메이션당 3번 재생
    while rooped < 3:

        # 1바퀴를 다 돌았을 경우
        if frame == spnum:
            frame = 0
            rooped += 1

        # 남은 동작이 있을 경우
        else:
            clear_canvas()
            character.clip_draw(frame * 87, (yline-1) * 94, 80, 92, 400, 300)
            update_canvas()

            # 다음 프레임으로
            frame += 1

            # 동작 대기
            delay(0.07)

close_canvas()  # 캔버스 닫기



