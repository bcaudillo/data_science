# Import the entire file
import ride

# Import only the Ride class
from ride import 
# Import only the Driver class
from driver import Driver
# Create Passenger class
class Passenger:
    pass

# Two instances of the Passenger class
meryl = Passenger()
daniel = Passenger()

print(meryl)
print(daniel)
 # One instance of the Driver class
flatiron_taxi = Driver()
print(flatiron_taxi)


# Two instances of the Ride class
ride_to_school = Ride()
ride_home = Ride()

print(ride_to_school)
print(ride_home)