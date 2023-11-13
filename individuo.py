from .constants import COLORS, DBS, IDES, JOBS, LANGS
import random


class Individuo:
    def __init__(self):
        colores = COLORS.copy()
        profesiones = JOBS.copy()
        lenguajes = LANGS.copy()
        bases_datos = DBS.copy()
        editores = IDES.copy()

        random.shuffle(colores)
        random.shuffle(profesiones)
        random.shuffle(lenguajes)
        random.shuffle(bases_datos)
        random.shuffle(editores)

        self.casas = [[colores[i], profesiones[i], lenguajes[i],
                       bases_datos[i], editores[i]] for i in range(5)]
        self.aptitud = 0

    def calcular_aptitud(self):
        self.aptitud = 0
        for i, casa in enumerate(self.casas):
            # Pista 2: El Matemático vive en la casa roja
            if casa[1] == "Matemático" and casa[0] == "Rojo":
                self.aptitud += 1

            # Pista 3: El hacker programa en Python
            if casa[1] == "Hacker" and casa[2] == "Python":
                self.aptitud += 1

            # Pista 4: El Brackets es utilizado en la casa verde
            if casa[4] == "Brackets" and casa[0] == "Verde":
                self.aptitud += 1

            # Pista 5: El analista usa Atom
            if casa[1] == "Analista" and casa[4] == "Atom":
                self.aptitud += 1

            # Pista 6: La casa verde está a la derecha de la casa blanca
            if (i < 4 and self.casas[i][0] == "Blanco" and self.casas[i + 1][0] == "Verde") or (
                i > 0 and self.casas[i][0] == "Verde" and self.casas[i - 1][0] == "Blanco"):
                self.aptitud += 1

            # Pista 7: La persona que usa Redis programa en Java
            if casa[3] == "Redis" and casa[2] == "Java":
                self.aptitud += 1

            # Pista 8: Cassandra es utilizado en la casa amarilla
            if casa[3] == "Cassandra" and casa[0] == "Amarillo":
                self.aptitud += 1

            # Pista 9: Notepad++ es usado en la casa del medio
            if i == 2 and casa[4] == "Notepad++":
                self.aptitud += 1

            # Pista 10: El Desarrollador vive en la primera casa
            if i == 0 and casa[1] == "Desarrollador":
                self.aptitud += 1

            # Pista 11
            if (i < 4 and ((casa[3] == "HBase" and self.casas[i + 1][2] == "JavaScript") or (
                self.casas[i + 1][3] == "HBase" and casa[2] == "JavaScript"))) or (
                    i > 0 and ((casa[3] == "HBase" and self.casas[i - 1][2] == "JavaScript") or (
                    self.casas[i - 1][3] == "HBase" and casa[2] == "JavaScript"))):
                self.aptitud += 1

            # Pista 12
            if (i < 4 and (
                (casa[3] == "Cassandra" and self.casas[i + 1][2] == "C#") or (
                    self.casas[i + 1][3] == "Cassandra" and casa[2] == "C#"))) or (
                        i > 0 and ((casa[3] == "Cassandra" and self.casas[i - 1][2] == "C#") or (
                            self.casas[i - 1][3] == "Cassandra" and casa[2] == "C#"))):
                self.aptitud += 1
                
            # Pista 13: La persona que usa Neo4J usa Sublime Text
            if casa[3] == "Neo4J" and casa[4] == "Sublime Text":
                self.aptitud += 1

            # Pista 14: El Ingeniero usa MongoDB
            if casa[1] == "Ingeniero" and casa[3] == "MongoDB":
                self.aptitud += 1

            # Pista 15: El desarrollador vive en la casa azul
            if casa[1] == "Desarrollador" and casa[0] == "Azul":
                self.aptitud += 1

        return self.aptitud


    def __str__(self):
        return f"Casas: {self.casas} - Aptitud: {self.aptitud}"
