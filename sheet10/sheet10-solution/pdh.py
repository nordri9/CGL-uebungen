from random import randrange
from itertools import permutations
import math

import matplotlib.pyplot as plt


def total_path_length(path):
    sum = 0
    for i in range(len(path)-1):
        sum += calculate_distance(path[i], path[i+1])
    return sum


def calculate_distance(p1, p2):
    return math.hypot(p2[0] - p1[0], p2[1] - p1[1])


def generate_random_points(n):
    points = list()
    for i in range(n):
        points.append((randrange(100), randrange(100)))

    return points


def pdh(n):

    destinations = generate_random_points(n)

    paths = list(permutations(destinations[1:]))

    distances = list()

    for i in paths:
        distances.append(total_path_length(i))

    # print(distances)

    res = min(distances)
    # print(res)

    shortest_path = 0

    for i in range(len(distances)):
        if distances[i] == res:
            shortest_path = i

    print(shortest_path)

    x_coords, y_coords = zip(*paths[shortest_path])

    x_plot = list(x_coords) + [x_coords[0]]
    y_plot = list(y_coords) + [y_coords[0]]

    plt.plot(x_plot, y_plot, 'ro-')
    plt.savefig("pdh.pdf")
    plt.show()


n_limit = int(input("Enter a limit (N): "))
pdh(n_limit)
