side_cube = input("Enter the side of the cube: ")

if side_cube.isnumeric():
    side_cube = int(side_cube)
    print("The volume of the cube is: ", side_cube**3)
else:
    print("The side of the cube must be a number")
