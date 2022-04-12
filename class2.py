class Factory:
    def __init__(self):
        self.engine = 'I am an Engine shop'
        self.bridge = 'I am an Mechanic shop'

    def create_eng(self):
        return 'Engine is done'

    def create_brdg(self):
        return 'Bridge is done'

fact = Factory()
print(fact.engine)
print(fact.bridge)

print(fact.create_eng())
print(fact.create_brdg())