from example2 import Java
class Python(Java):
    def __init__(self):
        self.i_am_groot = 'I am Groot'
        self.i_am_attribute = 'I am attribute'

    def create_game(self):
        return 'I can make a game'

    def create_site(self):
        return 'I can make a site'

python = Python()
print(python.i_am_groot)
print(python.i_am_attribute)

print(python.create_game())
print(python.create_site())