import json
import os
class GestorInventario:
    @staticmethod
    def guardar_catalogo_json(lista_dispositivos, ruta_archivo):
        """Serializa y almacena la lista de dispositivos ecológicos en un archivo JSON."""
        datos_catalogo = []
        for dispositivo in lista_dispositivos:
            # utilizo método de polimorfismo de la ficha técnica
            datos_catalogo.append(dispositivo.obtener_ficha_tecnica())
        
        try:
            with open(ruta_archivo, 'w', encoding='utf-8') as archivo:
                json.dump(datos_catalogo, archivo, indent=4, ensure_ascii=False)
            print(f"Catálogo exportado exitosamente en: {ruta_archivo}")
        except Exception as e:
            print(f"Error al guardar el archivo JSON: {e}")