import random

lower_boundary = int(input("Enter the lower boundary : "))
upper_boundary = int(input("Enter the upper boundary : "))


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
