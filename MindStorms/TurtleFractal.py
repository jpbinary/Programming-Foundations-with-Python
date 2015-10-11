import turtle

def draw_triangle(turtle_name,length):
    # draw a filled-in triangle function
    turtle_name.begin_fill()
    for i in range(3):
        turtle_name.forward(length)
        turtle_name.right(120) # 120 degree turn
    turtle_name.end_fill()

def draw_fractal(turtle_name):
    # draw fractal from triangles
    length = 12
    turtle_name.left(60) # face up and to the right to start
    
    for i in range(240):
        if i == 0:
            draw_triangle(turtle_name,length)
            turtle_name.forward(length)

        # after 24th triangle, start at right of bottom-left triangle    
        elif i % 24 == 0:
            turtle_name.right(180)
            turtle_name.forward(length*4)
            turtle_name.right(120)
            turtle_name.forward(length*3)
            turtle_name.right(180)
            #pause
            draw_triangle(turtle_name,length)          

        # after 12th triangle, start at top of the existing triangle
        elif i % 12 == 0:
            turtle_name.right(120)
            turtle_name.forward(length*5)
            draw_triangle(turtle_name,length)
            
        # after 4th triangle turn right 120 degress before drawing triangle
        elif i % 4 == 0:
            turtle_name.right(120)
            turtle_name.forward(length)
            draw_triangle(turtle_name,length)

        else:
            draw_triangle(turtle_name,length)
            turtle_name.forward(length)            

        
def draw_shapes():
    window = turtle.Screen()
    window.bgcolor("white")

    george = turtle.Turtle()
    george.shape("turtle")
    george.color("red")
    george.speed(100)

    # draw a fractal from triangles
    draw_fractal(george)
    
    window.exitonclick()


draw_shapes()

    
