pie = 3.14  # Global variable for circle area calculation

def linear_equation():
# Solves a linear equation of the form ax + b = c
    a = float(input("Enter the value of 'a': "))
    b = float(input("Enter the value of 'b': "))
    c = float(input("Enter the value of 'c': "))
    
    if a == 0:
        if b == c:
            print("Infinite solutions (any x)")
        else:
            print("No solution")
    else:
        x = (c - b) / a
        print(f"The solution is x = {x}")

def calculate_shapes():
    """Calculates both area and volume (where applicable) for various shapes."""

    print('1. Triangle (Area only)')
    print('2. Rectangle (Area only)')
    print('3. Circle (Area only)')
    print('4. Square (Area and Volume)')
    print('5. Rhombus (Area only)')
    print('6. Cube (Volume only)')
    print('7. Linear Equation (ax + b = c)')

    num = int(input('Enter your choice (hint: Enter the serial numbers): '))

    if num == 1:
        triangle_area()
    elif num == 2:
        rectangle_area()
    elif num == 3:
        circle_area()
    elif num == 4:
        square_area_and_volume()
    elif num == 5:
        rhombus_area()
    elif num == 6:
        cube_volume()
    elif num == 7:
        linear_equation()
    else:
        print("Invalid choice. Please enter a number between 1 and 7.")

def triangle_area():
    """Calculates the area of a triangle."""
    l = float(input("Enter the height: "))
    b = float(input("Enter the base: "))
    area = 1/2 * l * b
    print(f"Area of the triangle is {area}")

def rectangle_area():
    """Calculates the area of a rectangle."""
    l = float(input("Enter the height: "))
    b = float(input("Enter the breadth: "))
    area = l * b
    print(f"Area of the rectangle is {area}")

def circle_area():
    """Calculates the area of a circle."""
    r = float(input("Enter the radius: "))
    area = pie * r * r
    print(f"Area of the circle is {area}")

def square_area_and_volume():
    """Calculates both area and volume of a square."""
    a = float(input("Enter the side of the square: "))
    area = a * a
    volume = a * a * a  # Calculate volume as well
    print(f"Area of the square is {area}")
    print(f"Volume of the square is {volume}")

def rhombus_area():
    """Calculates the area of a rhombus."""
    d1 = float(input("Enter the first diagonal: "))
    d2 = float(input("Enter the second diagonal: "))
    area = d1 * d2 / 2
    print(f"Area of the rhombus is {area}")

def cube_volume():
    """Calculates the volume of a cube."""
    side = float(input('Enter the side of the cube: '))
    volume = side * side * side
    print(f'The volume of the cube is {volume}.')

# Call the main function to start the program
calculate_shapes()
