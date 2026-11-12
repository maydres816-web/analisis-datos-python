"""
Proyecto: Sistema Básico de Análisis de Datos de Ventas
Nivel: Primer Semestre - Fundamentos de Programación
Objetivo: Aplicar descomposición de problemas, limpieza de datos y cálculo de métricas
          utilizando estructuras nativas de Python (listas, diccionarios y funciones).
"""

# 1. DATOS CRUDOS (Simulación de registros con algunos errores de captura)
registros_crudos = [
    {"id": 1, "producto": "Laptop", "categoria": "Tecnologia", "precio": 850.00, "cantidad": 2},
    {"id": 2, "producto": "Mouse", "categoria": "Accesorios", "precio": 15.50, "cantidad": 10},
    {"id": 3, "producto": "Teclado", "categoria": "Accesorios", "precio": -25.00, "cantidad": 4},   # Error: precio negativo
    {"id": 4, "producto": "Monitor", "categoria": "Tecnologia", "precio": 220.00, "cantidad": 3},
    {"id": 5, "producto": "Laptop", "categoria": "Tecnologia", "precio": 850.00, "cantidad": 1},
    {"id": 6, "producto": "Audifonos", "categoria": "Accesorios", "precio": 45.00, "cantidad": 0},   # Error: cantidad cero
    {"id": 7, "producto": "Impresora", "categoria": "Oficina", "precio": 180.00, "cantidad": 2},
    {"id": 8, "producto": "Silla", "categoria": "Oficina", "precio": 130.00, "cantidad": 4},
]


# 2. FASE DE LIMPIEZA Y VALIDACIÓN (Preprocesamiento)
def limpiar_datos(datos):
    """Filtra registros inválidos (precios o cantidades menores o iguales a cero)."""
    datos_limpios = []
    descartados = 0

    for fila in datos:
        if fila["precio"] > 0 and fila["cantidad"] > 0:
            datos_limpios.append(fila)
        else:
            descartados += 1

    return datos_limpios, descartados


# 3. FASE DE PROCESAMIENTO Y ANÁLISIS (Algoritmos de agregación)
def analizar_ventas(datos):
    """Calcula ingresos totales, producto más vendido e ingresos por categoría en un solo recorrido."""
    ingreso_total = 0.0
    unidades_por_producto = {}
    ingresos_por_categoria = {}

    for fila in datos:
        subtotal = fila["precio"] * fila["cantidad"]
        ingreso_total += subtotal

        # Acumular unidades por producto
        prod = fila["producto"]
        unidades_por_producto[prod] = unidades_por_producto.get(prod, 0) + fila["cantidad"]

        # Acumular ingresos por categoría
        cat = fila["categoria"]
        ingresos_por_categoria[cat] = ingresos_por_categoria.get(cat, 0.0) + subtotal

    # Encontrar el producto con mayor cantidad de unidades vendidas
    producto_top = max(unidades_por_producto, key=unidades_por_producto.get)
    max_unidades = unidades_por_producto[producto_top]

    return {
        "ingreso_total": ingreso_total,
        "producto_top": (producto_top, max_unidades),
        "por_categoria": ingresos_por_categoria,
        "total_transacciones": len(datos)
    }


# 4. FASE DE PRESENTACIÓN DE RESULTADOS
def generar_reporte():
    datos_validos, errores = limpiar_datos(registros_crudos)
    resultados = analizar_ventas(datos_validos)

    print("=== REPORTE DE ANÁLISIS DE DATOS ===")
    print(f"Registros procesados : {resultados['total_transacciones']}")
    print(f"Registros descartados: {errores} (por datos inconsistentes)")
    print(f"Ingresos totales     : ${resultados['ingreso_total']:.2f}")
    print(f"Producto más vendido : {resultados['producto_top'][0]} ({resultados['producto_top'][1]} unidades)")
    print("\n--- Desglose por Categoría ---")
    for categoria, monto in resultados["por_categoria"].items():
        porcentaje = (monto / resultados["ingreso_total"]) * 100
        print(f"  * {categoria:<12}: ${monto:>8.2f} ({porcentaje:.1f}%)")


if __name__ == "__main__":
    generar_reporte()
