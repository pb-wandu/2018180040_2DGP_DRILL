from pico2d import *

import play_state

def enter():
    # fill here
    pass

def exit():
    # fill here
    pass

def update():
    # fill here
    pass

def draw():
    # fill here
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

                case pico2d.SDLK_0:
                    play_state.boy.item = None
                    game_framework.pop_state()

                case pico2d.SDLK_1:
                    play_state.boy.item = 'Ball'
                    game_framework.pop_state()

                case pico2d.SDLK_2:
                    play_state.boy.item = 'BigBall'
                    game_framework.pop_state()

def draw_world():
    grass.draw()
    boy.draw()

def draw():
    clear_canvas()
    play_state.draw_world()
    image.draw(400, 300)
    update_canvas()


def pause():
    pass

def resume():
    pass
