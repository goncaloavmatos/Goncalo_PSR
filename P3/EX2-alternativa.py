#!/usr/bin/python3

from collections import namedtuple
Complex = namedtuple('Complex', ['r','i'])

def addComplex(x, y):
    a = x.r
    b = x.i
    c =y.r
    d=y.i
    return (r=a + c,i=b + d)


def multiplyComplex(x, y):
    a = x.r
    b = x.i
    c = y.r
    d = y.i
    result_real= (a*c - b*d)
    result_im = (a*d + b*c)
    return(result_real, result_im)

def printComplex(x, prefix=''):
    # add code here ...
    a = x.r
    b = x.i
    print(prefix + str(a) + '+' + str(b) + 'i')

def main():
    # ex2 a)

    # define two complex numbers as tuples of size two
    c1 = Complex(5, 3)
    c2 = (r=-2, i=7)

    printComplex(c1, prefix='c1= ')
    printComplex(c2, prefix='c2= ')

    # Test add
    print('addition')
    c3 = addComplex(c1, c2)
    printComplex(c3)

    # test multiply
    print('multiplication')
    printComplex(multiplyComplex(c1, c2))

if __name__ == '__main__':
    main()