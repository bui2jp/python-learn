def say_test():
    print('hello xxxx')
    s = 'aaa'
    return s

print(say_test)
say_test()

f = say_test
f()

r = f()
print(r)

def what_is_this(color):
    print(color)

what_is_this('bbbb')



# 引数　戻り値
def add_num(a, b) -> int:
    return a + b
r = add_num(1,2)
print(r)

def menu(aaa='999', bbb=888, ccc=777):
    print(aaa)
    print(bbb)
    print(ccc )

# キーワード引数
menu(bbb='111',aaa='222',ccc='333')

menu()


# default引数

def test_func(x, l=[]):
    l.append(x)
    return l

# y = [1,2,3]
# r = test_func(100, y)
# print(r)

# y = [1,2,3]
# r = test_func(200, y)
# print(r)

r = test_func(100)
print(r)

# リストは同じものを指している
# デフォルト引数で配列を初期化しない
r = test_func(100)
print(r)

def test_func2(x, l=None):
    #init
    if l is None:
        l = []
    l.append(x)
    return l

r = test_func2(100)
print(r)
r = test_func2(100)
print(r)

# タプル化 *指定 可変長の引数
def say_something(word, *args):
    print(word)
    print(args)
    for arg in args:
        print(arg)

say_something('word','test2','aaaa')

t = ('bbb','cccc')
say_something('zzz', *t)


#キーワード引数の辞書化
def menu(**kvargs):
    #print(entree)
    #print(drink)
    for k, v in kvargs.items():
        print(k, v)

menu(key1='beef', key2='coffee')

d = {
    'entree': 'aaa',
    'drink': 'bbb',
    'dessert': 'ccc'
}
menu(**d)

def menu2(food, *args, **kwargs):
    print(food)
    print(args)
    print(kwargs)

menu2('aaa', 'bbb', 'ccc', key1=123, key2=456)

#docstrings
def exmaple_fun(param1, param2):
    """Example func

    Args:
        param1 (int):xxx
        param2 (str):
    Returns:
        bool:
    """
print(exmaple_fun.__doc__)
#help(exmaple_fun)

# 関数内関数
def outer_fun(a, b):

    def plus(c, d):
        return c + d
    r = plus(a, b)
    print(r)

outer_fun(1,2)

# クロージャー
def outer(a, b):
    def inner():
        return a + b
    return inner

f = outer(1,2)
r = f()
print(r)

# クロージャー2
def circle_area_func(pi):
    def circle_area(r):
        return pi * r * r
    return circle_area

c1 = circle_area_func(3.14)
c2 = circle_area_func(3.141592)

print(c1(10))
print(c2(10))


#デコレーター
def print_info(func):
    def wrapper(*args, **kwargs):
        print('start')
        r = func(*args, **kwargs)
        print('end')
        return r
    return wrapper

def add_num(a, b):
    return a + b

f = print_info(add_num)
r = f(10,20)
print(r)

#@指定でOK これがデコレーターの指定
# 複数してもできる
@print_info
def add_num2(a, b):
    return a + b

r = add_num2(20,30)
print(r)

# ラムダ
l = ['Mon','tue', 'Web', 'Thu', 'Fri', 'sat', 'sun']

def change_words(words, func):
    for word in words:
        print(func(word))

def sample_func(word):
    return word.capitalize()

change_words(l, sample_func)

sample_func2 = lambda word: word.capitalize()
change_words(l, sample_func2)

change_words(l, lambda word: word.capitalize())
change_words(l, lambda word: word.lower())

# generater
# yield 関数を一時停止して値を返す
l = ['aaa','bbb','ccc']

for i in l:
    print(i)

print('##########')

def greeting():
    yield 'xxxx1'
    yield 'xxxx2'
    yield 'xxxx3'    

for g in greeting():
    print(g)

g = greeting()
print(next(g))
print('@@@')
print(next(g))
print(next(g))


#リスト内包表記
t = (1,2,3,4,5)
t2 = (10,20,30,40,50)

r = []
for i in t:
    r.append(i)
print(r)

r = [i for i in t if i % 2 == 0]
print(r)


r = [i * j for i in t for j in t2]
print(r)

#辞書の包括表記

#集合内包評価 set

#ジェネレーター内包表記

def g():
    for i in range(10):
        yield i

g = g()

g = (i for i in range(10) if i % 2 == 0)
print(type(g))
print(next(g))
print(next(g))
print(next(g))

#名前空間とスコープ
animal = 'cat'

def f():
    #print(animal)
    animal = 'dog' #これはローカル変数
    print(animal)
    print('local ', locals())
print(animal)

f()

print('global: ', globals())