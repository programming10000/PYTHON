#encapsulation in python
class Student(object):
    def __init__(self, first_name, second_name):
        self.first_name = first_name
        self.second_name= second_name

    def get_first_name(self):
        return self.first_name

    def set_first_name(self, first_name):
        self.first_name = first_name

    def get_second_name(self):
        return self.first_name

    def set_second_name(self, second_name):
        self.second_name = second_name