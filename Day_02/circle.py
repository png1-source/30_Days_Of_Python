import math # Calculating the area and circumference of a circle using the math module

radius_of_circle = int(input("Enter the radius of the circle: "))
area_of_circle = math.pi * radius_of_circle ** 2
circumference_of_circle = 2 * math.pi * radius_of_circle
print(f'The area of the circle is: {area_of_circle}')
print(f'The circumference of the circle is: {circumference_of_circle}')