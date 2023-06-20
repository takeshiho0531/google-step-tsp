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




def three_opt(path, N):
    rand = [random.randint(2, N) for _ in range(3)]
    sorted_rand = sorted(rand)
    left = sorted_rand[0]
    intermediate = sorted_rand[1]
    right=sorted_rand[2]

    # A, B, C, D, E, F = path[left-1], path[left], path[intermediate-1], path[intermediate], path[right-1], path[right]

    path1=path.copy()
    path1[left:intermediate] = reversed(path1[left:intermediate])

    path2=path.copy()
    path2[intermediate:right] = reversed(path2[intermediate:right])

    path3=path.copy()
    path3[left:right] = reversed(path3[left:right])

    return [(path, path1), (path, path2), (path, path3)]






def solve_sa(cities, trial, initial_path, opt:int):
    N = len(cities)
    path=initial_path
    path.append(0)


    if opt==2:
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

    if opt==3:
        for i in range(trial):
            for j in range(3):
                path, updated_path=three_opt(path, N)[j]
                distance=get_distance(path,cities)
                updated_distance=get_distance(updated_path, cities)
                temperature=30-28*i/trial
                probability=math.exp(min(0, (distance-updated_distance)/temperature))
                random_prob=random.random()
                if random_prob<probability:
                    out_of_inner_roop_path=updated_path
                    break
                else:
                    out_of_inner_roop_path=path
            path=out_of_inner_roop_path
            print(path)
        return path[:-1]

