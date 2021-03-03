#Ali Rajgarah 1586471

def exact_change(total_change):
    dollars = total_change // 100
    total_change %= 100
    quarters = total_change // 25
    total_change %= 25
    dimes = total_change // 10
    total_change %= 10
    nickels = total_change // 5
    total_change %= 5
    pennies = total_change
    return dollars, quarters, dimes, nickels, pennies


if __name__ == '__main__':
    input_val = int(input())
    numdollars, numquarters, numdimes, numnickels, numpennies = exact_change(input_val)
    if input_val <= 0:
        print('no change')
    else:
        if numdollars > 1:
            print('%d dollars' % numdollars)
        elif numdollars == 1:
            print('%d dollar' % numdollars)

        if numquarters > 1:
            print('%d quarters' % numquarters)
        elif numquarters == 1:
            print('%d quarter' % numquarters)

        if numdimes > 1:
            print('%d dimes' % numdimes)
        elif numdimes == 1:
            print('%d dime' % numdimes)

        if numnickels > 1:
            print('%d nickels' % numnickels)
        elif numnickels == 1:
            print('%d nickel' % numnickels)

        if numpennies > 1:
            print('%d pennies' % numpennies)
        elif numpennies == 1:
            print('%d penny' % numpennies)