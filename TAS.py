# -*- coding: utf-8 -*-

import AnalizadorLexico as s
from ComponentesLexicos import *

TAS = {
    (S, leer): [Z, A],
    (S, escribir): [Z, A],
    (S, id): [Z, A],
    (A, puntoycoma): [puntoycoma, Z, A],
    (A, peso): [epsilon],
    (Z, leer): [leer, parentesisAbre, cadena, coma, id, parentesisCierra],
    (Z, escribir): [escribir, parentesisAbre, cadena, coma, Q, H, N, parentesisCierra],
    (Z, id): [id, igual, Q, H, N],
    (N, puntoycoma): [epsilon],
    (N, parentesisCierra): [epsilon],
    (N, mas): [mas, Q, H, N],
    (N, menos): [menos, Q, H, N],
    (N, peso): [epsilon],
    (H, puntoycoma): [epsilon],
    (H, parentesisCierra): [epsilon],
    (H, mas): [epsilon],
    (H, menos): [epsilon],
    (H, por): [por, Q, H],
    (H, dividido): [dividido, Q, H],
    (H, peso): [epsilon],
    (Q, parentesisAbre): [parentesisAbre, Q, H, N, parentesisCierra],
    (Q, id): [id],
    (Q, real): [real]
}
