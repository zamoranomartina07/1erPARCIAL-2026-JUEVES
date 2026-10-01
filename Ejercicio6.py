from datetime import date

class ProductoKwikE:
    def __init__(self, descripcion: str, id_producto: int, fecha_vencimiento: date, precio: float, stock: int):
        self.descripcion = descripcion
        self.id_producto = id_producto
        self.fecha_vencimiento = fecha_vencimiento
        self.precio = precio
        self.stock = stock

    # Método 1: Cambiar uno o varios datos del producto
    def actualizar_datos(self, descripcion=None, precio=None, stock=None):
        if descripcion is not None:
            self.descripcion = descripcion
        if precio is not None:
            self.precio = precio
        if stock is not None:
            self.stock = stock

    # Método 2: Calcular días para expirar y actualizar stock si venció
    def dias_para_expirar(self):
        hoy = date.today()
        dias_restantes = (self.fecha_vencimiento - hoy).days

        if dias_restantes < 0:
            self.stock = 0
            print(f"El producto '{self.descripcion}' ha expirado. Stock asignado a 0.")
        else:
            print(f"El producto '{self.descripcion}' expira en {dias_restantes} días.")
            
        return dias_restantes