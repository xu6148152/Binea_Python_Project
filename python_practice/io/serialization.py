__author__ = 'xubinggui'

import json

try:
    import cPickle as pickle

except ImportError:
    import pickle


d = dict(name = 'bob', age = 20, score = 80)
print pickle.dumps(d)

f = open('dump.txt', 'wb')
pickle.dump(d, f)
f.close()

f = open('dump.txt', 'rb')
d = pickle.load(f)
f.close()
print d

print json.dumps(d)

json_str = '{"age": 20, "score": 88, "name": "Bob"}'
print json.loads(json_str)

class Student(object):
    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score

s = Student('Bob', 20, 88)

# def student2dict(std):
#     return {
#         'name': std.name,
#         'age': std.age,
#         'score': std.score
#     }

# print json.dumps(s, default = student2dict)

print json.dumps(s, default= lambda obj : obj.__dict__)