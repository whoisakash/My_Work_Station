from turtle import*
'''corona patter'''
# color("red")
# bgcolor("black")
# speed(11)
# hideturtle()
# b=0
# while b < 250:
#     right(b)
#     forward(b*2)
#     b=b+1

setup(800,800)
speed(15)
bgcolor('black')
r,g,b=255,0,0
for i in range(255*2):
    colormode(255)
    if i<255/3:
        g+=3
    elif i<255*2//3:
        r=3
    elif i<255:
        b+=3
    elif i<255*4//3:
        g-=3
    elif i<255*5//3:
        r+=3
    else:
        b-=3
    fd(60+i)
    rt(91)
    pencolor(r,g,b)
done()
