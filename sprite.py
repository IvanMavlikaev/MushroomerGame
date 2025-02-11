class Sprite:
    def __init__(self, start_x, start_y, name):
        self.x = start_x
        self.y = start_y
        self.name = name

    def update_coordinats(self, delta_x, delta_y):
        self.x += delta_x
        self.y += delta_y
        print(self.x, self.y)

    def copy(self, other):
        self.x = other.x
        self.y = other.y
        self.name = other.name