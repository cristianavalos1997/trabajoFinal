import servicios.procesador

def main():
    registros_crudos = [
        {
            "sensor_id": [" SENSOR-001 "],
            "temperatura": ["24.5C"],
            "ubicacion": ["Planta Norte"]
        },
        {
            "sensor_id": ["SENSOR-002"],
            "temperatura": [" 29.8 C "],
            "ubicacion": ["Planta Sur"]  
        },
        {
            "sensor_id": [" SENSOR-003"],
            "temperatura": ["22.1C"],
            "ubicacion": ["Planta Sur"]
        },
        {
            "sensor_id": ["SENSOR-004"],
            "temperatura": ["31.4C"], 
            "ubicacion": ["Planta Este"]
        }
    ]
    
    print("--- INICIANDO PROCESAMIENTO DE SENSORES ECOTECH CON PANDAS ---")
    
    sensores_limpios = []
    
    # Recorro los registros utilizando try-except para que el programa no se rompa
    for registro in registros_crudos:
        try:
            sensor_normalizado = servicios.procesador.limpiar_registro_sensor(registro)
            sensores_limpios.append(sensor_normalizado)
        except ValueError as e:
            # Capturo el error, mostrando un mensaje y asi continuar con el siguiente
            print(f"    ⚠️  [ADVERTENCIA] Registro omitido: {e}")
        
    print(f"\n[OK] Se normalizaron {len(sensores_limpios)} registros con éxito de forma segura.")
    
    UMBRAL_PRUEBA = 25.0
    sensores_alerta, promedio_global = servicios.procesador.generar_resumen_sensores(sensores_limpios, UMBRAL_PRUEBA)
    
    print("\n================ REPORTE CONSOLIDADO ================")
    print(f" Umbral de Temperatura Configurado: {UMBRAL_PRUEBA} °C")
    print(f" Promedio Térmico Global de la Planta: {promedio_global:.2f} °C")
    print(f" Dispositivos en Alerta (> {UMBRAL_PRUEBA} °C):")
    
    if sensores_alerta:
        for sensor_id in sensores_alerta:
            print(f"        ⚠️     Alerta crítica en dispositivo: {sensor_id}")
    else:
        print("        ✅ Ningún dispositivo supera el umbral establecido.")
        
    print("=====================================================")

if __name__ == "__main__":
    main()