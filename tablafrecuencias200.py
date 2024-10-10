import random

def calcular_frecuencias(numeros):
    # Frecuencia absoluta
    frec_abs = {}
    for num in numeros:
        frec_abs[num] = frec_abs.get(num, 0) + 1

    total_numeros = len(numeros)
    
    # Frecuencia relativa y porcentaje
    frec_rel = {}
    porcentaje = {}
    for num, frecuencia in frec_abs.items():
        frec_rel[num] = frecuencia / total_numeros
        porcentaje[num] = frec_rel[num] * 100

    # Frecuencia absoluta acumulada
    frec_abs_acum = {}
    acum = 0
    for num, frecuencia in frec_abs.items():
        acum += frecuencia
        frec_abs_acum[num] = acum

    # Frecuencia relativa acumulada y porcentaje acumulado
    frec_rel_acum = {}
    porcentaje_acum = {}
    acum_rel = 0
    for num, frecuencia in frec_rel.items():
        acum_rel += frecuencia
        frec_rel_acum[num] = acum_rel
        porcentaje_acum[num] = acum_rel * 100

    # Mostrar tabla de frecuencias
    print("Dato | Frec. Abs. | Frec. Rel. | Porcentaje | Frec. Abs. Acum. | Frec. Rel. Acum. | Porcentaje Acum.")
    for num in sorted(frec_abs.keys()):
        print(f"{num:4} | {frec_abs[num]:10} | {frec_rel[num]:10.2f} | {porcentaje[num]:10.2f} | {frec_abs_acum[num]:16} | {frec_rel_acum[num]:16.2f} | {porcentaje_acum[num]:15.2f}")

    # totales
    print("-" * 82)
    total_frec_abs = sum(frec_abs.values())
    total_frec_rel = sum(frec_rel.values())
    total_porcentaje = sum(porcentaje.values())

    # El último valor de la frecuencia acumulada y porcentaje acumulado es el total
    ultimo_frec_abs_acum = max(frec_abs_acum.values())
    ultimo_frec_rel_acum = max(frec_rel_acum.values())
    ultimo_porcentaje_acum = max(porcentaje_acum.values())

    print(f"{'Totales':4} | {total_frec_abs:10} | {total_frec_rel:10.2f} | {total_porcentaje:10.2f} | {ultimo_frec_abs_acum:16} | {ultimo_frec_rel_acum:16.2f} | {ultimo_porcentaje_acum:15.2f}")

# Generar 200 números al azar entre 0 y 10
numeros_aleatorios = [random.randint(0, 10) for _ in range(200)]

# Mostrar los 200 números generados
print("Números generados:")
print(numeros_aleatorios)

# Llamar a la función para calcular y mostrar las frecuencias
calcular_frecuencias(numeros_aleatorios)
