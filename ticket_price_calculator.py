age = int(input("How old are you?: "))
movie_type = input("regular or premium?").lower()

if age <= 12:
    cost = [8,10]
    if movie_type == "regular":
        print (cost[0])
    else:
        print(cost[1])
elif age >= 13 and age <= 59:
    cost = [12,15]
    if movie_type == "regular":
        print (cost[0])
    else:
        print(cost[1])
else:
    cost = [10,12]
    if movie_type == "regular":
        print(cost[0])
    else:
        print(cost[1])
    