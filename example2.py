
class Java:
    def __init__(self):
        self.name = 'Java'
        self.paradigms = 'OOP'
        self.lang_type = 'Compiled'

    def create_desktop(self):
        return 'I can create Desktop software'

    def create_game(self):
        return 'I can make a game'

    def create_site(self):
        return 'I can make a site'

class Python(Java):
    def __init__(self):
        Java.__init__(self)
        self.name = 'Python'
        self.paradigms = ('OOP')

p = Python()
print(p.create_site())