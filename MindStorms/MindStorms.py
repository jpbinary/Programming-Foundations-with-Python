import turtle

def draw_square(turtle_name):
    # draw a square function
    for i in range(4):
        turtle_name.forward(100)
        turtle_name.right(90) # 90 degree turn

def draw_circle_from_squares(turtle_name):
    # draw a circle from squares function
    # 360 since 360 degress in a circle
    for i in range(360):
        turtle_name.speed(100)
        draw_square(turtle_name)
        # after drawing a square, turn right 1 extra degree, before drawing another square
        turtle_name.right(1)
        
def draw_shapes():
    window = turtle.Screen()
    window.bgcolor("white")

    # draw a square
    simon = turtle.Turtle()
    simon.shape("turtle")
    simon.color("green")
    simon.speed(2)
    draw_square(simon)

    # draw a circle
    seri = turtle.Turtle()
    seri.shape("arrow")
    seri.color("blue")
    seri.circle(100)
    seri.speed(3)

    sam = turtle.Turtle()
    sam.shape("square")
    sam.color("red")
    sam.speed(4)

    # draw a triangle
    sam_count = 0
    while sam_count < 3:
        sam.forward(100)
        sam.right(120)
        sam_count += 1

    # draw a circle from squares
    draw_circle_from_squares(simon)
    
    window.exitonclick()


draw_shapes()

    
