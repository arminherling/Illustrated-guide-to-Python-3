# Exercise: Imagine you are creating a Super Mario game. You need to define a class to represent
# Mario. What would it look like? If you aren’t familiar with Super Mario, use your
# own favorite video or board game to model a player.

class Mario:
    '''Super Mario'''

    def __init__(self):
        self._lives = 3
        self._speed = 10
        self._jumpheight = 5
        self._width = 32
        self._height = 64
        self._sprite = "/path/to/sprite.png"

    def draw(self, screen):
        # draw sprite to screen
        return 


    def update(self, delta_time):
        # use jump method if jump button is pressed
        # use run if left or right is pressed
        return 


    def move(self, direction):
        # use speed and move in the specified direction
        return 


    def jump(self):
        # use jump height to determine the height
        return 


    def collides(self, other):
        # use width and height to determine if mario collides with object
        return 
