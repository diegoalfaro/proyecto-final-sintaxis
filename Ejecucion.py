
from Arbol import Nodo
import ComponentesLexicos
from Errores import ErrorEjecucion

def evaluarPrograma(arbol: Nodo, ts: dict):
    funcion = arbol.hijos[0]
    otraFuncion = arbol.hijos[1]
    evaluarFuncion(funcion, ts)
    evaluarOtraFuncion(otraFuncion, ts)   
    if ('principal' in ts.keys()):
        funcion = ts['principal']
        listaSentencias = funcion.hijos[4].hijos[1]
        evaluarListaSentencias(listaSentencias, ts)
    else:
        raise ErrorEjecucion

def evaluarFuncion(arbol: Nodo, ts: dict):
    id = arbol.hijos[0].hijos[0].getDato()
    ts[id] = arbol

def evaluarOtraFuncion(arbol: Nodo, ts: dict):
    if arbol.hijos[0].getDato() != ComponentesLexicos.epsilon:
        evaluarFuncion(arbol.hijos[0], ts)
        evaluarOtraFuncion(arbol.hijos[1], ts)

def evaluarListaSentencias(arbol: Nodo, ts: dict):
    if arbol.hijos[0].getDato() != ComponentesLexicos.epsilon:
        evaluarSentencia(arbol.hijos[0], ts)
        if arbol.hijos[0].getDato() == ComponentesLexicos.RETORNO:
            return evaluarRetorno(arbol.hijos[0], ts)
        else:
            return evaluarListaSentencias(arbol.hijos[2], ts)

def evaluarSentencia(arbol: Nodo, ts: dict):
    sentencia = arbol.hijos[0]
    tipoSentencia = sentencia.getDato()
    if tipoSentencia == ComponentesLexicos.LECTURA:
        evaluarLectura(sentencia, ts)
    elif tipoSentencia == ComponentesLexicos.ESCRITURA:
        evaluarEscritura(sentencia, ts)
    elif tipoSentencia == ComponentesLexicos.ASIGNACION:
        evaluarAsignacion(sentencia, ts)
    elif tipoSentencia == ComponentesLexicos.CONDICIONAL:
        evaluarCondicional(sentencia, ts)
    elif tipoSentencia == ComponentesLexicos.CICLO:
        evaluarCiclo(sentencia, ts)
    elif tipoSentencia == ComponentesLexicos.EJECUCION:
        return evaluarEjecucion(sentencia, ts)

def evaluarLectura(arbol: Nodo, ts: dict):
    id = arbol.hijos[4].hijos[0].getDato()
    cadena = arbol.hijos[2].hijos[0].getDato()
    escritura = cadena[1:-1]
    ts[id] = input(escritura)

def evaluarEscritura(arbol: Nodo, ts: dict):
    cadena = arbol.hijos[2].hijos[0].getDato()
    argumentos = arbol.hijos[3]
    listaDeArgumentos = [str(parametro) for parametro in evaluarArgumentos(argumentos, ts)]
    escritura = cadena[1:-1] + " ".join(listaDeArgumentos)
    print(escritura)

def evaluarAsignacion(arbol: Nodo, ts: dict):
    id = arbol.hijos[0].hijos[0].getDato()
    exparit = arbol.hijos[2]
    valor = evaluarExparit(exparit, ts)
    ts[id] = valor

def evaluarCondicional(arbol: Nodo, ts: dict):
    condicion = arbol.hijos[2]
    listaSentencias = arbol.hijos[4].hijos[1]
    sino = arbol.hijos[5]
    if evaluarCondicion(condicion, ts):
        evaluarListaSentencias(listaSentencias, ts)
    else:
        evaluarSino(sino, ts)

def evaluarSino(arbol: Nodo, ts: dict):
    if arbol.hijos[0].getDato() != ComponentesLexicos.epsilon:
        listaSentencias = arbol.hijos[1].hijos[1]
        evaluarListaSentencias(listaSentencias, ts)

def evaluarCiclo(arbol: Nodo, ts: dict):
    condicion = arbol.hijos[2]
    listaSentencias = arbol.hijos[4].hijos[1]
    while evaluarCondicion(condicion, ts):
        evaluarListaSentencias(listaSentencias, ts)

def evaluarEjecucion(arbol: Nodo, ts: dict):
    id = arbol.hijos[2].hijos[0].getDato()
    if id in ts:
        funcion = ts[id]
        parametros = evaluarParametros(funcion.hijos[2], ts)
        argumentos = dict(zip(parametros, evaluarArgumentos(arbol.hijos[3], ts)))
        tablaSimbolosFuncion = ts.copy()
        tablaSimbolosFuncion.update(argumentos)
        listaSentencias = funcion.hijos[4].hijos[1]
        return evaluarListaSentencias(listaSentencias, tablaSimbolosFuncion)
    else:
        raise ErrorEjecucion

def evaluarParametros(arbol: Nodo, ts: dict):
    if arbol.hijos[0].getDato() != ComponentesLexicos.epsilon:
        parametro = evaluarParametro(arbol.hijos[0], ts)
        otroParametro = evaluarOtroParametro(arbol.hijos[0].hijos[1], ts)
        return [parametro] + otroParametro
    else:
        return []

def evaluarParametro(arbol: Nodo, ts: dict):
    return arbol.hijos[0].hijos[0].getDato()

def evaluarOtroParametro(arbol: Nodo, ts: dict):
    if arbol.hijos[0].getDato() != ComponentesLexicos.epsilon:
        id = arbol.hijos[1].hijos[0].getDato()
        otroParametro = evaluarOtroParametro(arbol.hijos[2], ts)
        return [id] + otroParametro
    else:
        return []

def evaluarRetorno(arbol: Nodo, ts: dict):
    exparit = arbol.hijos[2]
    return evaluarExparit(exparit, ts)

def evaluarExparit(arbol: Nodo, ts: dict):
    resultadoJ = evaluarJ(arbol.hijos[0], ts)
    resultadoK = evaluarK(arbol.hijos[1], ts, resultadoJ)
    return resultadoK

def evaluarJ(arbol: Nodo, ts: dict):
    resultadoM = evaluarM(arbol.hijos[0], ts)
    resultadoN = evaluarN(arbol.hijos[1], ts, resultadoM)
    return resultadoN

def evaluarK(arbol: Nodo, ts: dict, entrada: float):
    if arbol.hijos[0].getDato() != ComponentesLexicos.epsilon:
        resultadoJ = evaluarJ(arbol.hijos[1], ts)
        resultadoK = evaluarK(arbol.hijos[2], ts, entrada)
        if arbol.hijos[0].getDato() == ComponentesLexicos.mas:
            return resultadoJ + resultadoK
        elif arbol.hijos[0].getDato() == ComponentesLexicos.menos:
            return resultadoJ - resultadoK
    else:
        return entrada

def evaluarM(arbol: Nodo, ts: dict):
    resultadoF = evaluarF(arbol.hijos[0], ts)
    resultadoR = evaluarR(arbol.hijos[1], ts, resultadoF)
    return resultadoR

def evaluarN(arbol: Nodo, ts: dict, entrada: float):
    if arbol.hijos[0].getDato() != ComponentesLexicos.epsilon:
        resultadoM = evaluarM(arbol.hijos[1], ts)
        resultadoN = evaluarN(arbol.hijos[2], ts, entrada)
        if arbol.hijos[0].getDato() == ComponentesLexicos.por:
            return resultadoM * resultadoN
        elif arbol.hijos[0].getDato() == ComponentesLexicos.dividido:
            return resultadoM / resultadoN
    else:
        return entrada

def evaluarF(arbol: Nodo, ts: dict):
    if arbol.hijos[0].getDato() == ComponentesLexicos.EJECUCION:
        return evaluarEjecucion(arbol.hijos[0], ts)
    elif arbol.hijos[0].getDato() == ComponentesLexicos.id:
        id = arbol.hijos[0].hijos[0].getDato()
        return float(ts[id] if id in ts.keys() else 0)
    elif arbol.hijos[0].getDato() == ComponentesLexicos.real:
        numero = arbol.hijos[0].hijos[0].getDato()
        return float(numero)

def evaluarR(arbol: Nodo, ts: dict, entrada: float):
    if arbol.hijos[0].getDato() != ComponentesLexicos.epsilon:
        return pow(entrada)
    else:
        return entrada

def evaluarG(arbol: Nodo, ts: dict, entrada: list):
    if arbol.hijos[0].getDato() != ComponentesLexicos.epsilon:
        resultadoF = evaluarF(arbol.hijos[1], ts)
        resultadoG = evaluarG(arbol.hijos[2], ts, [resultadoF])
        return entrada + resultadoG
    else:
        return entrada

def evaluarArgumentos(arbol: Nodo, ts: dict):
    if arbol.hijos[0].getDato() != ComponentesLexicos.epsilon:
        resultadoF = evaluarF(arbol.hijos[1], ts)
        resultadoG = evaluarG(arbol.hijos[2], ts, [resultadoF])
        return resultadoG
    else:
        return []

def evaluarCondicion(arbol: Nodo, ts: dict):
    resultadoS = evaluarS(arbol.hijos[0], ts)
    resultadoT = evaluarT(arbol.hijos[1], ts, resultadoS)
    return resultadoT

def evaluarS(arbol: Nodo, ts: dict):
    resultadoV = evaluarV(arbol.hijos[0], ts)
    resultadoW = evaluarW(arbol.hijos[1], ts, resultadoV)
    return resultadoW

def evaluarT(arbol: Nodo, ts: dict, entrada: bool):
    if arbol.hijos[0].getDato() != ComponentesLexicos.epsilon:
        resultadoS = evaluarS(arbol.hijos[1], ts)
        resultadoT = evaluarT(arbol.hijos[2], ts, entrada)
        if arbol.hijos[0].getDato() == ComponentesLexicos.o:
            return resultadoS or resultadoT
    else:
        return entrada

def evaluarV(arbol: Nodo, ts: dict):
    if (arbol.hijos[0].getDato() == ComponentesLexicos.verdadero):
        return True
    if (arbol.hijos[0].getDato() == ComponentesLexicos.falso):
        return False
    if (arbol.hijos[0].getDato() == ComponentesLexicos.corcheteAbre):
        condicion = arbol.hijos[1]
        return evaluarCondicion(condicion, ts)
    if (arbol.hijos[0].getDato() == ComponentesLexicos.negacion):
        condicion = arbol.hijos[2]
        return not evaluarCondicion(condicion, ts)
    if (arbol.hijos[0].getDato() == ComponentesLexicos.COMPARACION):
        comparacion = arbol.hijos[0]
        return evaluarComparacion(comparacion, ts)

def evaluarW(arbol: Nodo, ts: dict, entrada: bool):
    if arbol.hijos[0].getDato() != ComponentesLexicos.epsilon:
        resultadoV = evaluarV(arbol.hijos[1], ts)
        resultadoW = evaluarW(arbol.hijos[2], ts, entrada)
        if arbol.hijos[0].getDato() == ComponentesLexicos.y:
            return resultadoV and resultadoW
    else:
        return entrada

def evaluarComparacion(arbol: Nodo, ts: dict):
    exparitA = evaluarExparit(arbol.hijos[0], ts)
    exparitB = evaluarExparit(arbol.hijos[2], ts)
    simbolo = arbol.hijos[1].hijos[0].getDato()
    if simbolo == ComponentesLexicos.igual:
        return exparitA == exparitB
    elif simbolo == ComponentesLexicos.diferente:
        return exparitA != exparitB
    elif simbolo == ComponentesLexicos.mayor:
        return exparitA > exparitB
    elif simbolo == ComponentesLexicos.menor:
        return exparitA < exparitB
    elif simbolo == ComponentesLexicos.mayorIgual:
        return exparitA >= exparitB
    elif simbolo == ComponentesLexicos.menorIgual:
        return exparitA <= exparitB