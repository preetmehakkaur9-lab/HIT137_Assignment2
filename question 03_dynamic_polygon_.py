import turtle

def indent_edge(t, length, depth):
    if depth == 0:
        t.forward(length)
    else:
        indent_edge(t, length / 3, depth - 1)
        t.left(60)
        indent_edge(t, length / 3, depth - 1)
        t.right(120)
        indent_edge(t, length / 3, depth - 1)
        t.left(60)
        indent_edge(t, length / 3, depth - 1)

# Set parameters as per the example
sides = 4
length = 300
depth = 3

# Set up the turtle
window = turtle.Screen()
window.title("Geometric Pattern")
t = turtle.Turtle()
t.speed(0)  # Fastest speed

# Position the turtle to center the shape
t.penup()
t.goto(-length / 2, -length / 2)
t.pendown()

# Draw the pattern
for _ in range(sides):
    indent_edge(t, length, depth)
    t.left(360 / sides)

# Keep the window open
turtle.done() 
