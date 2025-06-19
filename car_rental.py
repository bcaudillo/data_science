days = int(input("How many days do you plan to rent the car?"))
weekend = input("Does the rental include a weekend?(Y/N)")
cost = int(input("How much does the rental cost?"))
rate = cost * days
if weekend == "Y":
    rate = rate * .9
    print(f"the cost of your rental is${rate}")
else:
    print(f"thecost of your rental is ${rate}")