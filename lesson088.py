#クラス変数
from select import KQ_FILTER_VNODE


class Person(object):

    kind = 'human' # クラス変数　すべてのオブジェクトで共有される

    def __init__(self, name) -> None:
        self.name = name

    def who_are_you(self):
        print(self.name, self.kind)
    
a = Person('A')
a.who_are_you()

b = Person('B')
b.who_are_you()

class T(object):
    words = []

    def add(self, word):
        self.words.append(word)


c = T()
c.add('aaa')
c.add('bbb')

print(c.words)

d = T()
d.add('aaa')
d.add('bbb')

#wordsは同じものを指すよ
print(c.words)
print(d.words)