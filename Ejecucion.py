
from Arbol import Nodo
import ComponentesLexicos

def evaluarPrograma(arbol: Nodo, ts: dict):
    def obtenerFunciones(arbol: Nodo):
        funciones = [arbol.hijos[0]]
        if (arbol.hijos[1].hijos[0].getDato() != ComponentesLexicos.epsilon):
            funciones.extend(obtenerFunciones(arbol.hijos[1]))
        return funciones
    def obtenerNombreFuncionDesdeFuncion(arbol: Nodo):
        return arbol.hijos[0].hijos[0].getDato()
    funciones = obtenerFunciones(arbol)
    for funcion in funciones:
        ts[obtenerNombreFuncionDesdeFuncion(funcion)] = funcion
    evaluarFuncion(ts['principal'], ts)

def evaluarFuncion(arbol: Nodo, ts: dict):
    def obtenerListaSentenciasDesdeFuncion(arbol: Nodo):
        return arbol.hijos[4].hijos[1]
    listaSentencias = obtenerListaSentenciasDesdeFuncion(arbol)
    return evaluarListaSentencias(listaSentencias, ts)

def evaluarListaSentencias(arbol: Nodo, ts: dict):
    if arbol.hijos[0].getDato() != ComponentesLexicos.epsilon:
        evaluarSentencia(arbol.hijos[0], ts)
    if len(arbol.hijos) >= 3 and arbol.hijos[2].hijos[0].getDato() != ComponentesLexicos.epsilon:
        evaluarListaSentencias(arbol.hijos[2], ts)

def evaluarA(arbol: Nodo, ts: dict):
    if len(arbol.hijos)>=1 and arbol.hijos[0].getDato()== ComponentesLexicos.puntoycoma:
        evaluarSentencia(arbol.hijos[1] ,ts)
        evaluarA(arbol.hijos[2] ,ts)

def evaluarSentencia(arbol: Nodo, ts: dict):
    if len(arbol.hijos)>=1 and arbol.hijos[0].getDato() == ComponentesLexicos.LECTURA:
        print(arbol.hijos[0].hijos[2].hijos[0].getDato()[1:-1], end='')
        ts[arbol.hijos[0].hijos[4].hijos[0].getDato()] = input()
    elif len(arbol.hijos)>=1 and arbol.hijos[0].getDato() == ComponentesLexicos.ESCRITURA:
        print(arbol.hijos[0].hijos[2].hijos[0].getDato()[1:-1], end='')
        res = evaluarExprArit(arbol.hijos[0].hijos[4], ts)
        res = evaluarH(arbol.hijos[0].hijos[5], ts, res)
        res = evaluarN(arbol.hijos[0].hijos[6], ts, res)
        print(res)
    elif len(arbol.hijos)>=1 and arbol.hijos[0].getDato() == ComponentesLexicos.ASIGNACION:
        res = evaluarExprArit(arbol.hijos[0].hijos[2], ts)
        res = evaluarH(arbol.hijos[0].hijos[3], ts, res)
        res = evaluarN(arbol.hijos[0].hijos[4], ts, res)
        ts[arbol.hijos[0].hijos[0].hijos[0].getDato()] = str(res)
    elif len(arbol.hijos)>=1 and arbol.hijos[0].getDato() == ComponentesLexicos.CONDICIONAL:
        if evaluarCondicion(arbol.hijos[0].hijos[2], ts):
            evaluarListaSentencias(arbol.hijos[0].hijos[4].hijos[1], ts)
        elif arbol.hijos[0].hijos[5].hijos[0].getDato() != ComponentesLexicos.epsilon:
            evaluarListaSentencias(arbol.hijos[0].hijos[5].hijos[1].hijos[1], ts)
    elif len(arbol.hijos)>=1 and arbol.hijos[0].getDato() == ComponentesLexicos.CICLO:
        while evaluarCondicion(arbol.hijos[0].hijos[2], ts):
            evaluarListaSentencias(arbol.hijos[0].hijos[4].hijos[1], ts)

def evaluarCondicion(arbol, ts):
    if arbol.hijos[0].getDato() == ComponentesLexicos.verdadero:
        return True
    elif arbol.hijos[0].getDato() == ComponentesLexicos.falso:
        return False
    else:
        return False

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

def evaluarH(arbol, ts, res: int):
    if len(arbol.hijos)>=1 and arbol.hijos[0].getDato() == ComponentesLexicos.por:
        res1 = evaluarExprArit(arbol.hijos[1], ts)
        res = res * evaluarH(arbol.hijos[2], ts, res1)
    elif len(arbol.hijos)>=1 and arbol.hijos[0].getDato() == ComponentesLexicos.dividido:
        res2 = evaluarExprArit(arbol.hijos[1], ts)
        res = res / evaluarH(arbol.hijos[2], ts, res2)
    return res

def evaluarExprArit(arbol: Nodo, ts: dict):
    if len(arbol.hijos)>=1 and arbol.hijos[0].getDato() == ComponentesLexicos.id:
        id = arbol.hijos[0].hijos[0].getDato()
        return float(ts[id] if id in ts.keys() else 0)
    elif len(arbol.hijos)>=1 and arbol.hijos[0].getDato() == ComponentesLexicos.real:
        numero = arbol.hijos[0].hijos[0].getDato()
        return float(numero)
    elif len(arbol.hijos)>=1 and arbol.hijos[0].getDato() == ComponentesLexicos.parentesisAbre:
        res = evaluarExprArit(arbol.hijos[1], ts)
        res = evaluarH(arbol.hijos[2], ts, res)
        res = evaluarN(arbol.hijos[3], ts, res)
        return res