# -*- coding: utf-8 -*-

import sys
from os import path
import time

from AnalizadorLexico import AnalizadorLexico
from AnalizadorSintactico import AnalizadorSintactico
from Ejecucion import evaluarPrograma
from Utilidades import modoDebug
from Textos import ERROR_GENERICO, ERROR_LEXICO, ERROR_SINTACTICO
from Errores import ErrorLexico, ErrorSintactico

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
            tablaSimbolos = {}
            analizadorLexico = AnalizadorLexico(archivo, tablaSimbolos)
            analizadorSintactico = AnalizadorSintactico(analizadorLexico)
            if modoDebug():
                print("Analizamos lexica y sintacticamente el programa...")
            arbol = analizadorSintactico.analizar()
            if modoDebug():
                print(arbol)
            if modoDebug():
                print("Ejecutamos el programa...")
            evaluarPrograma(arbol, tablaSimbolos)
        except ErrorLexico as err:
            print(ERROR_LEXICO.format(linea=err.linea, posicion=err.posicion))
            if not modoDebug():
                exit(1)
        except ErrorSintactico:
            print(ERROR_SINTACTICO)
            if not modoDebug():
                exit(1)
        except Exception as err:
            print(ERROR_GENERICO)
            if not modoDebug():
                exit(1)
        finally:
            archivo.close()
            if modoDebug():
                print("Se queda el programa esperando porque esta en modo DEBUG")
                while True:
                    time.sleep(5)
            exit(0)