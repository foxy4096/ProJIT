import turtle
import random
import math
delay =0    
score=0

t=turtle.Screen()
t.bgcolor("black")
t.tracer(0)
#creating Boundary
ca=random.choice(["violet","darkgreen","chocolate"])
s=random.choice(["red","skyblue","yellow","lightgreen"])
p=random.choice(["gold","navy","purple","green","cyan","orange"])
k=random.choice(["gold","red","purple","green","cyan","orange"])
mybound=turtle.Turtle()
mybound.color("yellow")
mybound.penup()
mybound.setposition(-300,-300)
mybound.pendown()
mybound.pensize(10)
mybound.hideturtle()
for side in range(4):
    mybound.fd(600)
    mybound.left(90)
#CREATING TURTLE
a=turtle.Turtle()

#x=random.choice(["white","red","purple","green","cyan","yellow"])
a.color(s)
a.shape("arrow")
a.shapesize(2,2,2)
#placing 
a.penup()
a.goto(0,-250)
#a.pendown()
#writing text 1
#pen1=turtle.Turtle()
#pen1.color("red")
#pen1.penup()
#pen1.hideturtle()
#pen1.goto(0,-300)
#pen1.write("Score had been deducted",font=("courier",8,"normal"))
#writing text 2

pen=turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(00,300)
pen.write("ESCAPE LEVEL-01",align="center",font=("courier",8,"normal"))
#Warning for the gamer





# Border Color
bd_1=turtle.Turtle()
bd_1.color(p)
bd_1.shape("square")
bd_1.shapesize(35,23,20)
bd_1.penup()
bd_1.goto(-550,0)
#border color 2
bd_2=turtle.Turtle()
bd_2.color(p)
bd_2.shape("square")
bd_2.shapesize(35,23,20)
bd_2.penup()
bd_2.goto(550,0)
#Elements 1
em_1=turtle.Turtle()
em_1.color("red")
em_1.shape("circle")
em_1.shapesize(1)
em_1.penup()
em_1.speed(0)
em_1.setposition(-100,-100)

#Enemy 1
enem1=turtle.Turtle()
enem1.shape("turtle")
enem1.color(ca)
enem1.shapesize(2)
enem1.penup()
enem1.goto(-290,-40)
#ch_1=random.randint(5,9)
ch_2=random.randint(5,8)
enem1xdirection=ch_2


#Enemy 2


enem2=turtle.Turtle()
enem2.shape("classic")
enem2.color(p)
enem2.shapesize(3)
enem2.penup()
enem2.goto(-290,50)
#ch_2=random.randint(1,5)
enem2xdirection=ch_2

#enemy 3
enem3=turtle.Turtle()
enem3.shape("turtle")
enem3.color(k)
enem3.shapesize(2)
enem3.penup()
enem3.goto(-290,150)
#ch_3=random.randint(5,8)
enem3xdirection=ch_2

#movement
def f():
    a.fd(30)
    
def l():
    a.bk(30)
    
def r():
    a.right(-90)
    
def b():
    a.left(-90)
    
turtle.onkeypress(f,"Left")
turtle.onkeypress(l,"Right")
turtle.onkeypress(r,"Up")
turtle.onkeypress(b,"Down")
turtle.listen()

while True:
    t.update()
    #Moving The enemy
    enem1.setx(enem1.xcor()+enem1xdirection)
    enem2.setx(enem2.xcor()+enem2xdirection)
    enem3.setx(enem3.xcor()+enem3xdirection)
    
      
    if enem1.xcor()>290:
        for i in range(1):
            
            enem1.setx(-290)
     
    if enem2.xcor()>290:
        for i in range(1):
            enem2.setx(-290)
        
    
    if enem3.xcor()>290:
        for i in range(1):
            enem3.setx(-290)
      
    
    
       
    if a.xcor()>300 or a.xcor()<-300:
        a.rt(-90)
#    else:
    

    if a.ycor()>300 or a.ycor()<-300:
        a.rt(-90)
    #1st
    d=math.sqrt(math.pow(enem1.xcor()-a.xcor(),2)+math.pow(enem1.ycor()-a.ycor()-a.ycor(),2))
    if d<100:
        enem1.hideturtle()
        enem1.st()
        score=score+0.25
        enem1.delay=0.2
        pen.clear()
        pen.write("SCORE :{}".format(score),align="center",font=("arial",8,"normal"))
        t.reset()
     #2nd 
    de=math.sqrt(math.pow(enem2.xcor()-a.xcor(),2)+math.pow(enem2.ycor()-a.ycor()-a.ycor(),2))
    if de<80:
      
        enem2.hideturtle()
        
        enem2.st()
      
        enem2.delay=0.2
        pen.clear()
        pen.write("SCORE :{}".format(score),align="center",font=("arial",8,"normal"))
        t.reset()
      #3rd  
    df=math.sqrt(math.pow(em_1.xcor()-a.xcor(),2)+math.pow(em_1.ycor()-a.ycor()-a.ycor(),2))
    if df<100:
        em_1.setposition(random.randint(-200,300),random.randint(-200,300))
        score=score+1
        pen.clear()
        pen.write("SCORE:{}".format(score),align="center",font=("arial",8,"normal"))              
    db=math.sqrt(math.pow(enem3.xcor()-a.xcor(),2)+math.pow(enem3.ycor()-a.ycor()-a.ycor(),2))
    if db<100:
        enem3.hideturtle()
        enem3.st()

        t.reset()
     
                                   
                         
turtle.mainloop()
turtle.done()