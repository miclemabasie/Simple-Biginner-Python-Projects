import sys


def area(length, width):
    return length * width


def perimeter(lenght, widht):
    perimeter = 2 * (lenght + widht)
    return perimeter


def volume(length, widht, height):
    volume = length * widht * height
    return volume


def surface_area(lenght, widht, height):
    surface_area = 2 * (lenght * widht) + 2 * (lenght * height) + 2 * (widht * height)
    print(
        f"SA = 2 * ({lenght} * {widht}) + 2 * ({lenght} * {height}) + 2 * ({widht} * {height})"
    )
    return surface_area
