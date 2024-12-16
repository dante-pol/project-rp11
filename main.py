import math
import functions


is_program_exit = False

while not is_program_exit:

    a = int(input("input a >>"))
    b = int(input("input b >>"))
    c = int(input("input c >>"))

    area = functions.calculate_area(a, b, c)

    print(f"area= {area}")

    user_input = input("Y/N")

    if user_input == "N":
        is_program_exit = True