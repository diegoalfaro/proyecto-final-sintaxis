# -*- coding: utf-8 -*-

class ErrorLexico(Exception):
    linea: str
    posicion: int

class ErrorSintactico(Exception): ...