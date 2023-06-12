import sys
import random

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

def get_score(path,cities):
    N=len(cities)
    score=0
    for i in range(N):
        score+=distance(cities[path[i]], cities[path[i+1]])
    return score

def solve(cities, trial, initial_path):
    N = len(cities)
    path=initial_path
    path.append(0)

    for i in range(trial):
        print("path",path)
        score=get_score(path,cities)
        left=rand_int(2,N)
        right=rand_int(2, N)
        if (left>right):
            left, right=right, left
        updated_path=path[:left]+path[left:right][::-1]+path[right:]
        print("updated_path",updated_path)
        updated_score=get_score(updated_path, cities)
        if updated_score>=score:
            path=path
        else:
            path=updated_path

    return path[:-1]
