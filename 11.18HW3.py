#Ali Rajgarah 1586471

integer_list = list(map(int, input().split()))
output_list = []

for i in integer_list:
    if i >= 0:
        output_list.append(i)

output_list.sort()

print(*output_list, end = " ")
