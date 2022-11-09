from pythymiodw import *

robot = ThymioReal() # create an object

"""
TO DO 2.1 Move the robot such that it points towards the black zone
"""
robot.wheels(0,50) # make the robot move at same speed on both wheels
robot.sleep(1) # wait for 1 second



while True:
    left_sensor = robot.prox_ground.delta[0]
    right_sensor = robot.prox_ground.delta[1]
    if left_sensor<=80 or right_sensor<=80:
        exit("Reached Blacked")
    else:
        robot.wheels(100,100)
        robot.sleep(0.5)

    """
    TO DO 2.2 Check if the sensors have detected the black zone.
    If yes, stop the robot and exit the loop
    else, then move the robot forward for 0.5 seconds
    Hint: you may want to use a low speed
    """
    pass
     
    
robot.quit() # disconnect communication
