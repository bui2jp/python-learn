#with closeを自動でやってくれる
with open('test.txt','w') as f:
    f.write('Test with ¥n')
    print('My', 'name', 'is', sep='#', end='!', file=f)

