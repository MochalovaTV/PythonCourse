
# First task

def print_more_and_less(num1, num2):
    if num1 >= num2:
        print(num1)
    else:
        print(num2)

print_more_and_less(6, 9)

# Second task

def return_more_and_less(num1, num2):
    if num1 >= num2:
        return num1
    else:
        return num2

print(return_more_and_less(1, 5))

#Third task

class Effect_from_items():
    def default_value (self):
        print('Движение и анимация вернулись к стандартным')
    def speed_down (self):
        print('Движение замедлилось вместе с анимацией')
    def speed_up (self):
        print('Движение ускорилось вместе с анимацией')

class Animations(Effect_from_items):
    def anim_run(self):
        print('Реализует анимацию бега')
    def anim_shot(self):
        print('Реализует анимацию стрельбы')
    def anim_collection(self):
        print('Реализует анимацию сбора предметов')
    def anim_fly(self):
        print('Реализует анимацию полета')

class General_action(Animations):
    objects = ['norm', 'up', 'down']  # Список возможных объектов для взаимодействия
    def run(self):
        self.anim_run()
        print('Персонаж перемещается')
    def fast_run(self):
        self.anim_run()
        print('Персонаж перемещается быстро')
    def slow_run(self):
        self.anim_run()
        print('Персонаж перемещается медленно')
    def shot(self):
        print('Персонаж производит выстрел')
        self.anim_shot()
    def collection(self, obj):  # Дополнительно вводим объект, который собрал игрок
        print('Персонаж собирает предмет')
        self.anim_collection()
        self.obj = obj
        if obj == self.objects[1]:
            self.fast_run()
            self.speed_up()
        elif obj == self.objects[2]:
            self.slow_run()
            self.speed_down()

class Special_action(General_action):
    def fly(self):
        print('Персонаж летает')
        self.anim_fly()

class Gamer ():
    def __init__(self, name):
        self.name = name

class Player1 (Gamer, General_action):
    pass

class Player2 (Gamer, Special_action):
    pass

player1 = Player1('Mark')

player1.collection('up')





