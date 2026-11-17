# Reinforcement Learning using Q-Learning

import numpy as np
import random

# Environment
states = 5
actions = 2

Q = np.zeros((states, actions))

alpha = 0.1
gamma = 0.9
epsilon = 0.1

for episode in range(100):
    state = 0

    while state != 4:

        if random.random() < epsilon:
            action = random.randint(0, 1)
        else:
            action = np.argmax(Q[state])

        next_state = min(state + 1, 4)

        reward = 10 if next_state == 4 else -1

        Q[state, action] += alpha * (
            reward + gamma * np.max(Q[next_state])
            - Q[state, action]
        )

        state = next_state

print("Learned Q-Table:")
print(Q)