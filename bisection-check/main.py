import random


def validate_boundary_input(prompt):
    """Prompt the user until they enter a positive integer."""
    while True:
        try:
            boundary = int(input(prompt))
        except ValueError:
            print("Invalid input. Please retry🔄️")
            continue

        if boundary < 1:
            print(
                "Invalid Input. The number should be greater than 0 (x > 0). Please retry🔄️"
            )
            continue

        return boundary


def get_boundaries():
    """Prompt the user for valid lower and upper search boundaries."""
    while True:
        lower_boundary = validate_boundary_input("Enter the lower boundary (x1 > 0): ")
        upper_boundary = validate_boundary_input(
            "Enter the upper boundary (0 < x2 > x1): "
        )

        # Ensure the lower boundary is strictly less than the upper boundary.
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


def play_bisection_game():
    """Generate a random number and locate it using the bisection (binary search) algorithm."""
    lower_boundary, upper_boundary = get_boundaries()

    # Generate a random secret number within the chosen range.
    secret_number = random.randint(lower_boundary, upper_boundary)

    guesses = 0

    # Continue searching while there is still a valid search interval.
    while lower_boundary <= upper_boundary:
        # Calculate the midpoint of the current search range.
        mid_section = (upper_boundary + lower_boundary) // 2

        print(f"Range: {lower_boundary}-{upper_boundary}")
        print(f"Middle: {mid_section}")

        guesses += 1

        # Stop once the secret number has been found.
        if secret_number == mid_section:
            print("You got it 💯")
            print(f"Number: {secret_number}")
            print(f"Guess(es): {guesses}")
            break

        # Eliminate the half of the search range that cannot contain the secret number.
        if secret_number > mid_section:
            lower_boundary = mid_section + 1
        else:
            upper_boundary = mid_section - 1


def main():
    """Run the program."""
    play_bisection_game()


if __name__ == "__main__":
    main()