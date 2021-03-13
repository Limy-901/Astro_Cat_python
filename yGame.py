import turtle as t
import random
import time

s = t.Screen(); s.setup(1500,800); t.bgcolor("white")
StampN = 0 ; FirstPlay = 0; mxPose = 0; myPose = 0

def mainF():
    t.ht(); t.penup(); t.setposition(-400, 0)
    t.write(" \" 우주에서 길을 잃은 고양이를 데리고 지구로 돌아오세요! \" ",font=("KCC-은영체",40))
    time.sleep(3); t.ht(); t.clear() 
    s.bgpic('bg1.gif'); s.update()
    time.sleep(0.5)
    main.setposition(0,-70); main.st() # 고양이등장
    global FirstPlay; FirstPlay = 0
    if FirstPlay == 0:
        t.onkeypress(firstGame, "space")

def firstGame(): # 도망다니면서 별모으기.
    def r(): main.setheading(0)  # 조종
    def u(): main.setheading(90)
    def l(): main.setheading(180)
    def d(): main.setheading(270)
    t.onkeypress(r, "Right")  # 키보드 조종 연결
    t.onkeypress(u, "Up")
    t.onkeypress(l, "Left")
    t.onkeypress(d, "Down")

    global FirstPlay
    FirstPlay += 0.5
    s.bgpic('bgg.gif'); s.update()
    t.ht(); t.penup(); t.setposition(-280, 30); t.color("white")
    t.write(" \" 외계인을 피해서 별을 모아보자 ! \" ", font=("KCC-은영체",40))
    alien = t.Turtle(); stars = t.Turtle(); alien.ht(); stars.ht(); 
    alien.up(); alien.shape(Enemy); alien.speed(0); alien.goto(400, 200)
    stars.speed(0); stars.up(); stars.shape(item); stars.goto(-400, 200)
    main.up()
    time.sleep(2); t.clear(); t.ht()
    alien.st(); stars.st()
    def goOn():
        global StampN
        if StampN >= 1: # 아이템 5개 먹으면,
            t.clear(); t.ht(); t.setposition(-250,0)
            t.write(" \" 첫번째 게임, 성공! \" ", font=("KCC-은영체",50))
            time.sleep(2)
            if FirstPlay == 0.5: 
                SecondGame(); return
        main.forward(12); alien.forward(5); angle = alien.towards(main.pos()); alien.setheading(angle)
        if main.distance(alien) > 12: # 안잡히면 반복
            t.ontimer(goOn, 100)
        else:
            Stop()
        if main.distance(stars) < 12: 
            tfx = random.randint(-400,250); tfy = random.randint(-400,250); stars.goto(tfx, tfy)
            StampN += 1
            main.color("white")
            main.write(str(StampN)+"개!",False,font=("KCC-은영체",50))
    goOn()

def SecondGame(): # 하늘에 떠있는 원을 제대로 클릭할때, forward하기.
    t.clearscreen(); s.bgpic('bg3.gif'); s.update(); t.ht(); t.penup(); t.setposition(-350,-20)
    sShip = t.Turtle(); sShip.ht(); sShip.up(); sShip.setposition(600,0); 
    
    sShip.shape(ship); sShip.st()
    t.write(" \" 뺏기지 않게 먼저 우주선에 도착하자 ! \" ", font=("KCC-은영체",40))
    # time.sleep(3); 
    t.clear(); t.ht()
    

    r1 = t.Turtle(); r1.ht(); r1.up(); r1.shape(Enem1); r1.setposition(-650,-50); r1.st()
    r2 = t.Turtle(); r2.ht(); r2.up(); r2.shape(Enem2); r2.setposition(-620,-100); r2.st()
    r3 = t.Turtle(); r3.ht(); r3.up(); r3.shape(Enem3); r3.setposition(-570,-150); r3.st()
    main2 = t.Turtle(); main2.ht(); main2.up(); main2.shape(mCharacter); main2.setposition(-600,-200); main2.st()

    stepX = random.choice(range(-600,600)); stepY = random.choice(range(-300,300))

    step1= t.Turtle(); step1.ht();  step1.up();  step1.shape('circle')
    step2= t.Turtle(); step2.ht();  step2.up();  step2.shape('circle')
    step3= t.Turtle(); step3.ht();  step3.up();  step3.shape('circle')
    step4= t.Turtle(); step4.ht();  step4.up();  step4.shape('circle')
    step5= t.Turtle(); step5.ht();  step5.up();  step5.shape('circle')

    def LevelSet():
        step1.setposition(stepX,stepY); step1.st()
    def Running():
        global StampN
        rs1=random.randint(1,10); rs2=random.randint(1,10); rs3=random.randint(1,10)
        r1.forward(rs1); r2.forward(rs2); r3.forward(rs3); main2.forward(9) # 움직이기
        def getPos(x,y): # 클릭 좌표
            global mxPose; global myPose
            mxPose = x; myPose = y
            print(str(x),str(y))
            return
        # step1.setposition(stepX,stepY); step1.st()
        # step1.setposition(stepX,stepY); step1.st()
        # step1.setposition(stepX,stepY); step1.st()
        # step1.setposition(stepX,stepY); step1.st()
        
        if StampN == 10: 
            t.clear(); t.ht(); t.setposition(-250,0)
            t.write(" \" 두번째 게임, 성공! \" ", font=("KCC-은영체",50))
            time.sleep(2)
            FirstPlay += 0.5
            if FirstPlay == 1: 
                Ending(); return

        if main2.distance(sShip) > 12: 
            t.ontimer(Running,100)
        elif main2.distance(sShip) == 12: 
            StampN == 10
        elif r1.distance(600,-50)or r2.distance(600,-100)or r3.distance(600,-150) < 50:
            Stop()

        t.onscreenclick(getPos)
    Running()

def Stop(): # 게임오버
    t.clearscreen(); t.ht();  t.penup(); s.bgpic('bg_lose.gif'); s.update(); main.stamp()
    t.setposition(-230,50); t.write("G a m e   O v e r ",font=("KCC-은영체",60))
    time.sleep(1)
    t.setposition(-150,-80); t.write("S c o r e   :   "+str(StampN),font=("KCC-은영체",40))
    time.sleep(5)
    exit()

def Ending():
        t.clearscreen()
        if FirstPlay == 1: 
            s.bgpic('bg4.gif'); s.update(); t.ht(); t.setposition(-300, 250); t.color("white")
            t.write(" \" 축하합니다! 함께 지구로 돌아갑니다! \" ",font=("KCC-은영체",40))
            time.sleep(4)
            exit()

mCharacter = "cat.gif"; Enemy = "alien.gif"; items = ["star.gif","moon.gif","stardust.gif"]
item = random.choice(items); Enem1 = "alien1.gif"; Enem2 = "alien2.gif"; Enem3 = "alien3.gif"; ship = "spaceship.gif"
s.addshape(mCharacter); s.addshape(Enemy); s.addshape(item); s.addshape(Enem1); s.addshape(Enem2); s.addshape(Enem3); s.addshape(ship)
main = t.Turtle(); main.ht(); main.shape(mCharacter); main.up()

#mainF()
SecondGame()
t.listen()
t.mainloop()

