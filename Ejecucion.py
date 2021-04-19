# -*- coding: utf-8 -*-

from TablaDeSimbolos import TablaDeSimbolos
from Arbol import Nodo
import ComponentesLexicos

#< S > -> < sentencia > < A >
def evaluarS(arbol: Nodo, ts: TablaDeSimbolos):
    evaluarSentencia(arbol.hijos[0], ts)
    evaluarA(arbol.hijos[1], ts)

#< A > -> ; < sentencia> <A> | ε
def evaluarA(arbol: Nodo, ts: TablaDeSimbolos):
    if len(arbol.hijos)>=1 and arbol.hijos[0].getDato()== ComponentesLexicos.puntoycoma:
        evaluarSentencia(arbol.hijos[1] ,ts)
        evaluarA(arbol.hijos[2] ,ts)

#<sentencia> ::= leer(cadena, id) | escribir(texto, < expr_arit_c > < H > < N > ) | id = < expr_arit_c > < H > < N >
def evaluarSentencia(arbol: Nodo, ts: TablaDeSimbolos):
    if len(arbol.hijos)>=1 and arbol.hijos[0].getDato()== ComponentesLexicos.leer:
        if len(arbol.hijos[2].hijos) == 1:
            print(arbol.hijos[2].hijos[0].getDato()[1:-1], end='')
        ts.actualizarTS(arbol.hijos[4].hijos[0].getDato(), input())
    elif len(arbol.hijos)>=1 and arbol.hijos[0].getDato() == ComponentesLexicos.escribir:
        if len(arbol.hijos[2].hijos) == 1:
            print(arbol.hijos[2].hijos[0].getDato()[1:-1], end='')
        res = evaluarExprArit(arbol.hijos[4], ts)
        res = evaluarH(arbol.hijos[5], ts, res)
        res = evaluarN(arbol.hijos[6], ts, res)
        print(res)
    else:
        res = evaluarExprArit(arbol.hijos[2], ts)
        res = evaluarH(arbol.hijos[3], ts, res)
        res = evaluarN(arbol.hijos[4], ts, res)
        ts.actualizarTS(arbol.hijos[0].hijos[0].getDato(), str(res))

#< N >::= + < expr_arit_c > < H > < N > | - < expr_arit_c > < H > < N > | ε
def evaluarN(arbol, ts, res):
    if len(arbol.hijos)>=1 and arbol.hijos[0].getDato() == ComponentesLexicos.mas:
        res1 = evaluarExprArit(arbol.hijos[1], ts)
        res2 = evaluarH(arbol.hijos[2], ts, res1)
        res = res + evaluarN(arbol.hijos[3], ts, res2)
    elif len(arbol.hijos)>=1 and arbol.hijos[0].getDato() == ComponentesLexicos.menos:
        res1 = evaluarExprArit(arbol.hijos[1], ts)
        res2 = evaluarH(arbol.hijos[2], ts, res1)
        res = res - evaluarN(arbol.hijos[3], ts, res2)
    return res

#< H >::= * < expr_arit_c > < H > | / < expr_ar1it_c > < H > | ε
def evaluarH(arbol, ts, res: int):
    if len(arbol.hijos)>=1 and arbol.hijos[0].getDato() == ComponentesLexicos.por:
        res1 = evaluarExprArit(arbol.hijos[1], ts)
        res = res * evaluarH(arbol.hijos[2], ts, res1)
    elif len(arbol.hijos)>=1 and arbol.hijos[0].getDato() == ComponentesLexicos.dividido:
        res2 = evaluarExprArit(arbol.hijos[1], ts)
        res = res / evaluarH(arbol.hijos[2], ts, res2)
    return res

#< expr_arit_c >::=    id | const | ( < expr_arit_c > < H > < N >)
def evaluarExprArit(arbol: Nodo, ts: TablaDeSimbolos):
    if len(arbol.hijos)>=1 and arbol.hijos[0].getDato() == ComponentesLexicos.id:
        return float(ts.devolverIdDato(arbol.hijos[0].hijos[0].getDato()))
    elif len(arbol.hijos)>=1 and arbol.hijos[0].getDato() == ComponentesLexicos.real:
        return float(arbol.hijos[0].hijos[0].getDato())
    elif len(arbol.hijos)>=1 and arbol.hijos[0].getDato() == ComponentesLexicos.parentesisAbre:
        res = evaluarExprArit(arbol.hijos[1], ts)
        res = evaluarH(arbol.hijos[2], ts, res)
        res = evaluarN(arbol.hijos[3], ts, res)
        return res