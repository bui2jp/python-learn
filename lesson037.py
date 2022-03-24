# 37

#is_ok = 1 # 0以外はTrue
#is_ok = 0 # False
#is_ok = 'a'
#is_ok=[] #中身がないのはFalse
is_ok=[1,2,3]

if is_ok:
    print('ok')
else:
    print('ng')


#
# None
#
is_empty = None
print(is_empty)

#if is_empty == None:
if is_empty is not None:
    print('None')


print(1==True)
aaa = True
print(1 is True)
print(aaa is True)

#
# while
#
count = 0
while count<5:
    print(count)
    count += 1

count = 0
while True:
    #print('xxx')
    if count >= 5:
        break

    if count == 2:
        count += 1
        continue

    print(count)
    count += 1
    
count = 0
while count < 5:
    if count == 1:
        break

    print(count)
    count += 1
else:
    # breakの場合は実行されない
    print('done')

# while と input 関数
# while True:
#     word = input('enter:')
#     if word == 'ok':
#         break
#     print('next')

# for
some_list = [1,3,4,5,2]
i = 0
while i < len(some_list):
    print(some_list[i])
    i += 1

# イテレーター
for i in some_list:
    print(i)
for s in 'aaaaa':
    print(s)
for s in ['aaa','eds','asafd']:
    print(s)
else: #forでも利用できるよ
    print('done')

#range関数
num_list = [0,1,2,3,4]
#for i in num_list:
for _ in range(10):    
    print('test')
for index in range(10):    
    print(index, 'test')

# enumerate
for i, f in enumerate(['a','b','c']):
    print(i, f)