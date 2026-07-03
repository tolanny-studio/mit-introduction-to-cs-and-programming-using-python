number = int(input("Enter a number "))

_number = number

factorial = 1

while number > 0 :
    factorial  *= number
    number -= 1

print(factorial)

_factorial = 1


for n in range(_number):

    _factorial *= _number
    _number -= 1


print(_factorial)

start = 3
end = 6
total = 0

for _ in range(start,end + 1):
    total +=  _
print(total)