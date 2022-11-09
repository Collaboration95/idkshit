from pythymiodw import *

robot = ThymioReal() # create an object

"""
TO DO 2.3 Initialize some variables
dt: is how long you want the sleep command to run
travel_time: a variable that keeps track of the travelling time.
What should its starting value be? 
time_limit:  how long you want the robot to travel before it stops 
"""

dt = 4 
travel_time = 0
time_limit = 10


while True:
    left_sensor = robot.prox_ground.delta[0]
    right_sensor = robot.prox_ground.delta[1]
    if left_sensor<=80 or right_sensor<=80:
        robot.sleep(dt)
    pass 
     
    
robot.quit() # disconnect communication