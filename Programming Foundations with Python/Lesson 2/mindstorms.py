import turtle

def draw_square():
  ## window is my screen
  window = turtle.Screen()
  window.bgcolor("green")
  i = 0
  Parker = turtle.Turtle()
  ## no there is not a screen import it is a function in turtle...
  window.register_shape("parker.gif")
  Parker.shape("parker.gif")
  Parker.pencolor("brown")
  Parker.fill(True)
  i = 0
  while(i< 4):
    ## parker's my dog but now here Parker listens. 
    Parker.left(90)
    Parker.forward(100)
    i = i + 1
  
  Parker.penup()
  Parker.right(90)
  Parker.forward(100)
  Parker.fill(False)
  window.exitonclick()

draw_square()  
