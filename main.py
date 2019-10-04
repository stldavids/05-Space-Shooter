import sys, logging, json, arcade

#check to make sure we are running the right version of Python
version = (3,7)
assert sys.version_info >= version, "This script requires at least Python {0}.{1}".format(version[0],version[1])

#turn on logging, in case we have to leave ourselves debugging messages
logging.basicConfig(format='[%(filename)s:%(lineno)d] %(message)s', level=logging.DEBUG)
logger = logging.getLogger(__name__)

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Space Shooter"
MOVEMENT_SPEED = 5


class Window(arcade.Window):

    def __init__(self, width, height, title):

        # Call the parent class's init function
        super().__init__(width, height, title)

        # Make the mouse disappear when it is over the window.
        # So we just see our object, not the pointer.
        self.set_mouse_visible(False)

        arcade.set_background_color(arcade.color.BLACK_LEATHER_JACKET)

        # Sprite lists
        self.player_list = arcade.SpriteList()

        # Set up the player
        self.score = 0




    def setup(self):


        # Set up the player
        self.score = 0
        self.player = arcade.Sprite('assets/PNG/playerShip2_blue.png', 1)
        self.player.center_x = SCREEN_WIDTH // 2
        self.player.center_y = SCREEN_HEIGHT // 2
        self.player_list.append(self.player)



    def update(self, delta_time):
        pass

    def on_draw(self):
        """ Called whenever we need to draw the window. """
        arcade.start_render()
        self.player_list.draw()




    def on_mouse_motion(self, x, y, dx, dy):
        """ Called to update our objects. Happens approximately 60 times per second."""
        pass

    def on_mouse_press(self, x, y, button, modifiers):
        """
        Called when the user presses a mouse button.
        """
        pass

    def on_mouse_release(self, x, y, button, modifiers):
        """
        Called when a user releases a mouse button.
        """
        pass

    def on_key_press(self, key, modifiers):
        """ Called whenever the user presses a key. """
        if key == arcade.key.LEFT:
            self.player.center_y += MOVEMENT_SPEED
        elif key == arcade.key.RIGHT:
            self.player.center_y -= MOVEMENT_SPEED
        elif key == arcade.key.UP:
            self.player.center_x -= MOVEMENT_SPEED
        elif key == arcade.key.DOWN:
            self.player.center_x += MOVEMENT_SPEED

    def on_key_release(self, key, modifiers):
        """ Called whenever a user releases a key. """
        #When the user releases the keys, the players movement stops.
        pass


def main():
    window = Window(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()