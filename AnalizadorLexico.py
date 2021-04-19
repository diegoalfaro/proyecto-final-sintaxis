# -*- coding: utf-8 -*-

from io import IOBase
from TablaDeSimbolos import TablaDeSimbolos
import string
import ComponentesLexicos
from Textos import ERROR_LEXICO

class AnalizadorLexico():
    
    def __init__(self, archivo: IOBase, tablaDeSimbolos: TablaDeSimbolos): #se ejecuta solo al crear el Lexico (constructor)
        self.x = 0
        self.y = 0
        self.codigoFuente = archivo.readlines()
        self.tablaDeSimbolos = tablaDeSimbolos

    def siguienteComponenteLexico(self) -> (str, str): #devuelve componente lexico, y lexema

        while self.y < len(self.codigoFuente) and self.x < len(self.codigoFuente[self.y]) and self.codigoFuente[self.y][self.x] == " "  and self.codigoFuente[self.y][self.x] != "\n": #mientras sea espacio o salto de pagina avanza uno, sin salirse del rang
            self.x += 1

        while self.y < (len(self.codigoFuente)-1) and self.codigoFuente[self.y][self.x] == "\n":
            self.x = 0
            self.y += 1

        if not (self.y < (len(self.codigoFuente)-1)) and not (self.x < len(self.codigoFuente[self.y])):
            return (ComponentesLexicos.peso, "$")

        funciones = [
            esConstReal,
            esEscribir,
            esLeer,
            esSimbolo,
            esId,
            esCadena,
        ]

        try:
            for funcion in funciones:
                (detectado, lexema, componenteLexico) = funcion(self.codigoFuente, self.x, self.y)
                if detectado:
                    if (componenteLexico == ComponentesLexicos.id):
                        self.tablaDeSimbolos.actualizarTS(lexema, "0")
                    self.x += + len(lexema)
                    return (componenteLexico, lexema)
        except:
            return (None, None)
        
        print(ERROR_LEXICO.format(x=self.x,y=self.y))

def leerCaracter(codigoFuente: list, x: int, y: int)-> str:
    if y < len(codigoFuente) and x < len(codigoFuente[y]):
        return codigoFuente[y][x]
    else:
        return ""

######################################################################################################
#########################################      AUTOMATAS      ########################################
######################################################################################################

def esSimbolo(codigoFuente: str, x: int, y: int) -> (bool, str, str):
    def componenteLexicoSimbolo (aux: int)-> str:
        if aux == '=':
            return ComponentesLexicos.igual
        elif aux == '+':
            return ComponentesLexicos.mas
        elif aux == '-':
            return ComponentesLexicos.menos
        elif aux == '*':
            return ComponentesLexicos.por
        elif aux == '/':
            return ComponentesLexicos.dividido
        elif aux == ";":
            return ComponentesLexicos.puntoycoma
        elif aux == ",":
            return ComponentesLexicos.coma
        elif aux == '.':
            return ComponentesLexicos.punto
        elif aux == "(":
            return ComponentesLexicos.parentesisAbre
        elif aux == ")":
            return ComponentesLexicos.parentesisCierra
        else:
            return None
    lexema = leerCaracter(codigoFuente, x, y)
    componenteLexico = componenteLexicoSimbolo(lexema)
    if componenteLexico:
        return (True, lexema, componenteLexico)
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
        return True if aux in {'=', '+', '-', '.', '*', '/', ';', ',', '(', ')'} else False
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
        return True if aux in {'=', '+', '*', '/', ';', ',', '(', ')'} else False
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

def esLeer(codigoFuente: str, x: int, y: int) -> (bool, str, str):
    linea = codigoFuente[y]
    if linea.lower().startswith("leer", x):
        return (True, "leer", ComponentesLexicos.leer)
    else:
        return (False, None, None)

def esEscribir(codigoFuente: str, x: int, y: int) -> (bool, str, str):
    linea = codigoFuente[y]
    if linea.lower().startswith("escribir", x):
        return (True, "escribir", ComponentesLexicos.escribir)
    else:
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

#######################################################TESTING#######################################################
"""
archivo=open(r"prueba.txt")
lex=Lexico(archivo)

a = lex.siguienteComponenteLexico()
print(a)
a = lex.siguienteComponenteLexico()
print(a)
a = lex.siguienteComponenteLexico()
print(a)
a = lex.siguienteComponenteLexico()
print(a)
a = lex.siguienteComponenteLexico()
print(a)
a = lex.siguienteComponenteLexico()
print(a)
a = lex.siguienteComponenteLexico()
print(a)
a = lex.siguienteComponenteLexico()
print(a)
a = lex.siguienteComponenteLexico()
print(a)
a = lex.siguienteComponenteLexico()
print(a)
a = lex.siguienteComponenteLexico()
print(a)
a = lex.siguienteComponenteLexico()
print(a)
a = lex.siguienteComponenteLexico()
print(a)
a = lex.siguienteComponenteLexico()
print(a)
a = lex.siguienteComponenteLexico()
print(a)
"""