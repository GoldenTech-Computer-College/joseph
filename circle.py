def circle_area(diameter):
    radius = diameter / 2
    pi = 3.14159
    return pi * radius ** 2

print(f"Area of circle with diameter 10: {circle_area(10)}")

def circle_circumference(diameter):
    radius = diameter / 2
    pi = 3.14159
    return 2 * pi * radius

print(circle_circumference(10))