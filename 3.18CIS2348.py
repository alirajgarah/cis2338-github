import math

# 1 \\\

wall_height = int(input("Enter wall height (feet):\n"))

wall_width = int(input("Enter wall width (feet):\n"))

wall_area = wall_height * wall_width

# 2 \\\

paint_cans = wall_area / 350


num_cans = math.ceil(paint_cans)

cost_paint={'red':35,'blue':25,'green':23}

print("Wall area: " + str(wall_area) + " square feet")
print("Paint needed: {:.2f} gallons".format(paint_cans))


# 3 \\\

print("Cans needed: " + str(num_cans) + " can(s)")

# 4 \\\

color_ofwall=input("\nChoose a color to paint the wall:\n")

total_price=num_cans * cost_paint[color_ofwall.lower()]

print ("Cost of purchasing " + str(color_ofwall) + " paint: $" + str(total_price))