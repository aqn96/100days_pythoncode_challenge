def turn_around():
    turn_left()
    turn_left()

def turn_right():
    turn_left()
    turn_left()
    turn_left()

def check_wall():
    move()
    turn_right()
    if wall_in_front():
        turn_left()
    else:
        if not at_goal():
            move()
            turn_right()
    
def jump_hurdle():
    turn_left()
    while front_is_clear():
        check_wall()
    turn_left()
    
while not at_goal():
    if front_is_clear():
        check_wall()
    elif wall_in_front():
        jump_hurdle()
    else:
        move()
        
