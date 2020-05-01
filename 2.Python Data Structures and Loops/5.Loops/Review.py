single_digits = []

for i in range(10):
    single_digits.append(i)

squares = []

for i in single_digits:
    squares.append(i * i)

print(squares)

cubes = [single_digits ** 3 for single_digits in single_digits]

print(cubes)