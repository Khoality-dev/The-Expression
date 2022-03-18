class Game_Object:
    def __init__(self, x, y, height, width, opacity = 1.0):
        self.x = x
        self.y = y
        self.height = height
        self.width = width
        self.opacity = opacity
    
    def update(self):
        pass

class Text(Game_Object):
    def __init__(self, x, y, height, width, text = None, opacity = 1.0, font = 'Default'):
        super().__init__(self, x, y, height, width, opacity)
        self.text = text
        self.font = font
        return

    def update(self):
        return

class Button(Game_Object):
    def __init__(self, x, y, height, width, title = None, opacity = 1.0, state = 0):
        super().__init__(self, x, y, height, width, title, opacity)

        self.state = state
        self.icons = []
        self.sounds = []
        return

    def mouse_hover(self):
        return

    def mouse_on_click(self):
        return

    def mouse_on_release(self):
        return

    def update(self):
        return

class Main_Menu():
    def __init__(self):
        self.buttons = []
        self.bgms = []

        return

    def update(self):
        return