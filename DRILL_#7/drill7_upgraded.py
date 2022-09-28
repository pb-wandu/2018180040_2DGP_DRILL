from pico2d import *

open_canvas() # 캔버스 열기

character = load_image('penguin.png')
infoimage = load_image('character.png') # 현재 몇 번째 애니메이션인지 표시용

### 아래 charater 이미지가 깜박이는 오류가 있습니다. 추후 수정 예정

y = 0 # 시작 y축 위치
frame = 0 # 현재 프레임
rooped = 0 # 현재 루프 돈 횟수

yline = 1 # 현재 진행중인 가로줄
spnum = 0 # 그 줄의 애니메이션 스프라이트 개수
spnum2 = 0 # 그 줄의 2번째 애니메이션 스프라이트 개수

xline = 0 # 한 가로줄에서 애니메이션이 다를 경우 구분

nowmotionnum = 0 # 현재 진행중인 동작의 번호 구분

delaytime = 0.1 # 스프라이트 사이의 지연시간

# 15번째 줄까지 스프라이트를 읽어와 애니메이션 출력
for yline in range(16):

    # 각 줄의 스프라이트 개수
    if yline == 1:
        spnum = 16; spnum2 = 0
    elif yline == 2:
        spnum = 12; spnum2 = 0
    elif yline == 3:
        spnum = 12; spnum2 = 0
    elif yline == 4:
        spnum = 12; spnum2 = 0
    elif yline == 5:
        spnum = 11; spnum2 = 0
    elif yline == 6:
        spnum = 6; spnum2 = 6
    elif yline == 7:
        spnum = 6; spnum2 = 6
    elif yline == 8:
        spnum = 10; spnum2 = 5
    elif yline == 9:
        spnum = 15; spnum2 = 0
    elif yline == 10:
        spnum = 12; spnum2 = 4
    elif yline == 11:
        spnum = 16; spnum2 = 0
    elif yline == 12: # 5~10번째 Sprite
        spnum = 6; spnum2 = 0
    elif yline == 13:
        spnum = 16; spnum2 = 0
    elif yline == 14:
        spnum = 12; spnum2 = 0
    elif yline == 15:
        spnum = 8; spnum2 = 0

    frame = 0
    rooped = 0

    # 각 애니메이션당 2번 재생
    while rooped < 2:

        # 1바퀴를 다 돌았을 경우
        if frame == spnum:
            frame = 0
            rooped += 1

        # 남은 동작이 있을 경우
        else:
            clear_canvas()

            # 12번째 줄은 애니메이션에 해당하는 5~10번째 Sprite만을 재생한다
            if yline == 12:
                character.clip_draw(128 * 4 + frame * 128, 1920 - (yline - 1) * 128, 128, 128, 400, 300)
            else:
                character.clip_draw(frame * 128, 1920 - (yline - 1) * 128, 128, 128, 400, 300)

            # 현재 몇 번째 동작인지 캐릭터로 표시하기
            for n in range(nowmotionnum):
                infoimage.draw_now(10 + n * 25, 10)
            update_canvas()

            # 다음 프레임으로
            frame += 1

            # 동작 대기
            delay(delaytime)

        # 4바퀴를 다 돌았을 경우
        if rooped == 2:
            nowmotionnum += 1  # 다음 동작으로 넘어가기

    rooped = 0

    # 현재 줄에 2번째 애니메이션 Sprite가 있을 경우
    if spnum2 != 0:

        if yline == 10:
            frame = spnum + 1
        else:
            frame = spnum

        # 각 애니메이션당 2번 재생
        while rooped < 2:

            # 1바퀴를 다 돌았을 경우
            if frame == spnum + spnum2:
                if yline == 10:
                    frame = spnum + 1
                else:
                    frame = spnum
                rooped += 1

            # 남은 동작이 있을 경우
            else:
                clear_canvas()

                # 12번째 줄은 애니메이션에 해당하는 5~10번째 Sprite만을 재생한다
                if yline == 12:
                    character.clip_draw(128 * 4 + frame * 128, 1920 - (yline - 1) * 128, 128, 128, 400, 300)
                else:
                    character.clip_draw(frame * 128, 1920 - (yline - 1) * 128, 128, 128, 400, 300)

                # 현재 몇 번째 동작인지 캐릭터로 표시하기
                for n in range(nowmotionnum):
                    infoimage.draw_now(10 + n * 25, 10)
                update_canvas()

                # 다음 프레임으로
                frame += 1

                # 동작 대기
                delay(delaytime)

            # 4바퀴를 다 돌았을 경우
            if rooped == 2:
                nowmotionnum += 1  # 다음 동작으로 넘어가기

    rooped = 0

close_canvas()  # 캔버스 닫기



