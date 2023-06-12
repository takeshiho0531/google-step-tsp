from common import format_tour, read_input

import solver_local_search

CHALLENGES = 2
TRIAL = 200000


def generate_sample_output():
    for i in range(CHALLENGES):
        cities = read_input(f'input_{i}.csv')
        # for solver, name in ((solver_random, 'random')):
        solver=solver_local_search
        tour = solver.solve(cities, TRIAL)
        with open(f'output_{i}.csv', 'w') as f:
            f.write(format_tour(tour) + '\n')


if __name__ == '__main__':
    generate_sample_output()