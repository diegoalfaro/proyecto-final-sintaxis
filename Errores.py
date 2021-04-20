# -*- coding: utf-8 -*-

class ErrorLexico(Exception):
    def __init__(self, linea, posicion): 
        self.linea = linea
        self.posicion = posicion

class ErrorSintactico(Exception): ...