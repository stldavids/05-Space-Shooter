import sys, logging, os, random, math, arcade

#check to make sure we are running the right version of Python
version = (3,7)
assert sys.version_info >= version, "This script requires at least Python {0}.{1}".format(version[0],version[1])

#turn on logging, in case we have to leave ourselves debugging messages
logging.basicConfig(format='[%(filename)s:%(lineno)d] %(message)s', level=logging.DEBUG)
logger = logging.getLogger(__name__)

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
MARGIN = 30
SCREEN_TITLE = "Bullet exercise"

NUM_ENEMIES = 5
STARTING_LOCATION = (400,100)
BULLET_DAMAGE = 10
ENEMY_HP = 100
HIT_SCORE = 10
KILL_SCORE = 100
ENEMY_SPEED = 5

class Bullet(arcade.Sprite):
    def __init__(self, position, velocity, damage):
        ''' 
        initializes the bullet
        Parameters: position: (x,y) tuple
            velocity: (dx, dy) tuple
            damage: int (or float)
        '''
        super().__init__("assets/PNG/Lasers/laserGreen07.png", 0.5)
        (self.center_x, self.center_y) = position
        (self.dx, self.dy) = velocity
        self.damage = damage

    def update(self):
        '''
        Moves the bullet
        '''
        self.center_x += self.dx
        self.center_y += self.dy


    
class Player(arcade.Sprite):
    def __init__(self):
        super().__init__("assets/PNG/playerShip2_blue.png", 0.5)
        (self.center_x, self.center_y) = STARTING_LOCATION

class Enemy(arcade.Sprite):
    def __init__(self, position):
        '''
        initializes a penguin enemy
        Parameter: position: (x,y) tuple
        '''
        super().__init__("assets/PNG/shipBeige_manned.png", 0.5)
        self.hp = ENEMY_HP
        (self.center_x, self.center_y) = position



        


class Window(arcade.Window):

    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        file_path = os.path.dirname(os.path.abspath(__file__))
        os.chdir(file_path)

        self.set_mouse_visible(True)
        arcade.set_background_color(arcade.color.PURPLE_NAVY)
        self.bullet_list = arcade.SpriteList()
        self.enemy_list = arcade.SpriteList()
        self.player = Player()
        self.score = 0

    def setup(self):
        '''
        Set up enemies
        '''
        for i in range(NUM_ENEMIES):
            x = 120 * (i+1) + 40
            y = 500
            enemy = Enemy((x,y))
            self.enemy_list.append(enemy)            

    def update(self, delta_time):
        self.bullet_list.update()
        for e in self.enemy_list:
            for b in self.bullet_list:
                collisions = e.collides_with_list(self.bullet_list)
                for c in collisions:
                    e.hp -= BULLET_DAMAGE
                    self.bullet_list.remove(b)
                    if e.hp <= 0:
                        self.enemy_list.remove(e)
                        self.score += KILL_SCORE
        
        for e in self.enemy_list:
            e.center_x += ENEMY_SPEED





            

    def on_draw(self):
        arcade.start_render()
        arcade.draw_text(str(self.score), 20, SCREEN_HEIGHT - 40, arcade.color.GHOST_WHITE, 16)
        self.player.draw()
        self.bullet_list.draw()
        self.enemy_list.draw()
        if len(self.enemy_list) == 0:
            arcade.draw_text('YOU WIN', 375, SCREEN_HEIGHT - 40, arcade.color.GHOST_WHITE, 24)

    def on_mouse_motion(self, x, y, dx, dy):
        '''
        The player moves left and right with the mouse
        '''
        self.player.center_x = x

    def on_mouse_press(self, x, y, button, modifiers):
        if button == arcade.MOUSE_BUTTON_LEFT:
            x = self.player.center_x
            y = self.player.center_y + 15
            bullet = Bullet((x,y),(0,10),BULLET_DAMAGE)
            self.bullet_list.append(bullet)

def main():
    window = Window(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()