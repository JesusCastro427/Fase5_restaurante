# ==========================================
# PROGRAMA: PROMOCIÓN MENÚ RESTAURANTE
# Autor: Jesus Castro
# ==========================================

# MATRIZ DEL MENÚ
# [Nombre del producto, Categoría, Precio Base]

menu = [
    ["Hamburguesa", "Comida Rapida", 25000],
    ["Pizza", "Comida Rapida", 30000],
    ["Ensalada", "Saludable", 18000],
    ["Jugo Natural", "Bebida", 12000],
    ["Pasta", "Italiana", 28000],
    ["Café", "Bebida", 8000]
]

# CATEGORÍA OBJETIVO PARA EL DESCUENTO
categoria_objetivo = "Comida Rapida"

# UMBRAL MÍNIMO PARA APLICAR DESCUENTO
umbral = 20000


# ==========================================
# FUNCIÓN PARA CALCULAR EL PRECIO FINAL
# ==========================================

def calcular_precio_final(categoria, precio):

    # Verificar si cumple las condiciones
    if categoria == categoria_objetivo and precio > umbral:

        descuento = precio * 0.15
        precio_final = precio - descuento

    else:
        precio_final = precio

    return precio_final


# ==========================================
# MOSTRAR RESULTADOS
# ==========================================

print("======================================")
print("      MENÚ DEL RESTAURANTE")
print("======================================")

# RECORRER LA MATRIZ
for producto in menu:

    nombre = producto[0]
    categoria = producto[1]
    precio_base = producto[2]

    # LLAMAR FUNCIÓN
    precio_final = calcular_precio_final(categoria, precio_base)

    # MOSTRAR DATOS
    print("Producto:", nombre)
    print("Categoría:", categoria)
    print("Precio Base: $", precio_base)
    print("Precio Final: $", precio_final)

print("======================================")
print("Promociones aplicadas correctamente")
print("======================================")