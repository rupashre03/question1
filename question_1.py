import streamlit as st
import random
import numpy as np

# PARAMETERS
POPULATION_SIZE = 300
CHROMOSOME_LENGTH = 80
GENERATIONS = 50
TARGET_ONES = 40

# Fitness function
def fitness(chromosome):
    return chromosome.count(1)

# Initialize population
def init_population():
    return [[random.randint(0,1) for _ in range(CHROMOSOME_LENGTH)] 
            for _ in range(POPULATION_SIZE)]

# Selection 
def selection(population):
    return max(random.sample(population, 2), key=fitness)

# Crossover
def crossover(p1, p2):
    point = random.randint(1, CHROMOSOME_LENGTH - 2)
    return p1[:point] + p2[point:]

# Mutation
def mutate(chromosome, rate=0.01):
    return [bit if random.random() > rate else 1-bit for bit in chromosome]

# Streamlit UI
st.title("Genetic Algorithm")

if st.button("Run Genetic Algorithm"):
    population = init_population()
    best_fitness_progress = []

    for gen in range(GENERATIONS):
        new_population = []

        # Elitism
        best = max(population, key=fitness)
        new_population.append(best)

        while len(new_population) < POPULATION_SIZE:
            parent1 = selection(population)
            parent2 = selection(population)
            child = crossover(parent1, parent2)
            child = mutate(child)
            new_population.append(child)

        population = new_population
        best_fitness_progress.append(fitness(best))

    st.success("Evolution Completed!")

    st.write("Best Fitness Achieved:", max(best_fitness_progress))
    st.line_chart(best_fitness_progress)
    st.write("Best Chromosome:")
    st.code("".join(map(str, best)))