from .individuo import Individuo
from .constants import COLORS, DBS, IDES, JOBS, LANGS

import random
import copy

class AlgoritmoGenetico:
    def __init__(self, tamaño_poblacion):
        self.tamaño_poblacion = tamaño_poblacion
        self.poblacion = [Individuo() for _ in range(tamaño_poblacion)]
        self.generacion = 0
        for individuo in self.poblacion:
            individuo.calcular_aptitud()


    def seleccion(self):
        self.poblacion.sort(key=lambda ind: ind.aptitud, reverse=True)
        return self.poblacion[:int(0.5 * len(self.poblacion))]


    def cruce(self, padre1, padre2):
        punto_cruce = random.randint(1, 4)
        hijo1 = copy.deepcopy(padre1)
        hijo2 = copy.deepcopy(padre2)

        hijo1.casas[punto_cruce:], hijo2.casas[punto_cruce:] = hijo2.casas[punto_cruce:], hijo1.casas[punto_cruce:]

        return hijo1, hijo2


    def mutacion(self, individuo):
        for _ in range(random.randint(1, 3)):  # Mutar múltiples atributos
            casa_mutada = random.randint(0, 4)
            atributo_mutado = random.randint(0, 4)

            nuevo_valor = None
            if atributo_mutado == 0:
                nuevo_valor = random.choice([c for c in COLORS if c != individuo.casas[casa_mutada][0]])
            elif atributo_mutado == 1:
                nuevo_valor = random.choice([p for p in JOBS if p != individuo.casas[casa_mutada][1]])
            elif atributo_mutado == 2:
                nuevo_valor = random.choice([l for l in LANGS if l != individuo.casas[casa_mutada][2]])
            elif atributo_mutado == 3:
                nuevo_valor = random.choice([b for b in DBS if b != individuo.casas[casa_mutada][3]])
            elif atributo_mutado == 4:
                nuevo_valor = random.choice([e for e in IDES if e != individuo.casas[casa_mutada][4]])

            individuo.casas[casa_mutada][atributo_mutado] = nuevo_valor


    def evolucionar(self):
        nueva_generacion = []

        seleccionados = self.seleccion()
        nueva_generacion.extend(seleccionados)

        while len(nueva_generacion) < self.tamaño_poblacion:
            if random.random() < 0.05:
                # Añadir un nuevo individuo aleatorio
                nueva_generacion.append(Individuo())
            else:
                padre1, padre2 = random.sample(seleccionados, 2)
                hijo1, hijo2 = self.cruce(padre1, padre2)

                # Aplicar mutación a copias de los hijos
                mutado_hijo1 = copy.deepcopy(hijo1)
                mutado_hijo2 = copy.deepcopy(hijo2)
                self.mutacion(mutado_hijo1)
                mutado_hijo1.calcular_aptitud()
                
                self.mutacion(mutado_hijo2)
                mutado_hijo2.calcular_aptitud()

                # Añadir los hijos mutados a la nueva generación
                nueva_generacion.append(mutado_hijo1)
                nueva_generacion.append(mutado_hijo2)

            # Asegurarse de no exceder el tamaño de la población
            if len(nueva_generacion) > self.tamaño_poblacion:
                nueva_generacion = nueva_generacion[:self.tamaño_poblacion]

        self.poblacion = nueva_generacion
        self.generacion += 1


