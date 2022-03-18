#多重継承

class Person(object):
    def talk(self):
        print('talk')
    
    def run(self):
        print('person run')

class Car(object):
    def run(self):
        print('car run')

class PersonCarRobot(Car, Person):
    def fly(self):
        print('fly')

person_car_robot = PersonCarRobot()
person_car_robot.talk()
person_car_robot.run() #継承の順番
person_car_robot.fly()