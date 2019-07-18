#change of X by small increments so it wont teleport
# it keeps going until it collides with one of the sides so you need to know how long your background is
#change X in opposite direction so it seems to "bounce"
ball_x = 10
ball_y = 20
ball_diameter = 10
ball_x_speed = 1
ball_y_speed = 1
rect_x=450
rect_width=30
rect_height=70
y=10

    
def setup():
    global d,y
    size(500,500)
    y=20
    speed=10
    d=speed


def draw():
    #local can only be used in one area, while global can be used all over the code. Global=confined to a scope. Everything with the same indentention as global is in globals scope.
    global y,d,ball_y, ball_x_speed, ball_y_speed, ball_diameter, ball_x, rect_x
    background(125)
    ellipse (ball_x, ball_y, ball_diameter,ball_diameter)
    rect(rect_x,mouseY,rect_width,rect_height)
    
#ball speed

    ball_x=ball_x+ball_x_speed
    ball_y=ball_y+ball_y_speed
    
    if ball_y < 0 or ball_y> 500:
        ball_y_speed= ball_y_speed * -1
        d=-1
#is x=500? Yes? D=-1. Is X not equal to 500? no. Yes. IS X equal to zero? Yes? d=+1. Is X not equal to 0? no? Do nothing.
    elif y <=0:
        d=+1

#make ball bounce off paddle
