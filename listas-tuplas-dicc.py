# 1) CARGA DE DATOS
ventas = [
    {"fecha": "2026-02-01", "producto": "Lavarropa",           "cantidad": 6, "precio": 1400.0},
    {"fecha": "2026-02-02", "producto": "Smart Tv Samsung 50", "cantidad": 2, "precio": 2344.0},
    {"fecha": "2026-02-03", "producto": "Laptop",              "cantidad": 3, "precio": 1567.0},
    {"fecha": "2026-02-06", "producto": "Laptop",              "cantidad": 2, "precio": 2000.0},
    {"fecha": "2026-02-04", "producto": "Silla Gamer",         "cantidad": 8, "precio": 5022.0},
    {"fecha": "2026-02-05", "producto": "Silla plegable",      "cantidad": 4, "precio": 2033.0},
]

print("1) Lista de ventas:")
for venta in ventas:
    print(venta)


# 2) CÁLCULO DE INGRESOS TOTALES
ingresos_totales = 0

for venta in ventas:
    ingresos_totales += venta["cantidad"] * venta["precio"]

print("\n2) Ingresos totales generados:", ingresos_totales)


# 3) PRODUCTO MÁS VENDIDO
ventas_por_producto = {}

for venta in ventas:
    producto = venta["producto"]
    if producto in ventas_por_producto:
        ventas_por_producto[producto] += venta["cantidad"]
    else:
        ventas_por_producto[producto] = venta["cantidad"]

producto_mas_vendido = max(ventas_por_producto, key=ventas_por_producto.get)

print("\n3) Producto más vendido:", producto_mas_vendido)
print("   Cantidad:", ventas_por_producto[producto_mas_vendido])


# 4) PRECIO PROMEDIO POR PRODUCTO
precios_por_producto = {}

for venta in ventas:
    producto = venta["producto"]
    cantidad = venta["cantidad"]
    precio = venta["precio"]
    if producto in precios_por_producto:
        suma, cant = precios_por_producto[producto]
        precios_por_producto[producto] = (suma + precio * cantidad, cant + cantidad)
    else:
        precios_por_producto[producto] = (precio * cantidad, cantidad)

print("\n4) Precio promedio por producto:")
for producto, (suma, cantidad) in precios_por_producto.items():
    promedio = suma / cantidad
    print(f"   {producto}: ${promedio:.2f}")


# 5) INGRESOS POR DÍA
ingresos_por_dia = {}

for venta in ventas:
    fecha = venta["fecha"]
    total = venta["cantidad"] * venta["precio"]
    if fecha in ingresos_por_dia:
        ingresos_por_dia[fecha] += total
    else:
        ingresos_por_dia[fecha] = total

print("\n5) Ingresos por dia:")
for fecha, ingreso in sorted(ingresos_por_dia.items()):
    print(f"   {fecha}: ${ingreso:.2f}")

    # Total
total_dias = sum(ingresos_por_dia.values())
print(f"   {'─'*30}")
print(f"   Total: ${total_dias:.2f}")


# 6) RESUMEN DE VENTAS
resumen_ventas = {}

for venta in ventas:
    producto = venta["producto"]
    cantidad = venta["cantidad"]
    precio = venta["precio"]
    total = cantidad * precio
    if producto in resumen_ventas:
        resumen_ventas[producto]["cantidad_total"] += cantidad
        resumen_ventas[producto]["ingresos_totales"] += total
    else:
        resumen_ventas[producto] = {
            "cantidad_total": cantidad,
            "ingresos_totales": total
        }

for producto in resumen_ventas:
    datos = resumen_ventas[producto]
    datos["precio_promedio"] = datos["ingresos_totales"] / datos["cantidad_total"]

print("\n6) Resumen de ventas por producto:")
for producto, datos in resumen_ventas.items():
    print(f"   {producto}:")
    print(f"      Cantidad total:   {datos['cantidad_total']}")
    print(f"      Ingresos totales: ${datos['ingresos_totales']:.2f}")
    print(f"      Precio promedio:  ${datos['precio_promedio']:.2f}")
