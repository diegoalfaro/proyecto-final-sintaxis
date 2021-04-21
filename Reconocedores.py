# -*- coding: utf-8 -*-

import ComponentesLexicos
import string

def leerCaracter(codigoFuente: list, x: int, y: int)-> str:
    if y < len(codigoFuente) and x < len(codigoFuente[y]):
        return codigoFuente[y][x]
    else:
        return ""

def esSimbolo(codigoFuente: str, x: int, y: int) -> (bool, str, str):
    linea = codigoFuente[y]
    for simbolo in ComponentesLexicos.simbolos:
        if linea.startswith(simbolo, x):
            return (True, simbolo, simbolo)
    return (False, None, None)

def esId(codigoFuente: str, x: int, y: int) -> (bool, str, str):
    def simboloID(aux: str)-> int:
        if aux in string.ascii_letters:
            return 0
        elif aux in string.digits:
            return 1
        elif aux == "_":
            return 2
        else:
            return 3
    def simbolo(aux: str) -> bool:
        return True if aux in {'=', '+', '-', '.', '*', '/', ';', ',', '(', ')', '[', ']', '^' } else False
    q0 = 0
    F = {1}
    # Q = (0,1,2)
    # sigma=[(letra, digito, guionBajo, otro)]   #letra = 0ra columna, digito = 1da columna, guionBajo = 2ra columna, otro= 3ta columna)
    delta = {
        (0,0): 1,
        (0,1): 2,
        (0,2): 2,
        (0,3): 2,
        (1,0): 1,
        (1,1): 1,
        (1,2): 1,
        (1,3): 2,
        (2,0): 2,
        (2,1): 2,
        (2,2): 2,
        (2,3): 2
    }
    lexema = ""
    linea = codigoFuente[y]
    auxControl = x
    T = leerCaracter(codigoFuente, auxControl, y)
    estado = q0
    while (estado != 2) and (auxControl < len(linea)) and (T != " ") and (T != "\n") and (not simbolo(T)):
        estado = delta[(estado,simboloID(T))]
        lexema = lexema + T
        auxControl = auxControl + 1
        T = leerCaracter(codigoFuente, auxControl, y)
    if estado in F:
        return (True, lexema, ComponentesLexicos.id)
    else:
        return (False, None, None)

def esConstReal(codigoFuente: str, x: int, y: int) -> (bool, str, str):
    def simbCONS(Car: str)-> int:
        if Car in string.digits:
            return 0
        elif Car == '-':
            return 1
        elif Car == '.':
            return 2
        elif Car in ('e', 'E'):
            return 3
        else:
            return 4
    def simbolo(aux: str) -> bool:
        return True if aux in {'=', '+', '*', '/', ';', ',', '(', ')', '[', ']', '^'} else False
    q0=0
    F={4, 2, 7}
    #Q=range(1,9)
    #sigma=(D, menos, punto, E, O)
    delta = {
        (0,0): 2,
        (0,1): 1,
        (0,2): 8,
        (0,3): 8,
        (0,4): 8,
        (1,0): 2,
        (1,1): 8,
        (1,2): 8,
        (1,3): 8,
        (1,4): 8,
        (2,0): 2,
        (2,1): 8,
        (2,2): 3,
        (2,3): 5,
        (2,4): 8,
        (3,0): 4,
        (3,1): 8,
        (3,2): 8,
        (3,3): 8,
        (3,4): 8,
        (4,0): 4,
        (4,1): 8,
        (4,2): 8,
        (4,3): 5,
        (4,4): 8,
        (5,0): 7,
        (5,1): 6,
        (5,2): 8,
        (5,3): 8,
        (5,4): 8,
        (6,0): 7,
        (6,1): 8,
        (6,2): 8,
        (6,3): 8,
        (6,4): 8,
        (7,0): 7,
        (7,1): 8,
        (7,2): 8,
        (7,3): 8,
        (7,4): 8,
        (8,0): 8,
        (8,1): 8,
        (8,2): 8,
        (8,3): 8,
        (8,4): 8
    }
    estado = q0
    auxControl = x
    linea = codigoFuente[y]
    lexema = ""
    linea = codigoFuente[y]
    T = leerCaracter(codigoFuente, auxControl, y)
    while (estado != 8) and (auxControl < len(linea)) and (T != " ") and (T != "\n") and (not simbolo(T)):
        estado = delta[(estado, simbCONS(T))]
        if estado != 8:
            lexema = lexema + T
            auxControl = auxControl+1
            T = leerCaracter(codigoFuente, auxControl, y)
    if estado in F:
        return (True, lexema, ComponentesLexicos.real)
    else:
        return (False, None, None)

def esPalabraReservada(codigoFuente: str, x: int, y: int) -> (bool, str, str):
    linea = codigoFuente[y]
    if linea[x] in string.ascii_letters:
        for palabraReservada in ComponentesLexicos.palabrasReservadas:
            palabra = ''.join(filter(lambda x: x in (string.ascii_letters + string.digits), linea[x:x+len(palabraReservada)+1]))
            if palabraReservada == palabra:
                return (True, palabraReservada, palabraReservada)
    return (False, None, None)

def esCadena(codigoFuente: str, x: int, y: int) -> (bool, str, str):
    def simbCAD(aux: str)-> int:
        if aux == "\"":
            return 0
        if aux in string.ascii_letters:
            return 1
        elif aux in string.digits:
            return 1
        elif aux in string.punctuation:
            return 1
        elif aux in {" "}:
            return 1
        else:
            return 2
    q0 = 0
    F = [2]
    #Q=0..3
    # #sigma=(C,O);
    delta = {
        (0,0): 1,
        (0,1): 3,
        (0,2): 3,
        (1,0): 2,
        (1,1): 1,
        (1,2): 3,
        (2,0): 3,
        (2,1): 3,
        (2,2): 3,
        (3,0): 3,
        (3,1): 3,
        (3,2): 3
    }
    auxControl = x
    linea = codigoFuente[y]
    estado = q0
    lexema = ''
    T = leerCaracter(codigoFuente, auxControl, y)
    while estado != 3  and auxControl < len(linea)  and T!="\n" and (estado not in F):
        estado= delta[(estado,simbCAD(T))]
        if estado!=3:
            lexema = lexema + T
            auxControl = auxControl+1
            T = leerCaracter(codigoFuente, auxControl, y)
    if estado in F:
        return (True, lexema, ComponentesLexicos.cadena)
    else:
        return (False, None, None)

reconocedores = [
    esConstReal,
    esPalabraReservada,
    esSimbolo,
    esCadena,
    esId,
]