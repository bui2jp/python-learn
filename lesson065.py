# error handling

l = [1,2,3,4,5]
i = 2
#del l

try:
    l[i]
except IndexError as ex:
    print('exception... {}'.format(ex))
# except NameError as ex:
#     print('exception... {}'.format(ex))
except Exception as ex:
    print('exception... {}'.format(ex))
else:
    print('else (no exception)')
finally:
    print('finally...')

print('finished...')


#raise IndexError('test error')

class UppercaseError(Exception):
    pass

def check():
    raise UppercaseError('test')

try:
    check()
except UppercaseError as ex:
    print('my exception...')