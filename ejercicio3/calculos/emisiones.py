def calcular_emisiones_carbono(consumo_kwh, factor_emision=0.4):
    """Calcula las emisiones de carbono industriales basadas en el kWh consumido."""
    if consumo_kwh < 0:
        raise ValueError("El consumo no puede ser negativo.")
    return consumo_kwh * factor_emision
def obtener_metricas_consumo(registros):
    """
    Se procesa un historial de consumos por planta industrial.
    Luego retorna un diccionario con el total global de emisiones y la planta de mayor consumo.
    """
    total_emisiones = 0.0
    mayor_consumo = -1
    planta_mayor_consumo = None
    for reg in registros:
        nombre_planta = reg.get('planta')
        consumo_kwh = reg.get('consumo_kwh', 0)
        # Calculo las emisiones individuales usando la función previa
        emisiones_actuales = calcular_emisiones_carbono(consumo_kwh)
        # Acumulo para el total global
        total_emisiones += emisiones_actuales
        # De esta forma determino la planta de mayor consumo
        if consumo_kwh > mayor_consumo:
            mayor_consumo = consumo_kwh
            planta_mayor_consumo = nombre_planta
    return {
        'total_emisiones': total_emisiones,
        'planta_mayor_consumo': planta_mayor_consumo
    }