"""Calculadora simples com as quatro operações básicas.
"""


def adicao(x, y):
    """Calculo de adição.
    Args:
        x (float): Primeiro parâmetro da adição.
        y (float): Segundo parâmetro da adição.
    Return:
        Resultado da adição.
    """
    if type(x) == str or type(y) == str:
        return "Uma letra não pode ser operada"
    else:
        return x+y


def subtracao(x, y):
    """Calculo de subtração.
    Args:
        x (float): Primeiro parâmetro da subtração.
        y (float): Segundo parâmetro da subtração.
    Return:
        Resultado da subtração.
    """
    try:    
        return x - y
    except TypeError:
        return "Uma letra não pode ser operada"


def multiplicacao(x, y):
    """Calculo de multiplicação.
    Args:
        x (float): Primeiro parâmetro da multiplicação.
        y (float): Segundo parâmetro da multiplicação.
    Return:
        Resultado da multiplicação.
    """
    if type(x) == str or type(y) == str:
        return "Uma letra não pode ser operada"
    else:
        return x*y


def divisao(x, y):
    """Calculo de divisão.
    Args:
        x (float): Primeiro parâmetro da divisão.
        y (float): Segundo parâmetro da divisão. Tem que ser diferente de zero.
    Return:
        Resultado da divisão.
    """
    try:    
        return x/y
    except TypeError:
        return "Uma letra não pode ser operada"
    except ZeroDivisionError:
        return "Divisão por zero"