from datetime import date, timedelta
from Ejercicio6 import ProductoKwikE

class KwikEMart:
    def __init__(self):
        # un diccionario cuyas claves son las secciones/pasillos
        # y sus valores son listas de objetos ProductoKwikE
        self.pasillos = {
            "Bebidas": [],
            "Snacks": [],
            "Conveniencia": []
        }

    # 1. Añadir un nuevo producto a un pasillo
    def agregar_producto(self, pasillo: str, producto: ProductoKwikE):
        if pasillo in self.pasillos:
            self.pasillos[pasillo].append(producto)
            print(f"Producto '{producto.descripcion}' agregado al pasillo '{pasillo}'.")
        else:
            print(f"El pasillo '{pasillo}' no existe. Creando pasillo y agregando producto...")
            self.pasillos[pasillo] = [producto]

    # Buscar un producto por su ID
    def buscar_producto_por_id(self, id_producto: int):
        for pasillo, lista_productos in self.pasillos.items():
            for prod in lista_productos:
                if prod.id_producto == id_producto:
                    return pasillo, prod
        return None, None

    # 2. Remover un producto del inventario por su ID
    def remover_producto(self, id_producto: int):
        pasillo, producto = self.buscar_producto_por_id(id_producto)
        if producto:
            self.pasillos[pasillo].remove(producto)
            print(f"Producto '{producto.descripcion}' eliminado del inventario ({pasillo}).")
            return True
        print(f"No se encontró ningún producto con ID {id_producto}.")
        return False

    # 3. Actualizar el stock de un producto por su ID
    def actualizar_stock_producto(self, id_producto: int, nuevo_stock: int):
        _, producto = self.buscar_producto_por_id(id_producto)
        if producto:
            producto.stock = nuevo_stock
            print(f"Stock de '{producto.descripcion}' actualizado a {nuevo_stock}.")
            return True
        print(f"No se encontró ningún producto con ID {id_producto}.")
        return False

    # 4. Calcular productos que expiran en las prox 24 horas y removerlos
    def desechar_productos_por_expiracion(self):
        hoy = date.today()
        manana = hoy + timedelta(days=1)
        desechados = 0

        for pasillo, lista_productos in self.pasillos.items():
            # Filtramos manteniendo solo los productos que NO expiran hoy o mañana (24h)
            productos_validos = []
            for prod in lista_productos:
                # Si la fecha de vencimiento es hoy o antes de mañana
                if prod.fecha_vencimiento <= manana:
                    print(f"Apu desechó '{prod.descripcion}' por vencer/vencido.")
                    desechados += 1
                else:
                    productos_validos.append(prod)
            
            # Actualizamos la lista del pasillo
            self.pasillos[pasillo] = productos_validos

        print(f"Total de productos desechados en las próximas 24 horas: {desechados}")
        return desechados