import random
import matplotlib.pyplot as plt

def generate_random_point_in_square(length):
    """
    Generate a random point in a square of a given side length centered around the origin with the sides aligned with x- and y-axis.
    """
    return tuple([length*random.uniform(-0.5, 0.5), length*random.uniform(-0.5, 0.5)])

def distance(p1, p2):
    """
    Measures the Euclidean distance between the points p1 and p2 in 2D.
    """
    v =[(x1-x2,y1-y2)for x1,y1 in [p1] for x2,y2 in [p2]][0]
    return (v[0]**2+v[1]**2)**0.5

def point_in_circle(p, center=None, radius=None):
    """
    Checks if the provided point p lies in a circle of a given radius around the provided center.
    """
    d = distance(p, center)
    return d < radius


# TODO: generate a list of 10000 random points in a square of side length 2.0 using generate_random_point_in_square and list comprehension
n = 100000
full_list_of_points = [generate_random_point_in_square(2) for i in range(n)]

# TODO: generate a list of those points in full_list_of_points that are within a radius of 1.0 of the origin (again using list comprehension)
filtered_list_of_points = [i for i in full_list_of_points if point_in_circle(i,(0,0),1.0)]
#print(filtered_list_of_points)
# TODO: print the ratio of the number of points in filtered_list_of_points to the total number of generated points

print("ratio:",len(filtered_list_of_points)/n)

# TODO: Generate separate lists of the x- and y-values of full_list_of_points and filtered_list_of_points
x_values_full = [x for x,y in full_list_of_points]
y_values_full = [y for x,y in full_list_of_points]

x_values_filtered = [x for x,y in filtered_list_of_points]
y_values_filtered = [y for x,y in filtered_list_of_points]

plt.scatter(x_values_full, y_values_full)
plt.scatter(x_values_filtered, y_values_filtered)
plt.axis("equal")
plt.savefig("pi_montecarlo_plot.pdf")
plt.show()
