class StockInvalidoError(Exception):
    """Excepción personalizada para manejar valores de stock negativos o inválidos."""
    def __init__(self, mensaje="El stock no puede ser un valor negativo."):
        super().__init__(mensaje)