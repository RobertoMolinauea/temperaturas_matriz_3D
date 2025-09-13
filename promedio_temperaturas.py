# promedio_temperaturas.py
# -----------------------------------------------------------
# Función para calcular la temperatura promedio por ciudad.
# Entrada: {"Ciudad": [t_sem1, t_sem2, t_sem3, t_sem4, ...]}
# - Ignora valores no numéricos o None.
# - Si no hay datos válidos, devuelve None para esa ciudad.
# -----------------------------------------------------------

from typing import Dict, Iterable, Optional

def calcular_promedio_temperaturas(datos: Dict[str, Iterable[float]]) -> Dict[str, Optional[float]]:
    """
    Calcula el promedio de temperaturas por ciudad.

    Parámetros
    ----------
    datos : dict[str, Iterable[float]]
        Diccionario con ciudades como claves y listas/iterables de temperaturas (float/int) como valores.

    Retorna
    -------
    dict[str, Optional[float]]
        Diccionario {ciudad: promedio} donde el promedio es float o None si no hay datos válidos.
    """
    promedios: Dict[str, Optional[float]] = {}

    for ciudad, temperaturas in datos.items():
        # Filtra solo valores numéricos (int/float)
        validos = [t for t in temperaturas if isinstance(t, (int, float))]
        promedios[ciudad] = (sum(validos) / len(validos)) if validos else None

    return promedios


def _imprimir_resultados(resultados: Dict[str, Optional[float]]) -> None:
    """Imprime en pantalla los promedios por ciudad, con 2 decimales o 'Sin datos'."""
    for ciudad, promedio in resultados.items():
        if promedio is None:
            print(f"La temperatura promedio en {ciudad} es: Sin datos")
        else:
            print(f"La temperatura promedio en {ciudad} es: {promedio:.2f} °C")


if __name__ == "__main__":
    # Ejemplo base: 3 ciudades, 4 semanas
    datos_temperaturas = {
        "Loja": [20.1, 21.3, 19.8, 20.5],
        "Quito": [15.2, 14.9, 15.5, 14.8],
        "Guayaquil": [28.5, 29.0, 28.8, 29.2],
    }

    resultados = calcular_promedio_temperaturas(datos_temperaturas)
    _imprimir_resultados(resultados)

    # Pruebas simples
    assert calcular_promedio_temperaturas({"A": [10, 20, 30]})["A"] == 20.0
    assert calcular_promedio_temperaturas({"B": []})["B"] is None
    assert calcular_promedio_temperaturas({"C": [None, "x", 10, 20]})["C"] == 15.0
    assert calcular_promedio_temperaturas({"D": [-5, 5]})["D"] == 0.0

    print("Pruebas superadas.")
