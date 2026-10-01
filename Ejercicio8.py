from datetime import date, timedelta
from Ejercicio6 import ProductoKwikE

class Nodo:
    def __init__(self, dato, sig=None):
        self._elem = dato
        self._nxt = sig

# 8.2 Iterador simple
class IteradorListaEnlazada:
    def __init__(self, inicio):
        self.actual = inicio

    def __iter__(self):
        return self

    def __next__(self):
        if not self.actual:
            raise StopIteration
        dato = self.actual._elem
        self.actual = self.actual._nxt
        return dato

# 8.1 Lista Enlazada simplificada
class ListaEnlazada:
    def __init__(self):
        self.header = Nodo(0)  # Centinela

    def agregar_al_final(self, dato):
        actual = self.header
        while actual._nxt:
            actual = actual._nxt
        actual._nxt = Nodo(dato)

    def eliminar_por_condicion(self, condicion):
        eliminados = 0
        actual = self.header
        while actual._nxt:
            if condicion(actual._nxt._elem):
                actual._nxt = actual._nxt._nxt
                eliminados += 1
            else:
                actual = actual._nxt
        return eliminados

    def __iter__(self):
        return IteradorListaEnlazada(self.header._nxt)


class KwikEMart:
    def __init__(self):
        self.pasillos = {
            "Bebidas": ListaEnlazada(),
            "Snacks": ListaEnlazada(),
            "Conveniencia": ListaEnlazada()
        }

    def agregar_producto(self, pasillo: str, producto: ProductoKwikE):
        if pasillo not in self.pasillos:
            self.pasillos[pasillo] = ListaEnlazada()
        self.pasillos[pasillo].agregar_al_final(producto)

    def buscar_producto_por_id(self, id_producto: int):
        for pasillo, lista in self.pasillos.items():
            for prod in lista:
                if prod.id_producto == id_producto:
                    return pasillo, prod
        return None, None

    def remover_producto(self, id_producto: int):
        pasillo, prod = self.buscar_producto_por_id(id_producto)
        if prod:
            self.pasillos[pasillo].eliminar_por_condicion(lambda p: p.id_producto == id_producto)
            return True
        return False

    def actualizar_stock_producto(self, id_producto: int, nuevo_stock: int):
        _, prod = self.buscar_producto_por_id(id_producto)
        if prod:
            prod.stock = nuevo_stock
            return True
        return False

    def desechar_productos_por_expiracion(self):
        manana = date.today() + timedelta(days=1)
        total = 0
        for lista in self.pasillos.values():
            total += lista.eliminar_por_condicion(lambda p: p.fecha_vencimiento <= manana)
        return total