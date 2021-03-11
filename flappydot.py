import tkinter as tk

from gamelib import Sprite, GameApp, Text
import random
CANVAS_WIDTH = 800
CANVAS_HEIGHT = 500

UPDATE_DELAY = 33
GRAVITY = 2.5
PILLAR_SPEED = 6


class Dot(Sprite):
    pass


class PillarPair(Sprite):
    def update(self):
        self.x -= PILLAR_SPEED

    def is_out_of_screen(self):
        if self.x < -30:
            return True
        return False

    def reset_position(self):
        self.x = CANVAS_WIDTH + 30

    def random_height(self):
        self.y = random.randrange(150,350)


class FlappyGame(GameApp):
    def create_sprites(self):
        self.dot = Dot(self, 'images/dot.png', CANVAS_WIDTH // 2, CANVAS_HEIGHT // 2)
        self.elements.append(self.dot)
        self.pillar_pair = PillarPair(self, 'images/pillar-pair.png', CANVAS_WIDTH, CANVAS_HEIGHT // 2)
        self.elements.append(self.pillar_pair)

    def init_game(self):
        self.create_sprites()

    def pre_update(self):
        pass

    def post_update(self):
        if self.pillar_pair.is_out_of_screen():
            self.pillar_pair.random_height()
            self.pillar_pair.reset_position()

    def on_key_pressed(self, event):
        pass


if __name__ == "__main__":
    root = tk.Tk()
    root.title("Monkey Banana Game")

    # do not allow window resizing
    root.resizable(False, False)
    app = FlappyGame(root, CANVAS_WIDTH, CANVAS_HEIGHT, UPDATE_DELAY)
    app.start()
    root.mainloop()
