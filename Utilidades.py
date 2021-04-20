# -*- coding: utf-8 -*-

import sys

def modoDebug() -> bool:
    gettrace = getattr(sys, 'gettrace', lambda : None) 
    return gettrace() is not None