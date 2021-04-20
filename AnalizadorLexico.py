# -*- coding: utf-8 -*-

from io import IOBase
import ComponentesLexicos
from Detectores import detectores
from Errores import ErrorLexico

class AnalizadorLexico():
    
    def __init__(self, archivo: IOBase, tablaDeSimbolos: dict): #se ejecuta solo al crear el Lexico (constructor)
        self.x = 0
        self.y = 0
        self.codigoFuente = archivo.readlines()
        self.tablaDeSimbolos = tablaDeSimbolos
        self.detectores = detectores
        self.caractesIgnorados = [' ', '\t']
        self.caractesDeCierre = ['\n']

    def siguienteComponenteLexico(self) -> (bool, str, str): #devuelve componente lexico, y lexema

        while self.y < len(self.codigoFuente) and self.x < len(self.codigoFuente[self.y]) and self.codigoFuente[self.y][self.x] in self.caractesIgnorados  and self.codigoFuente[self.y][self.x] not in  self.caractesDeCierre:
            self.x += 1

        while self.y < (len(self.codigoFuente)-1) and self.codigoFuente[self.y][self.x] == "\n":
            self.x = 0
            self.y += 1

        if not (self.y < (len(self.codigoFuente)-1)) and not (self.x < len(self.codigoFuente[self.y])):
            return (True, ComponentesLexicos.peso, "$")

        for detector in self.detectores:
            (detectado, lexema, componenteLexico) = detector(self.codigoFuente, self.x, self.y)
            if detectado:
                self.x += + len(lexema)
                return (True, componenteLexico, lexema)
        
        raise ErrorLexico(linea = self.y+1, posicion = self.x+1)