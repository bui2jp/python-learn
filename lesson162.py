# test
class Cal(object):
    def add_num(self, x, y):
        """add num

        >>> c = Cal()
        >>> c.add_num(1,1)
        4

        >>> c.add_num('a', 'b')
        Traceback (most recent call last):
        ...
        ValueError
        """
        if type(x) is not int or type(y) is not int:
            raise ValueError
        return (x + y) * 2

if __name__ == '__main__':
    import doctest
    doctest.testmod()