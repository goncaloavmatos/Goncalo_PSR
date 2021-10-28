#!/usr/bin/python3

def addComplex(x, y):
    # Complex number addition: (a+b*i) + (c+d*i) = (a+c) + (b+d)*i
    a= x[0]  #a é a parte real do primeiro numero
    b= x[1]  #a é a parte imaginaria do primeiro numero
    c= y[0] #c é a parte real do segundo numero
    d= y[1] #d é a parte imaginaria do segundo numero
    return (a+c, b+d) #valor real e imaginario da soma pela formula da soma de numeros complexos

def multiplyComplex(x, y):
    # Complex number multiplication: (a+b*i) x (c+d*i) = (a*c-b*d) + (a*d+b*c)*i
    a = x[0]  # a é a parte real do primeiro numero
    b = x[1]  # a é a parte imaginaria do primeiro numero
    c = y[0]  # c é a parte real do segundo numero
    d = y[1]  # d é a parte imaginaria do segundo numero
    return (a*c-b*d, a*d+b*c )  # valor real e imaginario da multiplicação pela formula da multiplicação de numeros complexos

def printComplex(x, prefix=''):  #prefixo vazio por defeito, mas pode ser editado
        # add code here ...
    r = x[0] #parte real é a primeira posição (0) do numero x
    i = x[1] #parte imag é a segunda posição (1) do numero x
    print(prefix + str(r) + '+' + str(i) + 'i')

def main():
    # ex2 a)

    # define two complex numbers as tuples of size two
    c1 = (5, 3)
    c2 = (-2, 7)

    printComplex(c1, prefix='c1= ')
    printComplex(c2, prefix='c2= ')

    # Test add
    c3 = addComplex(c1, c2)
    printComplex(c3,prefix='Addition: c3= ')

    # test multiply
    c3 = multiplyComplex(c1, c2)
    printComplex(c3,prefix='Multiplication: c3= ')

if __name__ == '__main__':
    main()