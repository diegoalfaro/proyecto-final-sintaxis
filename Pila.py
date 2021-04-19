# -*- coding: utf-8 -*-

class Pila(list):

    def empty(self):
        return not len(self)

    def pop(self):
        return list.pop(self) if not self.empty() else None
