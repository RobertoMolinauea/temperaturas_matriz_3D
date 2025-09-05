ciudades = ["Quito", "Guayaquil", "Cuenca"]
dias = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]

# Datos ficticios (edítalos si quieres). Cada sublista son 7 días.
temperaturas = [
    [   # Quito
        [18, 20, 19, 21, 22, 20, 19],  # Semana 1
        [17, 18, 20, 21, 19, 18, 17]   # Semana 2
    ],
    [   # Guayaquil
        [28, 29, 30, 31, 29, 28, 30],  # Semana 1
        [27, 28, 29, 30, 31, 29, 28]   # Semana 2
    ],
    [   # Cuenca
        [15, 16, 17, 16, 15, 14, 15],  # Semana 1
        [14, 15, 16, 15, 14, 13, 14]   # Semana 2
    ]
]

# --- Cálculo de promedios con bucles anidados ---
num_ciudades = len(ciudades)
num_semanas = len(temperaturas[0])
num_dias = len(dias)

promedios = [[0.0 for _ in range(num_semanas)] for _ in range(num_ciudades)]

for i in range(num_ciudades):          # ciudades
    for j in range(num_semanas):       # semanas
        suma = 0
        for k in range(num_dias):      # días
            suma += temperaturas[i][j][k]
        promedios[i][j] = suma / num_dias

# --- Salida “bonita” en tabla ---
encabezado = ["Ciudad"] + [f"Semana {s+1}" for s in range(num_semanas)]
ancho = 12
print("".join(col.ljust(ancho) for col in encabezado))

for i, ciudad in enumerate(ciudades):
    fila = [ciudad] + [f"{promedios[i][s]:.2f} °C" for s in range(num_semanas)]
    print("".join(col.ljust(ancho) for col in fila))