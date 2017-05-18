import random


def make_matrix(n, m):
    """
    Make an N rows by M columns matrix
    [
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    ]
    """
    return [[0 for i in range(m)] for i in range(n)]


def between(min, max):
    """
    Return a number between boundary
    """
    return random.random() * (max - min) + min
