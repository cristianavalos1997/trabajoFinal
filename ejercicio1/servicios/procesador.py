import pandas as pd

def limpiar_registro_sensor(registro_raw: dict) -> dict:
    """
    Punto A: Normaliza un registro de sensor crudo utilizando Pandas.
    Se maneja valores en formato de lista (con posibles None).
    Aplica validación estricta: lanza un ValueError si la ubicación no está registrada.
    """
    # Extraigo los valores de las listas de manera segura por las dudas si viene con ['VALOR'] o [None]
    s_id = registro_raw.get("sensor_id", [None])
    temp = registro_raw.get("temperatura", [None])
    ubi = registro_raw.get("ubicacion", [None])

    val_id = s_id[0] if isinstance(s_id, list) and len(s_id) > 0 else s_id
    val_temp = temp[0] if isinstance(temp, list) and len(temp) > 0 else temp
    val_ubi = ubi[0] if isinstance(ubi, list) and len(ubi) > 0 else ubi

    # Creo el DataFrame directamente con los valores extraídos
    df = pd.DataFrame([{
        "sensor_id": val_id,
        "temperatura": val_temp,
        "ubicacion": val_ubi
    }])
    
    # 1. Limpieza de espacios sobrantes en 'sensor_id'
    df["sensor_id"] = df["sensor_id"].astype(str).str.strip()
    
    # 2. Quito letras y espacios de la temperatura
    df["temperatura"] = (
        df["temperatura"]
        .astype(str)
        .str.upper()
        .str.replace("C", "", regex=False)
        .str.strip()
    )
    df["temperatura"] = pd.to_numeric(df["temperatura"], errors="coerce")
    
    # 3. OPCIÓN 2: Valido estrictamente la ubicación. Si no existe, es None o está vacía, se lanza un error.
    ubicacion_actual = df.loc[0, "ubicacion"]
    if pd.isna(ubicacion_actual) or ubicacion_actual is None or str(ubicacion_actual).strip() in ["None", ""]:
        sensor_actual = df.loc[0, "sensor_id"]
        raise ValueError(f"Error de validación: El sensor '{sensor_actual}' no posee una ubicación registrada.")
    
    df["ubicacion"] = str(ubicacion_actual).strip()
        
    # Retorno el registro procesado como un diccionario plano
    return df.iloc[0].to_dict()


def generar_resumen_sensores(lista_sensores_limpios: list, umbral_temperatura: float) -> tuple:
    """
    Punto B: Se genera el resumen estadístico calculando el promedio mediante acumulación
    y filtrando las alertas mediante Pandas.
    """
    if not lista_sensores_limpios:
        return [], 0.0
        
    # Cálculo del promedio acumulando los valores 
    temperaturas_acumuladas = 0.0
    for sensor in lista_sensores_limpios:
        temperaturas_acumuladas += float(sensor["temperatura"])
        
    promedio_temperatura = temperaturas_acumuladas / len(lista_sensores_limpios)
    
    # Mapeo y filtrado de alertas usando Pandas
    df_sensores = pd.DataFrame(lista_sensores_limpios)
    sensores_en_alerta = df_sensores[df_sensores["temperatura"] > umbral_temperatura]
    lista_sensores_alerta = sensores_en_alerta["sensor_id"].tolist()
    
    return lista_sensores_alerta, promedio_temperatura