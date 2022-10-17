import game_framework
from pico2d import *

import random

import play_state

def enter():
    # fill here
    pass

def exit():
    # fill here
    pass

def update():
    # fill herek
    pass

def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()

        elif event.type == SDL_KEYDOWN:
            match event.key:
                case pico2d.SDLK_ESCAPE:
                    game_framework.pop_state()

                case pico2d.SDLK_j: # 소년 수 증가
                    play_state.nowboysnum += 1
                    play_state.boys = [play_state.Boy() for i in range(play_state.nowboysnum)]  # 소년들
                    play_state.boys[play_state.nowboysnum-1].spd = random.randint(50, 200)

                case pico2d.SDLK_k: # 소년 수 감소
                    if play_state.nowboysnum >= 2:
                        play_state.boys[play_state.nowboysnum-1] = None
                        play_state.nowboysnum -= 1

def draw_world():
    grass.draw()
    boys.draw()

def draw():
    clear_canvas()
    play_state.draw_world()
    image = load_image('add_delete_boy.png')
    image.draw(400, 300)
    update_canvas()

def pause():
    pass

def resume():
    pass

def test_self():
    import boyadddelete_state
    pico2d.open_canvas()
    game_framework.fill_states(play_state)
    game_framework.run(boyadddelete_state)
    pico2d.close_canvas()

if __name__ == '__main__':
    test_self()