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

def two_opt(path, N):
    print("path",path)

    left=rand_int(2,N)
    right=rand_int(2, N)
    if (left>right):
        left, right=right, left
    updated_path=path[:left]+path[left:right][::-1]+path[right:]
    print("updated_path",updated_path)

    return path, updated_path


def reverse_segment_if_better(tour, i, j, k):
    """If reversing tour[i:j] would make the tour shorter, then do it."""
    # Given tour [...A-B...C-D...E-F...]
    A, B, C, D, E, F = tour[i-1], tour[i], tour[j-1], tour[j], tour[k-1], tour[k % len(tour)]
    d0 = distance(A, B) + distance(C, D) + distance(E, F)
    d1 = distance(A, C) + distance(B, D) + distance(E, F)
    d2 = distance(A, B) + distance(C, E) + distance(D, F)
    d3 = distance(A, D) + distance(E, B) + distance(C, F)
    d4 = distance(F, B) + distance(C, D) + distance(E, A)

    if d0 > d1:
        tour[i:j] = reversed(tour[i:j])
        return -d0 + d1
    elif d0 > d2:
        tour[j:k] = reversed(tour[j:k])
        return -d0 + d2
    elif d0 > d4:
        tour[i:k] = reversed(tour[i:k])
        return -d0 + d4
    elif d0 > d3:
        tmp = tour[j:k] + tour[i:j]
        tour[i:k] = tmp
        return -d0 + d3
    return 0


def three_opt(path, N):
    left, intermediate, right =hoge()






def solve(cities, trial, initial_path):
    N = len(cities)
    path=initial_path
    path.append(0)

    for i in range(trial):
        path, updated_path=two_opt(path, N)
        distance=get_distance(path,cities)
        updated_distance=get_distance(updated_path, cities)
        temperature=30-28*i/trial
        probability=math.exp(min(0, (distance-updated_distance)/temperature))

        random_prob=random.random()
        if random_prob<probability:
            path=updated_path

    return path[:-1]
