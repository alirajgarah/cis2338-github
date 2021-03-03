#Ali Rajgarah 1586471

char1 = int(input())
char2 = int(input())
char3 = int(input())
char4 = int(input())
char5 = int(input())
char6 = int(input())

integer_solution = False

for x in range(-10, 11):
    for y in range(-10, 11):
        if char1 * x + char2 * y == char3 and char4 * x + char5 * y == char6:
            print(x, y)
            integer_solution = True

if not integer_solution:
    print("No solution")