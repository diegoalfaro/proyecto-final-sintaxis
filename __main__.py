# -*- coding: utf-8 -*-

import sys
from os import path
import time

from AnalizadorLexico import AnalizadorLexico
from AnalizadorSintactico import AnalizadorSintactico
from TablaDeSimbolos import TablaDeSimbolos
from Ejecucion import evaluarS

def debugger_is_active() -> bool:
    """Return if the debugger is currently active"""
    gettrace = getattr(sys, 'gettrace', lambda : None) 
    return gettrace() is not None

if __name__ == '__main__':
    if (len(sys.argv) < 2):
        print("Debe pasar como parámetro el archivo a ejecutar")
        exit(1)
    rutaArchivoCodigoFuente = str(sys.argv[1])
    if ((not path.exists(rutaArchivoCodigoFuente)) or (not path.isfile(rutaArchivoCodigoFuente))):
        print("No se encontró el archivo")
        exit(1)
    else:
        try:
            archivo = open(rutaArchivoCodigoFuente)
            tablaSimbolos = TablaDeSimbolos()
            analizadorLexico = AnalizadorLexico(archivo, tablaSimbolos)
            analizadorSintactico = AnalizadorSintactico(analizadorLexico)
            arbol = analizadorSintactico.analizar()
            evaluarS(arbol, tablaSimbolos)
        finally:
            archivo.close()
            if debugger_is_active():
                print("Se queda el programa esperando porque esta en modo DEBUG")
                while True:
                    time.sleep(5)
            exit(0)