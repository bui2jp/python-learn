#with closeを自動でやってくれる
s = """\
AAA
BBB
CCC
DDD
"""
#with open('test.txt','w+') as f:
with open('test.txt','r+') as f:    
    print(f.read())   
    f.write(s)
    f.seek(0)

