# TP 3 AI

This project implements a genetic algorithm to solve a complex puzzle involving houses with different attributes. The goal is to find an arrangement of houses that meets a set of given conditions.

## Prerequisites

- Python 3.10 or higher.

## Running the Code

To run the program, use the following command:

```bash
python -m main
```

## Project Explanation

### 1. Individual Design

Each individual in this problem represents a possible solution to the puzzle of 5 houses. An individual comprises 5 houses, where each house has the following attributes:

- Color
- Profession of the resident
- Programming language used
- NoSQL database used
- Text editor used

### 2. Generation of Individuals

Individuals are generated randomly, where each house in an individual is initialized with random values for each attribute, ensuring no repetitions within the same individual. This approach creates an initial population with diverse characteristics.

### 3. Genetic Operators

a. **Selection:** The selection operator implemented is elitist selection, where individuals with higher fitness are more likely to be chosen for reproduction.

b. **Crossover:** Crossover is performed by selecting a random cut-off point in two parent individuals and combining their segments to form new offspring. This allows for mixing characteristics from different solutions.

c. **Mutation:** Mutation involves randomly changing one or more attributes of an individual. This introduces variability in the population and helps explore new areas of the solution space.

### 4. Termination Conditions

The algorithm can terminate under several conditions:

- **Maximum Number of Generations:** Stop the algorithm after a predefined number of generations.
- **Fitness Convergence:** Stop if the maximum fitness does not improve significantly over a certain number of consecutive generations.
- **Optimal Fitness Achieved:** Stop if an individual reaches the maximum possible fitness score, indicating a perfect solution has been found.

### 5. Generating New Individuals for the Population

New individuals can be generated for the population through:

- **Combining the Best Traits:** Create new individuals by combining attributes from the best existing individuals.
- **Introducing Completely Random Individuals:** Occasionally introduce a completely randomly generated individual to maintain genetic diversity.
- **Directed Mutation:** Create new individuals by applying directed mutations (based on some heuristic) to the best current individuals.

These strategies help maintain a healthy diversity in the population and prevent the algorithm from getting stuck in local optima.
