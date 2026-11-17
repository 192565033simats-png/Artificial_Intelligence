# Markov Chain Model

import random

states = ['Sunny', 'Rainy']

# Transition Probability Matrix
transition = {
    'Sunny': [0.8, 0.2],
    'Rainy': [0.4, 0.6]
}

current = 'Sunny'

print("Weather Prediction:")

for i in range(5):
    print(current)

    current = random.choices(
        states,
        weights=transition[current]
    )[0]