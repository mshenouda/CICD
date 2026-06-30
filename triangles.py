Python
import math

# Take input from the user
a = float(input("Enter side a: "))
b = float(input("Enter side b: "))
c = float(input("Enter side c: "))

# Calculate the semi-perimeter
s = (a + b + c) / 2

# Calculate the area
area = math.sqrt(s * (s - a) * (s - b) * (s - c))

# Display the result
print(f"The area of the triangle is: {area:.2f}")
