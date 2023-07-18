class Brick:

    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def clicked(self, event):
        print('You clicked')
