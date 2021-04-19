# -*- coding: utf-8 -*-

class Nodo:

    def __init__(self, dato):
        self.dato = dato
        self.hijos = []
        self.padre = None

    def agregarHijo(self, hijo):
        hijo.padre = self
        self.hijos.append(hijo)
    
    def esHoja(self):
        if not len(self.hijos):
            return True
        else:
            return False
    
    def esRaiz(self):
        if self.padre == None:
            return True
        else:
            return False
    
    def getPadre(self):
        return self.padre
    
    def getHijos(self):
        return self.hijos
    
    def getDato(self):
        return self.dato

    def __repr__(self, mem=''):
        dato = self.getDato()
        ret = dato + '\n'
        if self.esRaiz():
            ret = '\n' + dato + '\n'
        esp = ''
        esq = ''
        hijos = self.getHijos()
        if self.esRaiz():
            for hijo in hijos:
                if hijo != hijos[-1]:
                    esq = '╠═'
                    esp = '║ '
                else:
                    esq = '╚═'
                    esp = '  '
                ret += mem + esq + hijo.__repr__(esp)
        else:
            if not self.esHoja():  # si tengo hijos
                if self == self.getPadre().getHijos()[-1]:
                    esp = '  '
                else:
                    esp = '║ '
                for hijo in hijos:
                    if hijo == hijos[-1]:
                        esq = '╚═'
                        esp = '  '
                    else:
                        esq = '╠═'
                        esp = '║ '
                    ret += mem + esq + hijo.__repr__(mem + esp)
        return ret
