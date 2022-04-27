import turtle

wn = turtle.Screen()
wn.title("Pong")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)

# Pontos de cada jogadar
ponto_a = 0
ponto_b = 0


# Remo A
remo_a = turtle.Turtle()
remo_a.speed(0)
remo_a.shape("square")
remo_a.color("white")
remo_a.shapesize(stretch_wid=5, stretch_len=1)
remo_a.penup()
remo_a.goto(-350, 0)


# Remo B
remo_b = turtle.Turtle()
remo_b.speed(0)
remo_b.shape("square")
remo_b.color("white")
remo_b.shapesize(stretch_wid=5, stretch_len=1)
remo_b.penup()
remo_b.goto(350, 0)


# Bola
bola = turtle.Turtle()
bola.speed(0)
bola.shape("square")
bola.color("white")
bola.penup()
bola.goto(0, 0)
bola.dx = 2
bola.dy = 2


# Tela do placar
placar = turtle.Turtle()
placar.speed(0)
placar.color("white")
placar.penup()
placar.hideturtle()
placar.goto(0, 260)
placar.write("Joagor A: 0 Jogador B: 0", align="center", font=("courier", 24, "normal"))


 
# Função onde vamos mover o remo
def remo_a_cima():
    y = remo_a.ycor()
    y+=20
    remo_a.sety(y)

def remo_a_baixo():
    y = remo_a.ycor()
    y-=20
    remo_a.sety(y)


def remo_b_cima():
    y = remo_a.ycor()
    y+=20
    remo_b.sety(y)

def remo_b_baixo():
    y = remo_b.ycor()
    y-=20
    remo_b.sety(y)



#Entrada do teclado
wn.listen()
wn.onkeypress(remo_a_cima, "w")
wn.onkeypress(remo_a_baixo, "s")
wn.onkeypress(remo_b_cima, "Up")
wn.onkeypress(remo_b_baixo, "Down")



while True:
    wn.update()

    #Mover a bola
    bola.setx(bola.xcor() + bola.dx)
    bola.sety(bola.ycor() + bola.dy)

    # verificar se a bola atingiu a borda
    if bola.ycor() > 290:
        bola.sety(290)
        bola.dy *= -1
    
    if bola.ycor() < -290:
        bola.sety(-290)
        bola.dy *= -1
    
    if bola.xcor() > 350:
        bola.goto(0, 0)
        bola.dx *= -1
        ponto_a+=1
        placar.clear()
        placar.write(f"Joagor A: {ponto_a} Jogador B: {ponto_b}", align="center", font=("courier", 24, "normal"))
    
    if bola.xcor() <-350:
        bola.goto(0, 0)
        bola.dx *= -1
        ponto_b+=1
        placar.clear()
        placar.write(f"Joagor A: {ponto_a} Jogador B: {ponto_b}", align="center", font=("courier", 24, "normal"))

    # Colisão entre a bola e o remo
    if (bola.xcor() > 340 and bola.xcor() < 350) and (bola.ycor() < remo_b.ycor() + 50 and bola.ycor() > remo_b.ycor() - 50):
        bola.setx(340)
        bola.dx *=-1

    if (bola.xcor() < -340 and bola.xcor() > -350) and (bola.ycor() < remo_a.ycor() + 50 and bola.ycor() > remo_a.ycor() - 50):
        bola.setx(-340)
        bola.dx *=-1