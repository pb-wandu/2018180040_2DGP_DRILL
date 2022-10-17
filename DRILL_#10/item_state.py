import game_framework
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
                    for play_state.boy in play_state.boys:
                        # 소년이 존재할 때
                        if play_state.boy is not None:
                            play_state.boy.item = None
                    game_framework.pop_state()

                case pico2d.SDLK_1:
                    for play_state.boy in play_state.boys:
                        # 소년이 존재할 때
                        if play_state.boy is not None:
                            play_state.boy.item = 'Ball'
                    game_framework.pop_state()

                case pico2d.SDLK_2:
                    for play_state.boy in play_state.boys:
                        # 소년이 존재할 때
                        if play_state.boy is not None:
                            play_state.boy.item = 'BigBall'
                    game_framework.pop_state()

def draw():
    clear_canvas()
    play_state.draw_world()
    image = load_image('item_select.png')
    image.draw(400, 300)
    update_canvas()

def pause():
    pass

def resume():
    pass

def test_self():
    import item_state
    pico2d.open_canvas()
    game_framework.fill_states(play_state)
    game_framework.run(item_state)
    pico2d.close_canvas()

if __name__ == '__main__':
    test_self()