#with closeを自動でやってくれる
s = """\
AAA
BBB
CCC
DDD
"""
with open('test.txt','r') as f:
    print(f.tell())
    print(f.read(1))
    f.seek(5)
    print(f.read(1)) 
    f.seek(14)
    print(f.read(1)) 
    f.seek(0)    
    print(f.read(3)) 