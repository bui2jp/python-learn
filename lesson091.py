#ファイルの作成

f = open('test.txt','w')
f.write('testa')

#print関数でfileに出力する
print('print', file=f)
print('My', 'name', 'is', sep='#', end='!', file=f)
f.close()

