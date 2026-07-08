import random


def validate_boundary_input(prompt):
    while True:
        try:
            boundary = int(input(prompt))
        except ValueError:
            print("Invalid input")
            continue
        return boundary


def get_boundaries():
    lower_boundary = validate_boundary_input("Enter the lower boundary : ")
    upper_boundary = validate_boundary_input("Enter the upper boundary : ")
    return lower_boundary, upper_boundary


def bisection_guess():
    lower_boundary, upper_boundary = get_boundaries()
    secret_number = random.randint(lower_boundary, upper_boundary)

    print(secret_number)
    tries = 0
    while True:
        mid_section = int((upper_boundary + lower_boundary) // 2)
        tries += 1
        if secret_number == mid_section:
            print(f"You got it 💯 => Tries : {tries}")
            break
        if secret_number > mid_section:
            lower_boundary = mid_section
        else:
            upper_boundary = mid_section


def main():
    bisection_guess()


if __name__ == "__main__":
    main()
