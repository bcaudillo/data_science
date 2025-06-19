#Inputs
pizza_input = input('What size of pizza would you like? (Small/Large) ').lower()
topping_input = int(input('How many toppings would you like? '))
miles_input = int(input('How many miles to the delivery destination? '))

#Constants
available_pizza_type = ['small','large']
error_message = 'Please enter a valid response. '
delivery_fee = 2
base_cost = 0

#Calculate base cost
if pizza_input == 'small':
    base_cost = 8
elif pizza_input == 'large':
    base_cost = 12
else: 
    base_cost

#Calculate cost of toppings
if topping_input > 0: 
    topping_cost = topping_input
else:
    topping_cost = 0
    print(error_message)

#Calculate delivery fee
if miles_input > 5:
    miles_input -= 5
    delivery_fee += miles_input
elif miles_input < 5:
    delivery_fee
else: 
    print(error_message)
    delivery_fee = 0

    
#Total calculation
total_cost = base_cost + delivery_fee + topping_cost

#Print response
if pizza_input in available_pizza_type and miles_input != 0:
    print(f"The cost of your {pizza_input} pizza is ${total_cost}.")
else: 
    print('We are unable to process the order. ' + error_message)

