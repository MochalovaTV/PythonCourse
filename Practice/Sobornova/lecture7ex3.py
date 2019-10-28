import pickle
import random

first_names = ('benedict', 'vincent', 'viggo', 'james',
               'jake', 'daniel', 'christian', 'leonardo')
last_names = ('cumberbatch', 'cassel', 'martensen', 'mcavoy',
              'gyllenhaal', 'radcliffe', 'bale', 'dicaprio')


class Human:

    def __init__(self, first_name, last_name, age, height, weight):
        self.first_name = first_name
        self.last_name = last_name
        self.age = str(age)
        self.height = str(height)
        self.weight = str(weight)
        self.info = "{} {}, age = {}, " \
                    "height = {}, weight = {}".format(self.first_name.title(),
                                                      self.last_name.title(), self.age,
                                                      self.height, self.weight)

    def pickling(self):
        with open("human.data", 'wb') as obj:
            pickle.dump(self.info, obj, protocol=3)

    def unpickling(self):
        with open("human.data", 'rb') as obj:
            data_new = pickle.load(obj)
        return data_new


for i in range(1, 10):
    people = Human(random.choice(first_names), random.choice(last_names),
                   random.randint(0, 100), random.randint(0, 300),
                   random.randint(0, 200))
    people.pickling()
    print(people.unpickling())



