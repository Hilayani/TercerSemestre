import streamlit as st

# Función de saludo
def saludar(nombre):
    return f"Hola, {nombre}"

# Suma de dos números
def sumar(a, b):
    return a + b

# Área de un triángulo
def calcular_area_triangulo(base, altura):
    return (base * altura) / 2

# Calculadora de descuento
def calcular_precio_final(precio, descuento=10, impuesto=16):
    precio_con_descuento = precio - (precio * (descuento / 100))
    precio_final = precio_con_descuento + (precio_con_descuento * (impuesto / 100))
    return precio_final

# Suma de una lista de números
def sumar_lista(numeros):
    return sum(numeros)

# Producto con valores predeterminados
def producto(nombre, cantidad=1, precio_unitario=10):
    return cantidad * precio_unitario

# Números pares e impares
def numeros_pares_e_impares(numeros):
    pares = [num for num in numeros if num % 2 == 0]
    impares = [num for num in numeros if num % 2 != 0]
    return pares, impares

# Multiplicación con *args
def multiplicar_todos(*args):
    if not args:
        return 1
    resultado = 1
    for num in args:
        resultado *= num
    return resultado

# Información personal con **kwargs
def informacion_personal(**kwargs):
    return kwargs

# Calculadora flexible
def calculadora_flexible(a, b, operacion="suma"):
    if operacion == "suma":
        return a + b
    elif operacion == "resta":
        return a - b
    elif operacion == "multiplicacion":
        return a * b
    elif operacion == "division" and b != 0:
        return a / b
    else:
        return "Operación no válida o división por cero."

# Configuración de la barra lateral para navegar entre los ejercicios
st.sidebar.title("Ejercicios")
opcion = st.sidebar.selectbox("Selecciona un ejercicio", [
    "Saludo", 
    "Suma de dos números", 
    "Área de un triángulo", 
    "Calculadora de descuento",
    "Suma de una lista de números",
    "Producto con valores predeterminados",
    "Números pares e impares",
    "Multiplicación con *args",
    "Información personal con **kwargs",
    "Calculadora flexible"
])

# Ejercicio 1: Saludo
if opcion == "Saludo":
    nombre = st.text_input("Ingresa tu nombre")
    if st.button("Saludar"):
        st.write(saludar(nombre))

# Ejercicio 2: Suma de dos números
elif opcion == "Suma de dos números":
    a = st.number_input("Ingresa el primer número", value=0)
    b = st.number_input("Ingresa el segundo número", value=0)
    if st.button("Sumar"):
        st.write(f"La suma es: {sumar(a, b)}")

# Ejercicio 3: Área de un triángulo
elif opcion == "Área de un triángulo":
    base = st.number_input("Ingresa la base del triángulo", value=0)
    altura = st.number_input("Ingresa la altura del triángulo", value=0)
    if st.button("Calcular área"):
        st.write(f"El área del triángulo es: {calcular_area_triangulo(base, altura)}")

# Ejercicio 4: Calculadora de descuento
elif opcion == "Calculadora de descuento":
    precio = st.number_input("Ingresa el precio original", value=0.0)
    descuento = st.number_input("Ingresa el porcentaje de descuento", value=10.0)
    impuesto = st.number_input("Ingresa el porcentaje de impuesto", value=16.0)
    if st.button("Calcular precio final"):
        st.write(f"El precio final es: {calcular_precio_final(precio, descuento, impuesto)}")

# Ejercicio 5: Suma de una lista de números
elif opcion == "Suma de una lista de números":
    numeros = st.text_input("Ingresa una lista de números separados por comas")
    if st.button("Sumar lista"):
        lista_numeros = list(map(int, numeros.split(',')))
        st.write(f"La suma de la lista es: {sumar_lista(lista_numeros)}")

# Ejercicio 6: Producto con valores predeterminados
elif opcion == "Producto con valores predeterminados":
    nombre = st.text_input("Nombre del producto")
    cantidad = st.number_input("Cantidad", value=1)
    precio_unitario = st.number_input("Precio por unidad", value=10.0)
    if st.button("Calcular precio total"):
        st.write(f"El precio total es: {producto(nombre, cantidad, precio_unitario)}")

# Ejercicio 7: Números pares e impares
elif opcion == "Números pares e impares":
    numeros = st.text_input("Ingresa una lista de números separados por comas")
    if st.button("Separar pares e impares"):
        lista_numeros = list(map(int, numeros.split(',')))
        pares, impares = numeros_pares_e_impares(lista_numeros)
        st.write(f"Números pares: {pares}")
        st.write(f"Números impares: {impares}")

# Ejercicio 8: Multiplicación con *args
elif opcion == "Multiplicación con *args":
    numeros = st.text_input("Ingresa una lista de números separados por comas")
    if st.button("Multiplicar todos"):
        lista_numeros = list(map(int, numeros.split(',')))
        st.write(f"El resultado de la multiplicación es: {multiplicar_todos(*lista_numeros)}")

# Ejercicio 9: Información personal con **kwargs
elif opcion == "Información personal con **kwargs":
    nombre = st.text_input("Nombre")
    edad = st.number_input("Edad", value=0)
    direccion = st.text_input("Dirección")
    if st.button("Mostrar información"):
        info = informacion_personal(nombre=nombre, edad=edad, direccion=direccion)
        for clave, valor in info.items():
            st.write(f"{clave}: {valor}")

# Ejercicio 10: Calculadora flexible
elif opcion == "Calculadora flexible":
    a = st.number_input("Ingresa el primer número", value=0)
    b = st.number_input("Ingresa el segundo número", value=0)
    operacion = st.selectbox("Selecciona la operación", ["suma", "resta", "multiplicacion", "division"])
    if st.button("Calcular"):
        st.write(f"El resultado es: {calculadora_flexible(a, b, operacion)}")