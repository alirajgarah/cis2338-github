#Ali Rajgarah 1586471

user_input = input()
sNoSpaces = ""
for x in user_input:
    if x!=' ':
        sNoSpaces += x
sReverse = ""
for x in sNoSpaces:
    sReverse=x+sReverse
if (sNoSpaces==sReverse):
    print(user_input + " is a palindrome")
else:
    print(user_input + " is not a palindrome")