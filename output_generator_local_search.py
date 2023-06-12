from common import format_tour, read_input

import solver_local_search
import solver_greedy

CHALLENGES = 2
TRIAL = 200000


def generate_output():
    for i in range(CHALLENGES):
        cities = read_input(f'input_{i}.csv')
        solver=solver_local_search
        initial_path=solver_greedy.solve(cities)
        tour = solver.solve(cities, TRIAL, initial_path)
        with open(f'output_{i}.csv', 'w') as f:
            f.write(format_tour(tour) + '\n')


if __name__ == '__main__':
    generate_sample_output()