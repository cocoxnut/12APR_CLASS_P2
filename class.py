class Human:
    money = 0

    def get_money(self, salary):
        return self.money + salary

class Person(Human):
    money = 0

per = Person()
print(per.get_money(500))