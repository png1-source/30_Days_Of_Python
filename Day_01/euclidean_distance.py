point_1 = (1, 2) # This is the first point in 2D space
point_2 = (4, 6) # This is the second point in 2D space

from math import dist # This function calculates the Euclidean distance between two points in n-dimensional space
distance = dist(point_1, point_2)
print(f"The Euclidean distance between {point_1} and {point_2} is: {distance}")