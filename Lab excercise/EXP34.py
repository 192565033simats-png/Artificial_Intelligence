# Genetic Algorithm to maximize f(x) = x^2

import random

def fitness(x):
    return x * x

population = [random.randint(0, 31) for _ in range(6)]

for generation in range(20):
    population.sort(key=fitness, reverse=True)

    parents = population[:3]
    new_population = parents.copy()

    while len(new_population) < 6:
        p1, p2 = random.sample(parents, 2)

        child = (p1 + p2) // 2

        if random.random() < 0.2:
            child = random.randint(0, 31)

        new_population.append(child)

    population = new_population

best = max(population, key=fitness)

print("Best Solution:", best)
print("Maximum Fitness:", fitness(best))