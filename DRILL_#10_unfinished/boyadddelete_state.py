from pico2d import *

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

def draw_world():
    grass.draw()
    boy.draw()

def draw():
    clear_canvas()
    draw_world()
    update_canvas()

def pause():
    pass

def resume():
    pass
