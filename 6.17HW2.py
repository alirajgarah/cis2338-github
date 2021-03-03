#Ali Rajgarah 1586471

password = input()

strong_password = ''

i = 0
while i < len(password):
    character = password[i]
    if character == 'i':
        strong_password += '!'
    elif character == 'a':
        strong_password += '@'
    elif character == 'm':
        strong_password += 'M'
    elif character == 'B':
        strong_password += '8'
    elif character == 'o':
        strong_password += '.'
    else:
        strong_password += character
    i += 1

strong_password += "q*s"

print(strong_password)