from django.shortcuts import render
from calculos.emisiones import obtener_metricas_consumo
def vista_panel_sustentabilidad(request):
    """Esta vista de Django procesa las métricas de sustentabilidad y para enviarlas al panel."""
    # Datos de ejemplo obteniendo
    registros_plantas = [
        {
            'planta': 'Planta Norte', 
            'consumo_kwh': 250
        },
        {
            'planta': 'Planta Sur', 
            'consumo_kwh': 420
        },
        {
            'planta': 'Planta Este', 
            'consumo_kwh': 180
        }
    ]
    # Llamo a la función de procesamiento del algoritmo
    metricas = obtener_metricas_consumo(registros_plantas)
    # Preparo el diccionario de contexto para la plantilla
    contexto = {
        'total_emisiones': metricas['total_emisiones'],
        'planta_mayor_consumo': metricas['planta_mayor_consumo']
    }
    # Aca renderizo la plantilla que se pide
    return render(request, 'sustentabilidad/panel.html', contexto)