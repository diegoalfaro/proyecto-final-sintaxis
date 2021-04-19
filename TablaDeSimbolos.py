# -*- coding: utf-8 -*-

class TablaDeSimbolos(dict):

    def devolverIdDato(self, id: str): #devuelve el valor del correspondiente id en la diccionario si se encuentra
        return self[id] if self.get(id) != None else None

    def actualizarTS(self, id: str, res: str):  #modifica el valor del id en la tabla de simbolo, si no se encuentra lo crea
        self[id] = res
        return self
