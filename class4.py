class Zoo:
    def __init__(self):
        self.animal_1 = 'Tiger'
        self.animal_2 = 'Hippo'
        self.animal_3 = 'Giraffe'


    def change_attr1(self):
        self.animal_1 = 'Lion'
        return self.animal_1


    def change_attr3(self):
        self.animal_3 = 'Snake'
        return self.animal_3

z = Zoo()
print(z.change_attr1())
print(list(z.__dict__.items()))
print(z.change_attr3())
