from excepciones.stock_invalido_error import StockInvalidoError
from modelos.panel_solar import PanelSolar
from persistencia.gestor_inventario import GestorInventario
def main():
    print("--- INICIANDO SISTEMA ECOTECH SOLUTIONS ---\n")
    # 1. Verifico captura controlada de StockInvalidoError (para el Punto B)
    print("Probando validación de stock negativo...")
    try:
        # Intento crear un panel con stock negativo para forzar el error
        panel_defectuoso = PanelSolar("PS-999", "Panel Experimental", stock=-5, potencia_w=300, tipo_celda="Monocristalino")
    except StockInvalidoError as e:
        print(f"[EXCEPCIÓN CAPTURADA EXITOSAMENTE]: {e}\n")
    # 2. Creación de los productos válidos para el punto A y B
    print("Creando catálogo de productos válidos...")
    panel_1 = PanelSolar("PS-001", "EcoPanel Max 400W", stock=15, potencia_w=400, tipo_celda="Monocristalino")
    panel_2 = PanelSolar("PS-002", "SunPower Slim 250W", stock=8, potencia_w=250, tipo_celda="Policristalino")
    lista_productos = [panel_1, panel_2]
    # 3. Exportación de forma exitosa en el archivo JSON para el Punto B
    print("\nExportando catálogo a disco...")
    ruta_json = "catalogo_ecotech.json"
    GestorInventario.guardar_catalogo_json(lista_productos, ruta_json)
    print("\n--- PROCESO FINALIZADO ---")
if __name__ == "__main__":
    main()