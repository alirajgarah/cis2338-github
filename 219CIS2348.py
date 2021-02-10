#Ali Rajgarah 1586471

# 1 \\\
lemon_juice = float(input('Enter amount of lemon juice (in cups):\n'))
water_juice = float(input('Enter amount of water (in cups):\n'))
agave_nectar = float(input('Enter amount of agave nectar (in cups):\n'))
servings_size = float(input('How many servings does this make?\n\n'))


print('Lemonade ingredients - yields {:.2f} servings'.format(servings_size))
print('{:.2f} cup(s) lemon juice'.format(lemon_juice))
print('{:.2f} cup(s) water'.format(water_juice))
print('{:.2f} cup(s) agave nectar\n'.format(agave_nectar))

# 2 \\\
desired_servings = float(input('How many servings would you like to make?\n\n'))

print('Lemonade ingredients - yields {:.2f} servings'.format(desired_servings))
print('{:.2f} cup(s) lemon juice'.format(lemon_juice * desired_servings / servings_size))
print('{:.2f} cup(s) water'.format(water_juice * desired_servings / servings_size))
print('{:.2f} cup(s) agave nectar\n'.format(agave_nectar * desired_servings / servings_size))

# 3 \\\
print('Lemonade ingredients - yields {:.2f} servings'.format(desired_servings))
print('{:.2f} gallon(s) lemon juice'.format(lemon_juice * desired_servings / servings_size / 16))
print('{:.2f} gallon(s) water'.format(water_juice * desired_servings / servings_size / 16))
print('{:.2f} gallon(s) agave nectar'.format(agave_nectar * desired_servings / servings_size / 16))
