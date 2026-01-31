# IMPUREZA GINI  Probabilidad de clasificar incorrectamente au una observacion
import pandas as pd

puntos_partido = pd.Series(["alto", "bajo", "alto", "alto", "alto",
                            "alto", "bajo", "alto", "alto", "bajo"])

minutos_partido = pd.Series(["alto", "alto", "bajo", "bajo", "bajo",
                             "alto", "bajo", "bajo", "bajo", "alto"])

rebotes_partido = pd.Series(["alto", "bajo", "bajo", "alto", "bajo",
                             "alto", "bajo", "alto", "bajo", "alto"])

asistencias_partido = pd.Series(["bajo", "bajo", "bajo", "bajo", "bajo",
                                 "bajo", "bajo", "bajo", "bajo", "bajo"])   # info de 10 jugadores en su primer año

# 1: Veterano (carrera de cinco años o más)
clase = pd.Series([1, 0, 0, 1, 0, 1, 0, 1, 0, 1])

datos = pd.DataFrame({"puntos": puntos_partido,
                      "minutos": minutos_partido,
                      "asistencias": asistencias_partido,
                      "rebotes": rebotes_partido,                      
                      "clase": clase})

def impureza_gini(caracteristica, clase, datos):
    """str, str, DataFrame -> float"""    
    atributo_clase = datos.groupby([caracteristica, clase])[clase].count()
    atributo = datos.groupby([caracteristica])[clase].count()
    procesados = pd.merge(atributo_clase, atributo, on=[caracteristica], 
                          suffixes=('_individual', '_total')) 
    procesados["combinacion"] = (procesados[clase+"_individual"]/
                                 procesados[clase+"_total"])**2
    gini_combinacion = 1 - procesados.groupby([caracteristica, clase+"_total"])["combinacion"].sum()
    gini_pesado = (gini_combinacion * atributo) / atributo.sum() 
    return gini_pesado.sum()


print("puntos -> impureza: %0.4f" % impureza_gini("puntos", "clase", datos))   # alto nivel de impureza
print("minutos -> impureza: %0.4f" % impureza_gini("minutos", "clase", datos))  # alto nivel de impureza
print("asistencias -> impureza: %0.4f" % impureza_gini("asistencias", "clase", datos))  # impureza mayto = 0.5  la info no aporta info alguna
print("rebotes -> impureza: %0.4f" % impureza_gini("rebotes", "clase", datos)) # Rebotes impureza de 0   perfecto

print(datos)

# Cuántos jugadores por categoría de puntos y por clase (novato o veterano)
puntos_y_clase = datos.groupby(["puntos", "clase"])["clase"].count()

print("\n\nJUGADORES POR PUNTOS Y CLASE\n\n", puntos_y_clase)

# Cuántos jugadores por categoría de puntos 
puntos = datos.groupby(["puntos"])["clase"].count()

print("\n\nJUGADORES POR PUNTOS\n\n", puntos)

# Unir ambas series de datos para procesamiento posterior 
jugadores = pd.merge(
    puntos_y_clase,
    puntos,
    on=["puntos"], 
    suffixes=('_indivual', '_total')) 

print("\n\nUNION\n\n", jugadores)

# Probabilidad para cada categoría de puntos con respecto a la clase
jugadores["combinaciones"] = (jugadores["clase_indivual"]/jugadores["clase_total"])**2
print(jugadores)

# Impureza gini para cada combinación
gini_por_combinacion = 1 - jugadores.groupby(["puntos", "clase_total"])["combinaciones"].sum()
print("\n\n",gini_por_combinacion)

# Impureza gini para cada combinación con pesos
gini_con_peso_por_combinacion = (gini_por_combinacion * puntos) / puntos.sum() 
print("\n\n", gini_con_peso_por_combinacion)
print("\n", gini_con_peso_por_combinacion.sum())