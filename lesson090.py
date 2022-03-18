#特殊メソッド
class Word(object):

    def __init__(self, text) -> None:
        self.text = text

    def __str__(self) -> str:
        return 'aaaaaaaaaaa'

    def __len__(self):
        return len(self.text)

    def __add__(self, word):
        return self.text.lower() + word.text.lower()

    def __eq__(self, word):
        return self.text.lower() == word.text.lower()

w = Word('aaa')
w2 = Word('aaa')
print(w)
print(len(w))

print(w + w2)

print(w == w2)