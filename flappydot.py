import tkinter as tk

from gamelib import Sprite, GameApp, Text

CANVAS_WIDTH = 800
CANVAS_HEIGHT = 500

UPDATE_DELAY = 33
GRAVITY = 2.5
JUMP_VELOCITY = -20
PILLAR_SPEED = 3


class Dot(Sprite):
    def init_element(self):
        self.is_started = False

    def update(self):
        if self.is_started:
            self.y += self.vy
            self.vy += GRAVITY

    def start(self):
        self.is_started = True

    def jump(self):
        self.vy = JUMP_VELOCITY

    def is_out_of_screen(self):
        if self.y > CANVAS_HEIGHT:
            return True
        return False

    def is_falling(self):
        if self.vy > 0:
            return True


class PillarPair(Sprite):
    def update(self):
        self.x -= PILLAR_SPEED


class FlappyGame(GameApp):
    def create_sprites(self):
        self.dot = Dot(self, 'images/dot.png',
                       CANVAS_WIDTH // 2, CANVAS_HEIGHT // 2)

        self.elements.append(self.dot)
        self.pillar_pair = PillarPair(
            self, 'images/pillar-pair.png', CANVAS_WIDTH, CANVAS_HEIGHT // 2)
        self.elements.append(self.pillar_pair)

    def init_game(self):
        self.create_sprites()
        self.is_started = False

    def pre_update(self):
        pass

    def post_update(self):
        if self.dot.is_out_of_screen():
            self.game_over()
        if self.dot.is_falling():
            self.fall()

    def on_key_pressed(self, event):
        self.dot.start()
        self.dot.jump()

    def game_over(self):
        self.dot.is_started = False
        self.dot.y = CANVAS_HEIGHT // 2

    def fall(self):
        pass


if __name__ == "__main__":
    root = tk.Tk()
    root.title("Flappy Dot Game")

    # do not allow window resizing
    root.resizable(False, False)
    app = FlappyGame(root, CANVAS_WIDTH, CANVAS_HEIGHT, UPDATE_DELAY)
    app.start()
    root.mainloop()
