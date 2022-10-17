import game_framework
from pico2d import *

import random

import title_state
import item_state
import boyadddelete_state

boys = None
grass = None
running = None
nowboysnum = 1

class Boy:
    def __init__(self):
        self.x, self.y = 0, 90
        self.frame = 0
        self.image = load_image('run_animation.png')
        self.ball_image = load_image('ball21x21.png')
        self.big_ball_image = load_image('ball41x41.png')
        self.item = None
        self.spd = random.randint(50, 200)

    def update(self):
        self.frame = (self.frame + 1) % 8
        self.x += self.spd/100
        if self.x >= 800:
            self.x -= 800

    def draw(self):
        self.image.clip_draw(self.frame * 100, 0, 100, 100, self.x, self.y)
        if self.item == 'BigBall':
            self.big_ball_image.draw(self.x + 40, self.y - 13)
        elif self.item == 'Ball':
            self.ball_image.draw(self.x + 30, self.y - 27)

class Grass:

    def __init__(self):
        self.image = load_image('grass.png')

    def draw(self):
        self.image.draw(400, 30)

# 초기화
def enter():
    global boy, boys, grass, running, nowboysnum
    grass = Grass()

    nowboysnum = 1  # 현재 소년 명수
    boys = [Boy() for i in range(nowboysnum)]  # 소년들

    running = True

# 종료
def exit():
    global boys, grass
    del boys
    del grass
    pass

def update():
    for boy in boys:
        # 소년이 존재할 때
        if boy is not None:
            boy.update()
    pass

def draw_world():
    grass.draw()
    for boy in boys:
        # 소년이 존재할 때
        if boy is not None:
             boy.draw()

def draw():
    clear_canvas()
    draw_world()
    update_canvas()


def handle_events():
    events = get_events()

    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_ESCAPE:
                game_framework.change_state(title_state)
            elif event.key == SDLK_i:
                game_framework.push_state(item_state)
            elif event.key == SDLK_b:
                game_framework.push_state(boyadddelete_state)

def test_self():
    import play_state
    pico2d.open_canvas()
    game_framework.fill_states(play_state)
    game_framework.run(play_state)
    pico2d.close_canvas()

    if __name__ == '__main__':
        test_self()

def pause():
    pass

def resume():
    pass

'''


boy = None
grass = None
running = None



# 초기화
def enter():
    global boy, grass, running
    # boy = Boy()
    # grass = Grass()
    running = True

def update():
    # boy.update()
    pass

def draw_world():
    # grass.draw()
    # boy.draw()
    pass

def draw():
    clear_canvas()
    draw_world()
    update_canvas()


def enter():
    pass






# 종료
def exit():
    global boy, grass
    del boy
    del grass
    pass
'''