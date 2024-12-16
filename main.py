import math
import functions


is_program_exit = False

while not is_program_exit:

    a_text = input("input a >>")
    b_text = input("input b >>")
    c_text = input("input c >>")

    while not functions.validate_text(a_text, b_text, c_text):
        print("system >> Error! Value error not validated!")

        a_text = input("input a >>")
        b_text = input("input b >>")
        c_text = input("input c >>")

    a = float(a_text)
    b = float(b_text)
    c = float(c_text)

    area = functions.calculate_area(a, b, c)

    print(f"area= {area}")

    user_input = input("Y/N")

    if user_input == "N":
        is_program_exit = True

print("Bye!")