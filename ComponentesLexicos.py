# -*- coding: utf-8 -*-

# Terminales

cadena = "cadena"
coma = ","
corcheteAbre = "["
corcheteCierra = "]"
dividido = "/"
epsilon = "epsilon"
errorLexico = "ErrorLexico"
escribir = "escribir"
id = "id"
igual = "="
leer = "leer"
llaveAbre = "{"
llaveCierra = "}"
mas = "+"
menos = "-"
parentesisAbre = "("
parentesisCierra = ")"
peso = "$"
por = "*"
punto = "."
puntoycoma = ";"
real = "real"
si = "si"
sino = "sino"
mientras = "mientras"
verdadero = "verdadero"
falso = "falso"

palabrasReservadas = [
    sino,
    si,
    mientras,
    escribir,
    leer,
    verdadero,
    falso
]

terminales = {
    cadena,
    coma,
    corcheteAbre,
    corcheteCierra,
    dividido,
    epsilon,
    errorLexico,
    escribir,
    id,
    igual,
    leer,
    llaveAbre,
    llaveCierra,
    mas,
    menos,
    mientras,
    parentesisAbre,
    parentesisCierra,
    parentesisCierra,
    peso,
    por,
    punto,
    puntoycoma,
    real,
    si,
    sino,
    verdadero,
    falso
}

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
CONDICION = "CONDICION"
A = "A"
Q = "Q"
Z = "Z"
H = "H"
N = "N"

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
    CONDICION,
    A,
    Q,
    Z,
    H,
    N,
}