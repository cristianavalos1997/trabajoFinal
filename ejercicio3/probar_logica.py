# 
from calculos.emisiones import obtener_metricas_consumo
# Datos de prueba para simular
registros_prueba = [
    {
        'planta': 'Planta Norte', 
        'consumo_kwh': 200
    },
    {
        'planta': 'Planta Sur', 
        'consumo_kwh': 500
    },
    {
        'planta': 'Planta Este', 
        'consumo_kwh': 100
    }
]
# Ejecuto la funcion
resultado = obtener_metricas_consumo(registros_prueba)
print("--- RESULTADO DEL PROCESAMIENTO ---")
print(f"Total Emisiones Globales: {resultado['total_emisiones']} kg CO2")
print(f"Planta de Mayor Consumo: {resultado['planta_mayor_consumo']}")