import arcade

# Constants
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 650
SCREEN_TITLE = "Poppetje"

#nieuw
CHARACTER_SCALING = 1
TILE_SCALING = 0.5


class MyGame(arcade.Window):
    def __init__(self):

        # Call the parent class and set up the window
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)

        #nieuw
        self.player_list = None
        self.player_sprite = None


        self.wall_list = None



        arcade.set_background_color(arcade.csscolor.CORNFLOWER_BLUE)

    def setup(self):
        """ Set up the game here. Call this function to restart the game. """
        #nieuw
        self.player_list = arcade.SpriteList()


        plaatje = "player_stand.png"
        self.player_sprite = arcade.Sprite(plaatje, CHARACTER_SCALING)
        self.player_sprite.center_x = 64
        self.player_sprite.center_y = 120

        self.player_list.append(self.player_sprite)


        self.wall_list = arcade.SpriteList(use_spatial_hash=True)

        for x in range(0, 1250, 64):
            wall = arcade.Sprite(":resources:images/tiles/grassMid.png", TILE_SCALING)
            wall.center_x = x
            wall.center_y = 32
            self.wall_list.append(wall)


    def on_draw(self):
        """ Render the screen. """

        arcade.start_render()

        #nieuw
        self.player_list.draw()
        self.wall_list.draw()
        # Code to draw the screen goes here

    def on_update(self, delta_time):
        """ Movement and game logic """

        # nieuw: Move the player with the physics engine
     
    def on_key_press(self, key, modifiers):
        """Called whenever a key is pressed. """
        pass

    def on_key_release(self, key, modifiers):
        """Called when the user releases a key. """
        pass

 


def main():
    """ Main method """
    window = MyGame()
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()