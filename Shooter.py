import random
import turtle
from turtle import Screen, Turtle


screen = Screen()
alex = Turtle("turtle")

def mouseClick(x,y):
  lowerX = circleX - radius
  lowerY = circleY
  upperX = circleX + radius
  upperY = circleY + (2 * radius)

  if(x >= lowerX and x <= upperX and y >= lowerY and y<= upperY):
    global sum
    sum = sum + 10
    print("Good Job! You have scored",sum,"points")
    

def dummyclick(x,y):
  a = 0 



def main():
  turtle.listen()
  turtle.onscreenclick(mouseClick,1)
  



Colors = ["green","red","blue","pink","magenta","yellow","orange","black","cyan"]
sum = 0
main()
for i in range(30):
    alex.speed(10)
    radius = random.randrange(10,20)
    circleX = random.randrange(-130,130)
    circleY = random.randrange(-130,130)
    centerX = circleX
    centerY = circleY + radius 
    index = random.randrange(0,8)
    alex.up()
    alex.goto(circleX,circleY)
    alex.down()
    alex.clear()
    alex.fillcolor(Colors[index])
    alex.begin_fill()
    alex.circle(radius)
    alex.end_fill()

turtle.onscreenclick(dummyclick,1)  
print("Your total score is",sum,"Well done!")
bob = input()
