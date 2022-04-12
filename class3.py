from class2 import Factory


class Toyota(Factory):
    def __init__(self):
        Factory.__init__(self)
        self.wheel = 'Wheel shop'
        self.windows = 'Windows shop'

    def create_wheels(self):
        return 'Wheel is ready'

    def create_windows(self):
        return 'Windows are ready'

    def save_methods(self):
        method_list = []
        for method in dir(Toyota):
            if method.startswith('__') is False:
                method_list.append(method)
        print(method_list)

t = Toyota()
print(t.create_wheels())
print(t.create_windows())
print(t.save_methods())





