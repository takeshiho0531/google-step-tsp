from common import format_tour, read_input

import solver_sa
import solver_greedy

CHALLENGES = 7
TRIAL = 200000

def generate_output():
    for i in range(CHALLENGES):
        cities = read_input(f'input_{i}.csv')
        solver=solver_sa
        initial_path=solver_greedy.solve(cities)
        tour = solver.solve_sa(cities, TRIAL, initial_path, opt=3)
        with open(f'output_{i}.csv', 'w') as f:
            f.write(format_tour(tour) + '\n')


if __name__ == '__main__':
    generate_output()