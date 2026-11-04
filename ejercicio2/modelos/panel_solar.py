from modelos.dispositivo_ecologico import DispositivoEcológico
class PanelSolar(DispositivoEcológico):
    def __init__(self, codigo: str, nombre: str, stock: int, potencia_w: float, tipo_celda: str):
        super().__init__(codigo, nombre, stock)
        self.potencia_w = potencia_w
        self.tipo_celda = tipo_celda
    # Aplico polimorfismo para personalizar la ficha técnica comercial
    def obtener_ficha_tecnica(self) -> dict:
        ficha = super().obtener_ficha_tecnica()
        ficha.update({
            "tipo_dispositivo": "Panel Solar",
            "potencia_w": self.potencia_w,
            "tipo_celda": self.tipo_celda
        })
        return ficha