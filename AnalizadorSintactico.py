# -*- coding: utf-8 -*-

from TAS import TAS
from Arbol import Nodo
from AnalizadorLexico import AnalizadorLexico
import ComponentesLexicos
from Utilidades import modoDebug
from Textos import DEBUG_LEXICO
from Errores import ErrorSintactico

class AnalizadorSintactico():
    def __init__(self, analizadorLexico: AnalizadorLexico):
        self.analizadorLexico = analizadorLexico
        self.arbol = Nodo(ComponentesLexicos.PROGRAMA)
        self.pilaTAS = []
        self.pilaNodos = []
        self.pilaTAS.append(ComponentesLexicos.peso) 
        self.pilaTAS.append(ComponentesLexicos.PROGRAMA)
        self.pilaNodos.append(self.arbol) 
        self.nodoActual = self.arbol 

    def analizar(self) -> Nodo:
        (detectado, componenteLexico, lexema) = self.analizadorLexico.siguienteComponenteLexico() 

        resultado = None

        if modoDebug():
            print(DEBUG_LEXICO.format(componenteLexico=componenteLexico, lexema=lexema))

        while detectado and not resultado:

            X = self.pilaTAS.pop() if len(self.pilaTAS) else None

            if X != ComponentesLexicos.peso:
                self.nodoActual = self.pilaNodos.pop() if len(self.pilaNodos) else None

            if X == componenteLexico == ComponentesLexicos.peso:
                return self.arbol

            elif X in ComponentesLexicos.terminales:
                if X == componenteLexico:
                    self.nodoActual.agregarHijo(Nodo(lexema))
                    (detectado, componenteLexico, lexema) = self.analizadorLexico.siguienteComponenteLexico()
                    if modoDebug():
                        print(DEBUG_LEXICO.format(componenteLexico=componenteLexico, lexema=lexema))
                else:
                    raise ErrorSintactico

            elif X in ComponentesLexicos.variables:
                tupla = (X, componenteLexico)
                if tupla in TAS:
                    auxPilaTAS = []
                    auxPilaNodos = []
                    for i in range(len(TAS[tupla])):
                        self.nodoActual.agregarHijo(Nodo(TAS[tupla][i]))
                        nodo = self.nodoActual.getHijos()[-1]
                        auxPilaTAS.append(TAS[tupla][i])
                        auxPilaNodos.append(nodo)
                    for i in range(len(TAS[tupla])):
                        auxTAS = auxPilaTAS.pop() if len(auxPilaTAS) else None
                        auxNodo = auxPilaNodos.pop() if len(auxPilaNodos) else None
                        if auxTAS != None and auxTAS != ComponentesLexicos.epsilon: 
                            self.pilaTAS.append(auxTAS)
                        if auxNodo != None and auxTAS != ComponentesLexicos.epsilon:
                            self.pilaNodos.append(auxNodo)
                else:
                    raise ErrorSintactico