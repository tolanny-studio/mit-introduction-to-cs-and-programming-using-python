import random


def validate_boundary_input(prompt):
    while True:
        try:
            boundary = int(input(prompt))
        except ValueError:
            print("Invalid input. Please retry🔄️")
            continue
        if boundary < 1:
            print("Invalid Input.The number should be greater than 0 (x > 0). Please retry🔄️")
            continue
        return boundary


def get_boundaries():
    while True:
        lower_boundary = validate_boundary_input("Enter the lower boundary (x1 > 0): ")
        upper_boundary = validate_boundary_input(
            "Enter the upper boundary (0 < x2 > x1): "
        )

        if lower_boundary > upper_boundary:
            print(
                f"Lower boundary {lower_boundary} is greater than upper boundary {upper_boundary}. Please retry🔄️"
            )
            continue
        if lower_boundary == upper_boundary:
            print(
                f"Lower boundary {lower_boundary} is equal to upper boundary {upper_boundary}. Please retry🔄️"
            )
            continue
        return lower_boundary, upper_boundary


def bisection_guess():
    lower_boundary, upper_boundary = get_boundaries()
    secret_number = random.randint(lower_boundary, upper_boundary)

    tries = 0
    while True:
        mid_section = int((upper_boundary + lower_boundary) // 2)
        tries += 1
        if secret_number == mid_section:
            print(f"You got it 💯")
            print(f"Number : {secret_number}")
            print(f"Tries : {tries}")
            break
        if secret_number > mid_section:
            lower_boundary = mid_section
        else:
            upper_boundary = mid_section


def main():
    bisection_guess()


if __name__ == "__main__":
    main()
