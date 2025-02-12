
## Reeborg's World MAZE Created Solution:
"""
def turn_right():
    turn_left()
    turn_left()
    turn_left()
        
state = True;
while(state):
    if(at_goal()):
        state = False
    elif(right_is_clear()):
        turn_right()
        move()
    elif(front_is_clear()):
        move()
    elif(wall_in_front()):
        turn_left()
        
"""