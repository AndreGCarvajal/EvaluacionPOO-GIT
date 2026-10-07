class Alojamiento:

    def __init__(self, nombre, tipo, precio, capacidad): # Inicializamos los atributos básicos de la instancia
        self.nombre = nombre
        self.tipo = tipo
        self.precio = precio
        self.capacidad = capacidad
    def mostrar_info(self):
        # Retornamos la cadena formateada con el formato de moneda y personas solicitado
        return f"Alojamiento: {self.nombre} | Tipo: {self.tipo} | Precio: ${self.precio:,.2f} | Capacidad: {self.capacidad} personas"


    # Reglas (léelas con atención, no son solo "rellenar")
    # 1. mostrar_info()

    # Debe devolver (no imprimir) una cadena de texto con la información
    # del alojamiento, en un formato legible y consistente.
    # El precio debe verse como moneda y la capacidad como número de personas.

    def precio_por_persona(self):
        # COMPLETAR
        pass

    def precio_por_persona(self):
        # Primero validamos que ni el precio ni la capacidad sean menores o iguales a cero
        if self.precio <= 0 or self.capacidad <= 0:
            # Si los datos no son válidos, devolvemos None para no generar errores
            return None

        # Si son válidos, calculamos la división y redondeamos el resultado a 2 decimales
        return round(self.precio / self.capacidad, 2)

    # 2. precio_por_persona()

    # Debe devolver el precio que corresponde pagar por persona.
    # Si precio o capacidad no son válidos (capacidad o precio <= 0), 
    # no debe lanzar error: debe devolver None.
    # El resultado debe estar redondeado a 2 decimales.

# Objeto 1: Creamos la instancia para la casa
casa = Alojamiento(
    "Casa Centro",
    "Casa",
    1800,
    6
)
# Objeto 2: Creamos la instancia para el departamento
departamento = Alojamiento(
    "Departamento Reforma",
    "Departamento",
    1200,
    4
)


# 1. Mostrar la información de la casa.
print(casa.mostrar_info())
# 2. Mostrar el precio por persona de la casa.
print(f"Precio por persona: ${casa.precio_por_persona()}")
# 3. Mostrar la información del departamento.
print(departamento.mostrar_info())
# 4. Mostrar el precio por persona del departamento.
print(f"Precio por persona: ${departamento.precio_por_persona()}")
