import turtle
import winsound

def main():
    try:
        # Main window
        win = turtle.Screen()
        win.setup(width=800, height=600)
        win.title("@xwaynelil pong")
        win.bgcolor("black")
        win.tracer(0)

        # label_a
        label_a = turtle.Turtle()
        label_a.speed(0)
        label_a.color("white")
        label_a.hideturtle()
        label_a.penup()
        label_a.goto(-360, 260)
        label_a.write("A", font=("Times new roman", 15, "bold"))

        # label_b
        label_b = turtle.Turtle()
        label_b.speed(0)
        label_b.color("white")
        label_b.hideturtle()
        label_b.penup()
        label_b.goto(360, 260)
        label_b.write("B", font=("Times new roman", 15, "bold"))

        # Pen
        pen = turtle.Turtle()
        pen.speed(0)
        pen.color("white")
        pen.hideturtle()
        pen.penup()
        pen.goto(-100, 260)
        pen.write("Player A: 0      Player B: 0 ", font=("Times new roman", 12, "bold"))

        # Score
        score_a = 0
        score_b = 0

        # right pad
        pad_r = turtle.Turtle()
        pad_r.shape("square")
        pad_r.color("white")
        pad_r.penup()
        pad_r.goto(360, 0)
        pad_r.shapesize(stretch_wid=5, stretch_len=1)

        # left pad
        pad_l = turtle.Turtle()
        pad_l.shape("square")
        pad_l.color("white")
        pad_l.penup()
        pad_l.goto(-360, 0)
        pad_l.shapesize(stretch_wid=5, stretch_len=1)

        # ball
        ball = turtle.Turtle()
        ball.shape("circle")
        ball.color("white")
        ball.penup()
        ball.goto(0, 0)
        ball.dx = 0.5
        ball.dy = -0.5

        # moving the paddle
        def pad_r_up():
            y = pad_r.ycor()
            y += 20
            pad_r.sety(y)


        def pad_r_down():
            y = pad_r.ycor()
            y -= 20
            pad_r.sety(y)


        def pad_l_up():
            y = pad_l.ycor()
            y += 20
            pad_l.sety(y)


        def pad_l_down():
            y = pad_l.ycor()
            y -= 20
            pad_l.sety(y)


        while True:
            win.update()

            # keyboard binding
            win.listen()
            win.onkeypress(pad_r_up, "Up")
            win.onkeypress(pad_r_down, "Down")
            win.onkeypress(pad_l_up, "w")
            win.onkeypress(pad_l_down, "s")

            # moving yhe ball
            ball.setx(ball.xcor() + ball.dx)
            ball.sety(ball.ycor() + ball.dy)

            # Boarder checking
            #   Top
            if ball.ycor() > 290:
                ball.sety(290)
                ball.dy *= -1
            # Bottom
            if ball.ycor() < -290:
                ball.sety(-290)
                ball.dy *= -1
            # Right
            if ball.xcor() > 390:
                ball.setx(390)
                ball.goto(0, 0)
                ball.dx *= -1
                score_a += 1
                winsound.PlaySound("score", winsound.SND_ASYNC)
                pen.clear()
                pen.write("Player A: {}      Player B: {} ".format(score_a, score_b), font=("Times new roman", 12, "bold"))

            # Left
            if ball.xcor() < -390:
                ball.setx(-390)
                ball.goto(0, 0)
                ball.dx *= -1
                score_b += 1
                winsound.PlaySound("score", winsound.SND_ASYNC)
                pen.clear()
                pen.write("Player A: {}      Player B: {} ".format(score_a, score_b), font=("Times new roman", 12, "bold"))

            # Ball and paddle collision
            if (ball.xcor() > 350 and ball.xcor() < 360) and (ball.ycor() < pad_r.ycor() + 50 and ball.ycor() > pad_r.ycor() - 50):
                ball.setx(350)
                ball.dx *= -1
                winsound.PlaySound("bounce", winsound.SND_ASYNC)

            if (ball.xcor() < -350 and ball.xcor() > -360) and (ball.ycor() < pad_l.ycor() + 50 and ball.ycor() > pad_l.ycor() - 50):
                ball.setx(-350)
                ball.dx *= -1
                winsound.PlaySound("bounce", winsound.SND_ASYNC)

    except:
        print("GAME STOPPED!")
main()












