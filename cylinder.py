def area(diameter, height):
    radius = diameter / 2
    part1 = 2 * 3.142 * radius ** 2
    part2 = 3.142 * diameter * height
    return part1 + part2

print(f"The area of the cylinder with diameter 10 and height 20 is {area(10, 20)}")

def volume(diameter, height):
    radius = diameter / 2
    return 3.142 * radius ** 2 * height

print(f"The volume of the cylinder with diameter 10 and height 20 is {volume(10, 20)}")