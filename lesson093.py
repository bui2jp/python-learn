#with closeを自動でやってくれる
s = """\
AAA
BBB
CCC
DDD
"""
with open('test.txt','r') as f:
    #print(f.read())
    while True:
        #line = f.readline()
        chunk = 2
        line = f.read(chunk)
        print(line,'\n')
        if not line:
            break

