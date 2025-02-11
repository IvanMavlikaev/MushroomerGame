class SpriteList:
    def __init__(self, start_list):
        self.list = start_list
        self.size = len(start_list)

    def update_coordinats(self, delta_x, delta_y):
        for i in range (self.size):
            self.list[i].update_coordinats(delta_x, delta_y)

    def add(self, sprite):
        self.list.append(sprite)
        self.size += 1

    def pop(self):
        if self.size:
            self.list = self.list[1:]
            self.size -= 1
        else:
            raise IndexError