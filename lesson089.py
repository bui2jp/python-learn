class Person(object):

    kind = 'human'

    def __init__(self) -> None:
        self.x = 100

    @classmethod #クラスメソッド指定することで、オブジェクトを生成しなくても関数を利用
    def what_is_your_kind(cls):
        return cls.kind

    @staticmethod
    def about(year):
        print('about human {}'.format(year))

print(Person.kind)
Person.about(10)