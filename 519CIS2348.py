#Ali Rajgarah 1586471

def CostofService(s):
    if s == "Oil change":
        return 35
    if s == "Tire rotation":
        return 19
    if s == "Car wash":
        return 7
    if s == "Car wax":
        return 12

print("Davy's auto shop services\n"
      "Oil change -- $35\n"
      "Tire rotation -- $19\n"
      "Car wash -- $7\n"
      "Car wax -- $12\n")

service_one = input("Select first service:\n")
service_two = input("Select second service:\n")

print("\nDavy's auto shop invoice\n")

firstinput = CostofService(service_one)
secondinput = 0
print("Service 1: %s, $%d" % (service_one, firstinput))

if service_two == '-':
    print("Service 2: No service")
else:
    two = CostofService(service_two)
print("Service 2: %s, $%d" % (service_two, secondinput))

print("\nTotal: $%d" % (firstinput + secondinput))