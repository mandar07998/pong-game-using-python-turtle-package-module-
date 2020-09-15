import turtle
import winsound



wn=turtle.Screen()
wn.title("Pong by Mandar")
wn.bgcolor("black")
wn.setup(width=800,height=600)
wn.tracer(0)

# score 
score_a=0
score_b=0


#pen
pen=turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write("player A: 0  player B : 0",align="center",font=("Courier",14,"normal"))


#paddle a
paddle_a=turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.penup()
paddle_a.goto(-350,0)
paddle_a.color("yellow")
paddle_a.shapesize(stretch_wid=5,stretch_len=1)


#paddle b
paddle_b=turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.penup()
paddle_b.goto(350,0)
paddle_b.color("yellow")
paddle_b.shapesize(stretch_wid=5,stretch_len=1)


#pong ball

pong_ball=turtle.Turtle()
pong_ball.speed(0)
pong_ball.shape("circle")
pong_ball.penup()
pong_ball.goto(0,0)
pong_ball.color("red")
pong_ball_dx=0.1
pong_ball_dy=-0.1





#1.now we need to move the paddle_a upwards which we do it by defining a function given below 
def paddle_a_up():
    y=paddle_a.ycor()
    y+=20
    paddle_a.sety(y)
    print(y)

#now call this defined function to move the paddle upwards
#keyboard bindings
wn.listen()
wn.onkeypress(paddle_a_up,"w")


#2.now we need to move the paddle_a downwards
def paddle_a_down():
    y=paddle_a.ycor()
    y-=20
    paddle_a.sety(y)
    print(y)

#keybindings 2
wn.listen()
wn.onkeypress(paddle_a_down,"s")



#3.do the same up and down steps for paddle_b



def paddle_b_up():
    y=paddle_b.ycor()
    y+=20
    paddle_b.sety(y)
    
wn.listen()
wn.onkeypress(paddle_b_up,"p")


#4 down paddle_b

def paddle_b_down():
    y=paddle_b.ycor()
    y-=20
    paddle_b.sety(y)
    
wn.listen()
wn.onkeypress(paddle_b_down,"l")






#main game loop
while True:
    wn.update()


    #move the ball
    pong_ball.setx(pong_ball.xcor()+pong_ball_dx)
    pong_ball.sety(pong_ball.ycor()+pong_ball_dy)

    #border checking for ball to bounce(height is 600)
    if pong_ball.ycor()> 290:
        pong_ball.sety(290)
        pong_ball_dy*=-1
        winsound.PlaySound("bounce.wav",winsound.SND_ASYNC)
        

    if pong_ball.ycor()<-290:
        pong_ball.sety(-290)
        pong_ball_dy*=-1
        winsound.PlaySound("bounce.wav",winsound.SND_ASYNC)    

    if pong_ball.xcor()>390:
        pong_ball.goto(0,0)
        pong_ball_dx*=-1
        score_a +=1
        pen.clear()
        pen.write("player A: {}  player B : {}".format(score_a,score_b),align="center",font=("Courier",14,"normal"))

    if pong_ball.xcor()<-390:
        pong_ball.goto(0,0)
        pong_ball_dx*=-1
        score_b +=1
        pen.clear()
        pen.write("player A: {}  player B : {}".format(score_a,score_b),align="center",font=("Courier",14,"normal"))


    #ball and paddle collisionsp
    if (pong_ball.xcor() > 340 and pong_ball.xcor()< 350) and (pong_ball.ycor() < paddle_b.ycor()+40 and pong_ball.ycor()>paddle_b.ycor() - 40):
        pong_ball.setx(340)
        pong_ball_dx *=-1
        winsound.PlaySound("bounce.wav",winsound.SND_ASYNC)



    if (pong_ball.xcor() < -340 and pong_ball.xcor()> -350) and (pong_ball.ycor() < paddle_a.ycor()+40 and pong_ball.ycor()>paddle_a.ycor() - 40):
        pong_ball.setx(-340)
        pong_ball_dx *=-1
        winsound.PlaySound("bounce.wav",winsound.SND_ASYNC)


