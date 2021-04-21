#-*- coding: utf-8 -*-

import AnalizadorLexico as s
from ComponentesLexicos import *

TAS = {

    #PROGRAMA
    (PROGRAMA, id): [FUNCION, OTRAFUNCION],

    #OTRAFUNCION
    (OTRAFUNCION, id): [FUNCION, OTRAFUNCION],
    (OTRAFUNCION, peso): [epsilon],

    #FUNCION
    (FUNCION, id): [id, parentesisAbre, PARAMETROS, parentesisCierra, CUERPO],

    #PARAMETROS
    (PARAMETROS, id): [PARAMETRO],
    (PARAMETROS, parentesisCierra): [epsilon],

    #PARAMETRO
    (PARAMETRO, id): [id, OTROPARAMETRO],

    #OTROPARAMETRO
    (OTROPARAMETRO, coma): [coma, id, OTROPARAMETRO],
    (OTROPARAMETRO, parentesisCierra): [epsilon],

    #CUERPO
    (CUERPO, llaveAbre): [llaveAbre, LISTASENTENCIAS, llaveCierra],

    #LISTASENTENCIAS
    (LISTASENTENCIAS, id): [SENTENCIA, puntoycoma, LISTASENTENCIAS],
    (LISTASENTENCIAS, leer): [SENTENCIA, puntoycoma, LISTASENTENCIAS],
    (LISTASENTENCIAS, escribir): [SENTENCIA, puntoycoma, LISTASENTENCIAS],
    (LISTASENTENCIAS, ejecutar): [SENTENCIA, puntoycoma, LISTASENTENCIAS],
    (LISTASENTENCIAS, si): [SENTENCIA, puntoycoma, LISTASENTENCIAS],
    (LISTASENTENCIAS, mientras): [SENTENCIA, puntoycoma, LISTASENTENCIAS],
    (LISTASENTENCIAS, retornar): [RETORNO, puntoycoma],
    (LISTASENTENCIAS, llaveCierra): [epsilon],

    #SENTENCIA
    (SENTENCIA, id): [ASIGNACION],
    (SENTENCIA, leer): [LECTURA],
    (SENTENCIA, escribir): [ESCRITURA],
    (SENTENCIA, ejecutar): [EJECUCION],
    (SENTENCIA, si): [CONDICIONAL],
    (SENTENCIA, mientras): [CICLO],

    #ASIGNACION
    (ASIGNACION, id): [id, igual, EXPARIT],

    #CONDICIONAL
    (CONDICIONAL, si): [si, parentesisAbre, CONDICION, parentesisCierra, CUERPO, SINO],

    #SINO
    (SINO, sino): [sino, CUERPO],
    (SINO, puntoycoma): [epsilon],

    #CICLO
    (CICLO, mientras): [mientras, parentesisAbre, CONDICION, parentesisCierra, CUERPO],

    #LECTURA
    (LECTURA, leer): [leer, parentesisAbre, cadena, coma, id, parentesisCierra],

    #RETORNO
    (RETORNO, retornar): [retornar, parentesisAbre, EXPARIT, parentesisCierra],

    #EJECUCION
    (EJECUCION, ejecutar): [ejecutar, parentesisAbre, id, ARGUMENTOS, parentesisCierra],

    #ESCRITURA
    (ESCRITURA, escribir): [escribir, parentesisAbre, cadena, ARGUMENTOS, parentesisCierra],

    #ARGUMENTOS
    (ARGUMENTOS, coma): [coma, EXPARIT, ARGUMENTOS],
    (ARGUMENTOS, parentesisCierra): [epsilon],

    #EXPARIT
    (EXPARIT, ejecutar): [J, K],
    (EXPARIT, id): [J, K],
    (EXPARIT, real): [J, K],
    (EXPARIT, raiz): [J, K],

    #F
    (F, ejecutar): [EJECUCION],
    (F, id): [id],
    (F, real): [real],

    #K
    (K, parentesisCierra): [epsilon],
    (K, puntoycoma): [epsilon],
    (K, mas): [mas, J, K],
    (K, menos): [menos, J, K],
    (K, igual): [epsilon],
    (K, diferente): [epsilon],
    (K, mayor): [epsilon],
    (K, menor): [epsilon],
    (K, mayorIgual): [epsilon],
    (K, menorIgual): [epsilon],
    (K, corcheteCierra): [epsilon],
    (K, coma): [epsilon],

    #J
    (J, ejecutar): [M, N],
    (J, id): [M, N],
    (J, raiz): [M, N],
    (J, real): [M, N],

    #N
    (N, parentesisCierra): [epsilon],
    (N, puntoycoma): [epsilon],
    (N, mas): [epsilon],
    (N, menos): [epsilon],
    (N, por): [por, M, N],
    (N, dividido): [dividido, M, N],
    (N, igual): [epsilon],
    (N, diferente): [epsilon],
    (N, mayor): [epsilon],
    (N, menor): [epsilon],
    (N, mayorIgual): [epsilon],
    (N, menorIgual): [epsilon],
    (N, corcheteCierra): [epsilon],
    (N, coma): [epsilon],

    #M
    (M, ejecutar): [F, R],
    (M, id): [F, R],
    (M, raiz): [raiz, parentesisAbre, M, parentesisCierra],
    (M, real): [F, R],

    #R
    (R, parentesisCierra): [epsilon],
    (R, puntoycoma): [epsilon],
    (R, mas): [epsilon],
    (R, menos): [epsilon],
    (R, por): [epsilon],
    (R, dividido): [epsilon],
    (R, potencia): [potencia, R],
    (R, igual): [epsilon],
    (R, diferente): [epsilon],
    (R, mayor): [epsilon],
    (R, menor): [epsilon],
    (R, mayorIgual): [epsilon],
    (R, menorIgual): [epsilon],
    (R, corcheteCierra): [epsilon],
    (R, coma): [epsilon],

    #CONDICION
    (CONDICION, id): [S, T],
    (CONDICION, raiz): [S, T],
    (CONDICION, negacion): [S, T],
    (CONDICION, verdadero): [S, T],
    (CONDICION, falso): [S, T],
    (CONDICION, corcheteAbre): [S, T],
    (CONDICION, real): [S, T],

    #T
    (T, parentesisCierra): [epsilon],
    (T, o): [o, S, T],
    (T, corcheteCierra): [epsilon],

    #S
    (S, id): [V, W],
    (S, raiz): [V, W],
    (S, negacion): [V, W],
    (S, verdadero): [V, W],
    (S, falso): [V, W],
    (S, corcheteAbre): [V, W],
    (S, real): [V, W],

    #W
    (W, parentesisCierra): [epsilon],
    (W, o): [epsilon],
    (W, y): [y, V, W],
    (W, corcheteCierra): [epsilon],

    #V
    (V, id): [COMPARACION],
    (V, raiz): [COMPARACION],
    (V, negacion): [negacion, corcheteAbre, CONDICION, corcheteCierra],
    (V, verdadero): [verdadero],
    (V, falso): [falso],
    (V, corcheteAbre): [corcheteAbre, CONDICION, corcheteCierra],
    (V, real): [COMPARACION],

    #COMPARACION
    (COMPARACION, id): [EXPARIT, OPERADOR, EXPARIT],
    (COMPARACION, raiz): [EXPARIT, OPERADOR, EXPARIT],
    (COMPARACION, real): [EXPARIT, OPERADOR, EXPARIT],

    #OPERADOR
    (OPERADOR, igual): [igual],
    (OPERADOR, diferente): [diferente],
    (OPERADOR, mayor): [mayor],
    (OPERADOR, menor): [menor],
    (OPERADOR, mayorIgual): [mayorIgual],
    (OPERADOR, menorIgual): [menorIgual],

}
