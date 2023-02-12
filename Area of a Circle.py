#Area of a Circle: Write a program that calculates the area of a circle given its radius.

# Program to find the area of a circle

# Function to calculate the area
def area_of_circle(radius):
    return 3.14 * radius * radius

# Input radius from the user
radius = float(input("Enter the radius of the circle: "))

# Call the function and print the result
result = area_of_circle(radius)
print("The area of the circle with radius", radius, "is", result)
