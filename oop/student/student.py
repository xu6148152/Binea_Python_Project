__author__ = 'xubinggui'

class Student(object):
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def print_score(self):
        print(self.score)

bart = Student('Bart Simpson', 59)
bart.print_score()