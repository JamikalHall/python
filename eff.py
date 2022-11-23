#generate an F shape
numbers = [5, 2, 5, 2, 2]
for value in numbers:
    output = ''
    for total in range(value):
        output += "x"
    print(f"{output}")
