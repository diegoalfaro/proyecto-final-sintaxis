# -*- coding: utf-8 -*-

# Terminales: expresiones

id = "id"
cadena = "cadena"
real = "real"

expresiones = {
    id,
    cadena,
    real,
}

# Terminales: simbolos

corcheteAbre = "["
corcheteCierra = "]"
llaveAbre = "{"
llaveCierra = "}"
parentesisAbre = "("
parentesisCierra = ")"
puntoycoma = ";"
coma = ","
punto = "."
mas = "+"
menos = "-"
por = "*"
dividido = "/"
igual = "="
diferente = "<>"
mayor = ">"
menor = "<"
mayorIgual = ">="
menorIgual = "<="
potencia = "^2"
negacion = "~"

simbolos = {
    corcheteAbre,
    corcheteCierra,
    llaveAbre,
    llaveCierra,
    parentesisAbre,
    parentesisCierra,
    puntoycoma,
    coma,
    punto,
    mas,
    menos,
    por,
    dividido,
    igual,
    diferente,
    mayor,
    menor,
    mayorIgual,
    menorIgual,
    potencia,
    negacion,
}

# Terminales: palabras reservadas

ejecutar = "ejecutar"
escribir = "escribir"
leer = "leer"
sino = "sino"
si = "si"
mientras = "mientras"
retornar = "retornar"
verdadero = "verdadero"
falso = "falso"
y = "y"
o = "o"
raiz = "raiz"

palabrasReservadas = [
    ejecutar,
    escribir,
    leer,
    sino,
    si,
    mientras,
    retornar,
    verdadero,
    falso,
    y,
    o,
    raiz,
]

# Terminales: especiales

epsilon = "epsilon"
peso = "$"
errorLexico = "ErrorLexico"

especiales = {
    epsilon,
    peso,
    errorLexico
}

# Terminales

terminales = expresiones.union(simbolos).union(palabrasReservadas).union(especiales)

# Variables

PROGRAMA = "PROGRAMA"
FUNCION = "FUNCION"
OTRAFUNCION = "OTRAFUNCION"
PARAMETROS = "PARAMETROS"
PARAMETRO = "PARAMETRO"
OTROPARAMETRO = "OTROPARAMETRO"
CUERPO = "CUERPO"
LISTASENTENCIAS = "LISTASENTENCIAS"
SENTENCIA = "SENTENCIA"
ASIGNACION = "ASIGNACION"
CONDICIONAL = "CONDICIONAL"
SINO = "SINO"
CICLO = "CICLO"
LECTURA = "LECTURA"
ESCRITURA = "ESCRITURA"
EJECUCION = "EJECUCION"
CONDICION = "CONDICION"
RETORNO = "RETORNO"
ARGUMENTOS = "ARGUMENTOS"
F = "F"
G = "G"
K = "K"
EXPARIT = "EXPARIT"
J = "J"
N = "N"
M = "M"
R = "R"
CONDICION = "CONDICION"
T = "T"
S = "S"
W = "W"
V = "V"
COMPARACION = "COMPARACION"
OPERADOR = "OPERADOR"

variables = {
    PROGRAMA,
    FUNCION,
    OTRAFUNCION,
    PARAMETROS,
    PARAMETRO,
    OTROPARAMETRO,
    CUERPO,
    LISTASENTENCIAS,
    SENTENCIA,
    ASIGNACION,
    CONDICIONAL,
    SINO,
    CICLO,
    LECTURA,
    ESCRITURA,
    EJECUCION,
    CONDICION,
    RETORNO,
    ARGUMENTOS,
    F,
    G,
    K,
    EXPARIT,
    J,
    N,
    M,
    R,
    CONDICION,
    T,
    S,
    W,
    V,
    COMPARACION,
    OPERADOR,
}