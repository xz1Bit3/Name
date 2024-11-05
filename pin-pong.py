
import arcade

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = 'PONG_GAME'

class Ball(arcade.Sprite):
    def __init__(self):
        super().__init__('ball6.png',0.10)
        self.change_x = 3
        self.change_y = 3

    def update(self):
        self.center_x += self.change_x
        self.center_y += self.change_y
        if self.right >= SCREEN_WIDTH:
            self.change_x = -self.change_x
        if self.left <= 0:
            self.change_x = -self.change_x
        if self.top >= SCREEN_HEIGHT:
            self.change_y = -self.change_y
        if self.bottom <=0:
            self.change_y = -self.change_y


class Rak(arcade.Sprite):
    def __init__(self):
        super().__init__('rak2.png',0.5)

    def update(self):
        self.center_x += self.change_x
        if self.right >= SCREEN_WIDTH:
            self.right = SCREEN_WIDTH
        if self.left <=0:
            self.left = 0


class Game(arcade.Window):
    def __init__(self,width, height, title):
        super().__init__(width, height, title)
        self.rak = Rak()
        self.ball = Ball()
        self.setap()


    def setap(self):
        self.rak.center_x = SCREEN_WIDTH /2
        self.rak.center_y = SCREEN_HEIGHT /5
        self.ball.center_x = SCREEN_WIDTH /2
        self.ball.center_y = SCREEN_HEIGHT /2


    def on_draw(self):
        self.clear((255,255,255))
        self.rak.draw()
        self.ball.draw()


    def update(self, delta):
        if arcade.check_for_collision(self.rak, self.ball):
            self.ball.change_y = -self.ball.change_y
        self.ball.update()
        self.rak.update()

    def on_key_press(self, key, modifiers):
        if key ==arcade.key.RIGHT:
            self.rak.change_x = 5
        if key ==arcade.key.LEFT:
            self.rak.change_x = -5

    def on_key_release(self, key, modifiers):
        if key == arcade.key.RIGHT or key == arcade.key.LEFT:
            self.rak.change_x = 0


if __name__ == '__main__':
    window = Game(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    arcade.run()