#change of X by small increments so it wont teleport
# it keeps going until it collides with one of the sides so you need to know how long your background is
#change X in opposite direction so it seems to "bounce"
def setup():
    global x,d
    size(500,500)
    x=0
    d=1
    
def draw():
    #local can only be used in one area, while global can be used all over the code. Global=confined to a scope. Everything with the same indentention as global is in globals scope.
    global x,d
    background(125)
    ellipse(x,400,40,40)
    x=x+d
    if x==500:
        d=-1
#is x=500? Yes? D=-1. Is X not equal to 500? no. Yes. IS X equal to zero? Yes? d=+1. Is X not equal to 0? no? Do nothing.
    elif x <=0:
        d=+1
   
