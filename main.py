from .genetic_algorithm import AlgoritmoGenetico

def main():
    tamaño_poblacion = 1000000
    numero_generaciones = 200000
    print(f"Comienzo de algoritmo genetico con población de {tamaño_poblacion} individuos y {numero_generaciones} generaciones")
    algoritmo = AlgoritmoGenetico(tamaño_poblacion)
    for i in range(numero_generaciones):
        algoritmo.evolucionar()
        print(f"Generación {i+1}: Mejor Aptitud = {algoritmo.poblacion[0].aptitud}")

    mejor_individuo = algoritmo.poblacion[0]
    print("\nMejor Individuo Encontrado:")
    print(mejor_individuo)

if __name__ == "__main__":
    main()

