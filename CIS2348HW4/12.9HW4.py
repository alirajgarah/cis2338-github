input_names = input().split()
output_names = input_names[0]
while output_names != '-1':
    try:
        age = int(input_names[1]) + 1
    except ValueError:
        age = 0
    print('{} {}'.format(output_names, age))

    input_names = input().split()
    output_names = input_names[0]