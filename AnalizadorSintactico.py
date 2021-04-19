# -*- coding: utf-8 -*-

from TAS import TAS
from Arbol import Nodo
from Pila import Pila
from AnalizadorLexico import AnalizadorLexico
from TablaDeSimbolos import TablaDeSimbolos
import ComponentesLexicos

class AnalizadorSintactico():
    def __init__(self, analizadorLexico: AnalizadorLexico):
        self.analizadorLexico = analizadorLexico
        self.arbol = Nodo(ComponentesLexicos.S) #crea el arbol con raiz S
        self.pila = Pila() #crea pila para apilar lo que contiene un vector de la tas
        self.pila2 = Pila() #crea pila para apilar el nodo del arbol en el que se encuentra un elemento apilado de la primer pila
        self.pila.append(ComponentesLexicos.peso)  # apilamos el simbolo final
        self.pila.append(ComponentesLexicos.S) # apilamos primer Variable
        self.pila2.append(self.arbol)  #apilamos raiz
        self.nodoActual = self.arbol  # el nodo inicial es la raiz

    def analizar(self) -> Nodo:
        (componenteLexico, lexema) = self.analizadorLexico.siguienteComponenteLexico()  #a es un vector con el componente lexico y el lexema en este orden
        resultado = 0 # resultado =0 indica que el analizador Sintactico debe seguir analizando
        while resultado == 0:
            X = self.pila.pop()  #desapila

            if X != ComponentesLexicos.peso:
                self.nodoActual = self.pila2.pop()  #desapila segunda pila y lo asigna a nodo actual

            if X == componenteLexico == ComponentesLexicos.peso:
                resultado = 1 #proceso terminado con exito
            elif X in ComponentesLexicos.terminales: #si X es terminal
                if X == componenteLexico: #y es el componente lexico leido
                    self.nodoActual.agregarHijo(Nodo(lexema)) #se agrega como hijo al nodo actual
                    (componenteLexico, lexema) = self.analizadorLexico.siguienteComponenteLexico() #y se obtiene el siguiente componente
                else:
                    resultado = -1 #error
            elif X in ComponentesLexicos.variables: #si X es variable
                tupla = (X[0], componenteLexico)
                if tupla in TAS:
                    i = 0
                    auxPila = Pila() #se crea dos auxiliares pila
                    auxPila2 = Pila()
                    v = TAS[(X[0], componenteLexico)]
                    while i < len(v) and v[i] != []: #mientras no se pase de rango y no quede vacio
                        self.nodoActual.agregarHijo(Nodo(v[i])) # se agrega el hijo ial arbol
                        nodo = self.nodoActual.getHijos()[-1] #se obtiene su nodo
                        auxPila.append(v[i]) #se apila en la primera pila auxiliar el elemento
                        auxPila2.append(nodo) # se apila en la segunda pila auxiliar el nodo
                        i += 1 #se suma al contador
                    while i >= 0: #mientras sea mayor igual a cero, como un for de i..0
                        aux = auxPila.pop()  #se desapilan en auxiliares las pilas auxiliares
                        aux2 = auxPila2.pop()
                        if aux != None and aux != ComponentesLexicos.epsilon :  #no se apila epsilon
                            self.pila.append(aux) # se apilar los auxiliares de forma que quedan apiladas de manera invertida
                        if aux2 != None and aux != ComponentesLexicos.epsilon:
                            self.pila2.append(aux2)
                        i -= 1 #se descuenta contador
                else:
                    print("Error sintactico")
                    resultado = -1 #error
        return self.arbol #se devuelve el arbol