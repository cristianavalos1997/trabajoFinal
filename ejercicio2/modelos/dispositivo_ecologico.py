from excepciones.stock_invalido_error import StockInvalidoError
class DispositivoEcológico:
    def __init__(self, codigo: str, nombre: str, stock: int):
        self.codigo = codigo
        self.nombre = nombre
        self._stock = 0  # Inicializamos usando el setter para validar
        self.stock = stock  # Llama al setter
    @property
    def stock(self):
        return self._stock
    @stock.setter
    def stock(self, nuevo_stock: int):
        if nuevo_stock < 0:
            raise StockInvalidoError(f"Error de stock para '{self.nombre}': El valor {nuevo_stock} es inválido. No se permiten stocks negativos.")
        self._stock = nuevo_stock
    def obtener_ficha_tecnica(self) -> dict:
        """Método base que será sobrescrito (polimorfismo)."""
        return {
            "codigo": self.codigo,
            "nombre": self.nombre,
            "stock": self.stock
        }