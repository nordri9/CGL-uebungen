import random
import matplotlib.pyplot as plt
import numpy as np


def generate_random_point_in_square(length):
    """
    Generate a random point in a square of a given side length centered around the origin with the sides aligned with x- and y-axis.
    """
    return tuple([length*random.uniform(-0.5, 0.5), length*random.uniform(-0.5, 0.5)])


def distance(p1, p2):
    """
    Measures the Euclidean distance between the points p1 and p2 in 2D.
    """
    a = np.array(p1)
    b = np.array(p2)
    d = np.linalg.norm(b-a)
    return d


def point_in_circle(p, center=None, radius=None):
    """
    Checks if the provided point p lies in a circle of a given radius around the provided center.
    """
    p = np.array(p)
    center = np.array(center)
    d = np.linalg.norm(p - center)
    if d < radius:
        return True
    else:
        return False


# TODO: generate a list of 1000 random points in a square of side length 2.0 using generate_random_point_in_square and list comprehension
N = 1000
full_list_of_points = [generate_random_point_in_square(2) for _ in range(N)]

# TODO: generate a list of those points in full_list_of_points that are within a radius of 1.0 of the origin (again using list comprehension)
filtered_list_of_points = [point for point in full_list_of_points if point_in_circle(point, (0, 0), 1.0)]

# TODO: print the ratio of the number of points in filtered_list_of_points to the total number of generated points
N_filtered = len(filtered_list_of_points)
ratio = N_filtered/N
print("ratio", ratio)

# TODO: Generate separate lists of the x- and y-values of full_list_of_points and filtered_list_of_points
x_values_full = np.array(full_list_of_points)[:, 0]
y_values_full = np.array(full_list_of_points)[:, 1]

x_values_filtered = np.array(filtered_list_of_points)[:, 0]
y_values_filtered = np.array(filtered_list_of_points)[:, 1]

plt.scatter(x_values_full, y_values_full)
plt.scatter(x_values_filtered, y_values_filtered)
plt.axis('equal')
plt.savefig('pi_montecarlo_plot.png')
plt.show()
