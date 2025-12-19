# website - https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Maze&url=worlds%2Ftutorial_en%2Fmaze1.json

def turn_right():
    turn_left()
    turn_left()
    turn_left()  

while not at_goal():
    if right_is_clear():
        turn_right()
        while front_is_clear():
            move()
            turn_left()
            if front_is_clear():
                while front_is_clear():
                    move()
            else:
                turn_right()
                while front_is_clear():
                    move()
                    turn_left()
                    if front_is_clear():
                        move()
                    else:
                        turn_right()
    elif wall_on_right():
        if front_is_clear():
            while front_is_clear():
                move()
        elif wall_in_front():
            turn_left()
            while front_is_clear():
                move()
            
