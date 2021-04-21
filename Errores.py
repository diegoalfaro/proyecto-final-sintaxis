# -*- coding: utf-8 -*-

class ErrorLexico(Exception):
    def __init__(self, linea: int, posicion: int): 
        self.linea = linea
        self.posicion = posicion

class ErrorSintactico(Exception):
    def __init__(self, terminal: bool, tupla=tuple): 
        self.terminal = terminal
        self.tupla = tupla

class ErrorEjecucion(Exception): ...