import pandas as pd

def limpiar_registro_sensor(registro_raw: dict) -> dict:
    """
    Punto A: Normalizo un registro de sensor crudo utilizando Pandas.
    """
    df = pd.DataFrame([registro_raw])
    
    if "sensor_id" in df.columns:
        df["sensor_id"] = df["sensor_id"].astype(str).str.strip()
        
    if "temperatura" in df.columns:
        df["temperatura"] = (
            df["temperatura"]
            .astype(str)
            .str.upper()
            .str.replace("C", "", regex=False)
            .str.strip()
        )
        df["temperatura"] = pd.to_numeric(df["temperatura"], errors="coerce")
        
    if "ubicacion" not in df.columns or pd.isna(df.loc[0, "ubicacion"]) or str(df.loc[0, "ubicacion"]).strip() == "":
        df["ubicacion"] = "Planta Genérica"
    else:
        df["ubicacion"] = df["ubicacion"].astype(str).str.strip()
        
    return df.iloc[0].to_dict()


def generar_resumen_sensores(lista_sensores_limpios: list, umbral_temperatura: float) -> tuple:
    """
    Punto B: Se genera el resumen estadístico calculando el promedio mediante acumulación
    y filtrando las alertas mediante Pandas.
    """
    if not lista_sensores_limpios:
        return [], 0.0
        
    # 1. Cálculo del promedio acumulando los valores 
    temperaturas_acumuladas = 0.0
    for sensor in lista_sensores_limpios:
        temperaturas_acumuladas += float(sensor["temperatura"])
        
    promedio_temperatura = temperaturas_acumuladas / len(lista_sensores_limpios)
    
    # 2. Mapeo y filtrado de alertas usando Pandas
    df_sensores = pd.DataFrame(lista_sensores_limpios)
    sensores_en_alerta = df_sensores[df_sensores["temperatura"] > umbral_temperatura]
    lista_sensores_alerta = sensores_en_alerta["sensor_id"].tolist()
    
    return lista_sensores_alerta, promedio_temperatura