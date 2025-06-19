class Robot:
  # Essentially a blank template since we never defined any attributes
  pass

# Instantiate the object
my_robot = Robot()
type(my_robot)


 # My little army of many robots
robot_army = [Robot() for _ in range(5)]
robot_army

# Remember each robot is an individual, a special snowflake ❄️
robot_army[0] is robot_army[1]

