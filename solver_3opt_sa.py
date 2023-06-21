import sys
import random
import math

from common import print_tour, read_input
from solver_greedy import distance
import solver_greedy

def rand_int(a: int, b: int) -> int:
    """a以上b以下の整数をランダムに返す関数

    Args:
        a (int): _description_
        b (int): _description_

    Returns:
        int: _description_
    """
    return random.randint(a,b)

def get_distance(path,cities):
    N=len(cities)
    score=0
    for i in range(N):
        score+=distance(cities[path[i]], cities[path[i+1]])
    return score

def update_strategy(original_distance, tmp_updated_distance, index, trial):
    temperature=30-28*index/trial
    probability=math.exp(min(0, (original_distance-tmp_updated_distance)/temperature))
    random_prob=random.random()
    if random_prob<probability:
        return True
    return False


def three_opt(path, N, index, trial):
    rand = [random.randint(2, N) for _ in range(3)]
    sorted_rand = sorted(rand)
    left = sorted_rand[0]
    intermediate = sorted_rand[1]
    right=sorted_rand[2]

    A, B, C, D, E, F = path[left-1], path[left], path[intermediate-1], path[intermediate], path[right-1], path[right]

    original_distance = distance(A,B) + distance(C,D) + distance(E,F)
    distance_candidate1=distance(A,C) + distance(B,D) + distance(E,F)
    distance_candidate2=distance(A,B) + distance(C,E) + distance(D,F)
    distance_candidate3=distance(A,D) + distance(E,B) + distance(C,F)
    distance_candidate4=distance(F,B) + distance(C,D) + distance(E,A)

    if update_strategy(original_distance, distance_candidate1, index, trial):
        path[left:intermediate] = reversed(path[left:intermediate])
        return path
    if update_strategy(original_distance, distance_candidate2, index, trial):
        path[intermediate:right] = reversed(path[intermediate:right])
        return path
    if update_strategy(original_distance, distance_candidate4, index, trial):
        path[left:right] = reversed(path[left:right])
        return path
    if update_strategy(original_distance, distance_candidate3, index, trial):  # TODO
        path[left:right] = reversed(path[left:right])
        path[left:intermediate] = reversed(path[left:intermediate])
        return path


def solve(trial, initial_path):
    N = len(initial_path)-1
    path=initial_path
    path.append(0)

    for index in range(trial):
        path=three_opt(path, N, index, trial)
    return path[:-1]


