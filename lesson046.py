


days = [1,2,3,10]
fruits = [4,5,6,]
drinks = [7,8,9]

for a, b, c in zip(days, fruits, drinks):
    print(a, b, c)

#dictionary (key, value)
d = {'a':100, 'b':200}
print(d)
print(d.items())
for k, v in d.items():
    print(k, ':', v)