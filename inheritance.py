class animal:
    def __init__(self, name):
        self.name = name

    def print_name(self):
        print(self.name)

class dog(animal):
    def __init__(self, name):
        super().__init__(name)

c = dog("Bob")
c.print_name()