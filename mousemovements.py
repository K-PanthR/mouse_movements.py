import pgzrun

WIDTH: 600
HEIGHT: 600
Points = []
Click = False

def draw():
    screen.clear()
    screen.fill("Black")
    for i in range(len(Points)-1):
        screen.draw.line(Points[i], Points[i+1],"White")

def update():
    pass

def on_mouse_down():
    global Click
    Click= True

def on_mouse_up():
    global Click
    Click= False
    
def on_mouse_move(pos):
    if Click:
        Points.append(pos)

pgzrun.go()