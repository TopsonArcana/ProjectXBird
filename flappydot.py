import tkinter as tk

from gamelib import Sprite, GameApp, Text
from PIL import ImageTk
from PIL import Image
import random
CANVAS_WIDTH = 800
CANVAS_HEIGHT = 500

UPDATE_DELAY = 33
GRAVITY = 2.5

PILLAR_SPEED = 6
JUMP_VELOCITY = -20


class Dot(Sprite):
    def init_element(self):
        self.vy = 0
        self.is_started = False

    def init_canvas_object(self, angle=0):
        self.image = Image.open(self.image_filename)
        self.angle = angle
        self.tkimage = ImageTk.PhotoImage(self.image.rotate(self.angle))
        self.canvas_object_id = self.canvas.create_image(
            self.x,
            self.y,
            image=self.tkimage)

    def update(self):
        if self.is_started:
            self.y += self.vy
            self.vy += GRAVITY
            self.angle -= 5
            self.canvas.delete(self.canvas_object_id)
        self.canvas.delete(self.canvas_object_id)
        self.init_canvas_object(self.angle)

    def start(self):
        self.is_started = True

    def jump(self):
        self.vy = JUMP_VELOCITY
        self.angle = 15

    def is_out_of_screen(self):
        if self.y > CANVAS_HEIGHT:
            return True
        return False


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
        self.y = random.randrange(150, 350)


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
        if self.pillar_pair.is_out_of_screen():
            self.pillar_pair.random_height()
            self.pillar_pair.reset_position()
        if self.dot.is_out_of_screen():
            self.game_over()

    def on_key_pressed(self, event):
        if event.char == " ":
            self.dot.start()
            self.dot.jump()

    def game_over(self):
        self.dot.is_started = False
        self.dot.y = CANVAS_HEIGHT // 2


if __name__ == "__main__":
    root = tk.Tk()
    root.title("Flappy Dot Game")

    # do not allow window resizing
    root.resizable(False, False)
    app = FlappyGame(root, CANVAS_WIDTH, CANVAS_HEIGHT, UPDATE_DELAY)
    app.start()
    root.mainloop()
