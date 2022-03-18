import abc

# 抽象クラス metaclass=abc.ABCMeta
class Person(metaclass=abc.ABCMeta):
    def __init__(self, age=1) -> None:
        self.age = age

    @abc.abstractmethod
    def drive(self):
        pass

# Personを継承しているよ
class Baby(Person):
    def __init__(self, age=1) -> None:
        super().__init__(age)

    def drive(self):
        raise ValueError

class Adult(Person):
    def __init__(self, age=18) -> None:
        super().__init__(age)
    def drive(self):
        print('ok')

baby = Baby()
adult = Adult()

class Car(object):
    def __init__(self, model=None):
        print('__init__ start')
        self.model = model
    def run(self, model=None):
        print('run', 'model: ' , self.model)
        print('a')
    def ride(self, person):
        person.drive()
    def __del__(self):
        print('__del__ start')

class ToyotaCar(Car):
    def run(self):
        print('run toyota')

class TeslaCar(Car):
    def __init__(self, model='tesla', enable_auto_run=False, passwd='123'):
        #親のコンストラクタの呼び出し
        super().__init__(model)        

        #_ プロパティーを介してアクセス
        self._enable_auto_run = enable_auto_run

        self.passwd = passwd
    #プロパティーの利用(getter)
    @property
    def enable_auto_run(self):
        return self._enable_auto_run
    #プロパティーの利用(setter)
    @enable_auto_run.setter
    def enable_auto_run(self, is_enable):
        if self.passwd == '456':
            self._enable_auto_run = is_enable
        else:
            raise ValueError

    def run(self):
        print('run ' + self.model)

print('## Car ##')
car = Car('aaa')
car.run()
car.ride(baby)
print('## Toyota ##')
toyota_car = ToyotaCar()
toyota_car.ride(adult)

print('## Tesla ##')
tesla_car = TeslaCar(passwd='456')
tesla_car.run()
tesla_car.enable_auto_run = True
print('enable_auto_run: ', tesla_car.enable_auto_run)
print('### del ###')
del car
del toyota_car
del tesla_car

print('### end ###')