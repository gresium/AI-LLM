import numpy as np

# Define the states
location_to_state = {
    'L1': 0,
    'L2': 1,
    'L3': 2,
    'L4': 3,
    'L5': 4,
    'L6': 5,
    'L7': 6,
    'L8': 7,
    'L9': 8
}

# Define the actions
actions = [0, 1, 2, 3, 4, 5, 6, 7, 8]

# Define the rewards
rewards = np.array([
    [0, 1, 0, 0, 0, 0, 0, 0, 0],
    [1, 1, 1, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 1, 0, 0, 0, 0],
    [0, 0, 0, 1, 0, 1, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 1, 0, 0],
    [0, 0, 0, 0, 0, 1, 0, 1, 0],
    [0, 0, 0, 0, 0, 0, 1, 0, 1],
    [0, 0, 0, 0, 0, 0, 0, 1, 0]
])

# Reverse mapping from states to locations
state_to_location = dict((state, location) for location, state in location_to_state.items())

# Initialize parameters
gamma = 0.75  # Discount factor
alpha = 0.9   # Learning rate

class QAgent:
    def __init__(self, alpha, gamma, location_to_state, actions, rewards, state_to_location):
        self.gamma = gamma
        self.alpha = alpha
        self.location_to_state = location_to_state
        self.actions = actions
        self.rewards = rewards
        self.state_to_location = state_to_location
        M = len(location_to_state)
        self.Q = np.zeros((M, M))

    def training(self, start_location, end_location, iterations):
        rewards_new = np.copy(self.rewards)
        ending_state = self.location_to_state[end_location]
        rewards_new[ending_state, ending_state] = 999

        for i in range(iterations):
            current_state = np.random.randint(0, 9)
            playable_actions = []

            # Find all actions reachable from current state
            for j in range(9):
                if rewards_new[current_state, j] > 0:
                    playable_actions.append(j)

            # Choose random next state
            next_state = np.random.choice(playable_actions)

            # Temporal Difference
            TD = rewards_new[current_state, next_state] + \
                 self.gamma * self.Q[next_state, np.argmax(self.Q[next_state, :])] - \
                 self.Q[current_state, next_state]

            # Update Q-value
            self.Q[current_state, next_state] += self.alpha * TD

        route = [start_location]
        next_location = start_location
        self.get_optimal_route(start_location, end_location, next_location, route, self.Q)

    def get_optimal_route(self, start_location, end_location, next_location, route, Q):
        while next_location != end_location:
            starting_state = self.location_to_state[start_location]
            next_state = np.argmax(Q[starting_state, :])
            next_location = self.state_to_location[next_state]
            route.append(next_location)
            start_location = next_location
        print(route)

# Example usage
agent = QAgent(alpha, gamma, location_to_state, actions, rewards, state_to_location)
agent.training('L1', 'L9', 1000)

