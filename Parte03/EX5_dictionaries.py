#!/usr/bin/python3

from collections import namedtuple

Complex = namedtuple('Complex',['r', 'i'])  # criar tuplo Complex, novo tipo de dados, neste caso com dois campos, um r e um i


def addComplex(x, y):
    # Complex number addition: (a+b*i) + (c+d*i) = (a+c) + (b+d)*i
    a = x['r']  # a é a parte real do primeiro numero
    b = x['í']  # a é a parte imaginaria do primeiro numero
    c = y['r']  # c é a parte real do segundo numero
    d = y['i']  # d é a parte imaginaria do segundo numero
    return {'r': a + c,'i' : b + d}  # valor real e imaginario da soma pela formula da soma de numeros complexos
    # IMPORTANTE: adicionar o Complex, para que o resultado da adição dos valores dos tuplos seja retornado também como um tuplo


def multiplyComplex(x, y):
    # Complex number multiplication: (a+b*i) x (c+d*i) = (a*c-b*d) + (a*d+b*c)*i
    a = x['r']  # a é a parte real do primeiro numero
    b = x['í']  # a é a parte imaginaria do primeiro numero
    c = y['r']  # c é a parte real do segundo numero
    d = y['i']  # d é a parte imaginaria do segundo numero
    return {'r': (a*c-b*d),'i' : (a*d+b*c)} # valor real e imaginario da multiplicação pela formula da multiplicação de numeros complexos


def printComplex(x, prefix=''):  # prefixo vazio por defeito, mas pode ser editado

    r = x['r']  # parte real é a primeira posição (0) do numero x
    i = x['i']  # parte imag é a segunda posição (1) do numero x
    print(prefix + str(r) + '+' + str(i) + 'i')



def main():
    #create a complex number as an instance of class ComplexClass
    c1 = {'r': 4, 'i' : 8}
    c2 = {'r': 6, 'i' : -7}

    printComplex(c1, prefix='c1= ')
    printComplex(c2, prefix='c2= ')


    #Addition
    c3 = addComplex(c1,c2)
    printComplex(c3, prefix='Addition|  c3= ')

    #Multiplication
    c3 = multiplyComplex(c1,c2)
    printComplex(c3, prefix='Multiplication|  c3= ')


if __name__ == '__main__':
    main()
