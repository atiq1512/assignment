import random
import pandas as pd
import streamlit as st

# --- Helper Functions ---

def initialize_population(programs, pop_size):
    population = []
    for _ in range(pop_size):
        schedule = random.sample(programs, len(programs))
        population.append(schedule)
    return population

def fitness(schedule, ratings):
    # Higher total rating = better fitness
    total = 0
    for i, program in enumerate(schedule):
        total += ratings[program]
    return total

def selection(population, ratings):
    # Rank schedules by fitness
    sorted_pop = sorted(population, key=lambda s: fitness(s, ratings), reverse=True)
    return sorted_pop[:len(population)//2]

def crossover(parent1, parent2):
    point = random.randint(1, len(parent1)-2)
    child = parent1[:point] + [p for p in parent2 if p not in parent1[:point]]
    return child

def mutate(schedule, mut_rate, programs):
    for i in range(len(schedule)):
        if random.random() < mut_rate:
            j = random.randint(0, len(schedule)-1)
            schedule[i], schedule[j] = schedule[j], schedule[i]
    return schedule

def genetic_algorithm(programs, ratings, pop_size, co_r, mut_r, generations=100):
    population = initialize_population(programs, pop_size)
    best_schedule = None
    best_fitness = 0
    
    for _ in range(generations):
        selected = selection(population, ratings)
        next_gen = []
        for _ in range(len(population)):
            p1 = random.choice(selected)
            p2 = random.choice(selected)
            child = crossover(p1, p2) if random.random() < co_r else p1.copy()
            child = mutate(child, mut_r, programs)
            next_gen.append(child)
        
        population = next_gen
        fittest = max(population, key=lambda s: fitness(s, ratings))
        f = fitness(fittest, ratings)
        if f > best_fitness:
            best_fitness = f
            best_schedule = fittest

    return best_schedule, best_fitness

# --- Streamlit App ---
st.title("Scheduling using Genetic Algorithm")

st.sidebar.header("Algorithm Parameters")
co_r = st.sidebar.slider("Crossover Rate (CO_R)", 0.0, 0.95, 0.8)
mut_r = st.sidebar.slider("Mutation Rate (MUT_R)", 0.01, 0.05, 0.02)
pop_size = st.sidebar.number_input("Population Size", 100, 1000, 500)
generations = st.sidebar.number_input("Generations", 10, 500, 100)

if st.button("Run Genetic Algorithm"):
    programs = ["Program A", "Program B", "Program C", "Program D", "Program E"]
    ratings = {
        "Program A": 8, "Program B": 5, "Program C": 9,
        "Program D": 6, "Program E": 7
    }
    
    schedule, score = genetic_algorithm(programs, ratings, pop_size, co_r, mut_r, generations)
    
    df = pd.DataFrame({"Time Slot": [f"Slot {i+1}" for i in range(len(schedule))],
                       "Program": schedule})
    
    st.subheader("Optimized Schedule")
    st.table(df)
    st.write(f"**Total Rating (Fitness): {score}**")
