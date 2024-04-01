from pynput import mouse,keyboard
import random,time

mouse_ctrl = mouse.Controller()
keyboard_ctrl = keyboard.Controller()

def mousemove():
    '''Move mouse using random delta x and delta y, then click middle button twice.'''
    cur_x,cur_y = mouse_ctrl.position
    delta_x = random.randint(-50,50)
    delta_y = random.randint(-50,50)
    mouse_ctrl.position = (cur_x+delta_x,cur_y+delta_y)
    print("moving to"+str(mouse_ctrl.position))
    mouse_ctrl.click(mouse.Button.middle,2)

def keyboard_listener():
    '''If no key is pressed in 5 seconds, move the mouse.''' 
    with keyboard.Events() as events:
        #print(events.get(5))
        if events.get(5) is not None:
            for event in events:
                    print("pressed"+str(event.key))
                    return True
        else:
            mousemove()

while True:
    keyboard_listener()
    time.sleep(120)#sleep for 2 minutes to avoid too many operations(this will also make Teams think you are not idle.)