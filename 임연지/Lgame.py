import turtle as t
import random
import time

s = t.Screen()
s.setup(1300,600) # 1500.800
t.bgcolor("white")
StampN = 0
FirstPlay = 0

# 메인 흐름
def mainF():
    t.ht(); t.up(); t.setposition(-400, 0)
    t.write(" \" 우주에서 길을 잃은 고양이를 데리고 지구로 돌아오세요! \" ",font=("KCC-은영체",40))
    time.sleep(3); t.ht(); t.clear() 
    s.bgpic('back_start.gif'); s.update()
    time.sleep(0.5)
    main.setposition(0,-70); main.st() # 고양이등장
    global FirstPlay; FirstPlay = 0
    if FirstPlay == 0: # 키보드로 재실행 안되게 조건 걸어줌.
        t.onkeypress(FirstGame, "space")

def FirstGame():
    
    # 키보드 조종 연결
    def r(): main.setheading(0)
    def u(): main.setheading(90)
    def l(): main.setheading(180)
    def d(): main.setheading(270)
    t.onkeypress(r, "Right")
    t.onkeypress(u, "Up")
    t.onkeypress(l, "Left")
    t.onkeypress(d, "Down")

    # 재실행 방지 도구
    global FirstPlay
    FirstPlay += 0.5
    main.up(); s.bgpic('back_first.gif'); s.update()

    # 설명 텍스트 + 2초 + 사라짐
    t.ht(); t.penup(); t.setposition(-270, 30); t.color("white")
    t.write(" \" 외계인을 피해서 별을 모아보자 ! \" ", font=("KCC-은영체",40))

    # 외계인, 아이템 생성
    alien = t.Turtle(); alien.ht(); alien.up(); alien.goto(400, 200); alien.shape(Enemy); alien.st()
    stars = t.Turtle(); stars.ht(); stars.up(); stars.goto(-400, 200); stars.shape(items); stars.st()

    # 2초 + 사라짐
    time.sleep(2); t.clear(); t.ht()

    # 반복 실행 함수
    def goOn():
        global StampN

        # 통과 기준
        if StampN > 5:
            t.clear(); t.ht(); t.setposition(-250,0); t.write(" \" 첫번째 게임, 성공! \" ", font=("KCC-은영체",50))
            time.sleep(2)

            # 두번째 게임 호출
            if FirstPlay == 0.5:
                exit()
                SecondGame()

        # 함수 호출에 따른 움직임
        main.forward(12)
        alien.forward(5); angle = alien.towards(main.pos()); alien.setheading(angle)

        # 안잡히면 ontimer 반복 / 잡히면 stop
        if main.distance(alien) > 12:
            t.ontimer(goOn,0)
        else:
            Stop()

        # 아이템 먹음 + 새 아이템 생성
        if main.distance(stars) < 14:
            StampN += 1; stars.ht()
            main.color("White"); main.write(str(StampN)+"개!",False,font=("KCC-은영체",50))
            tfx = random.randint(-250,250); tfy = random.randint(-150,150)
            stars.setpos(tfx, tfy); stars.st()
    # 호출
    goOn()

def SecondGame():
    global StampN

    # 배경정리
    t.clearscreen(); s.bgpic('back_second.gif'); s.update()

    # 우주선 + 라인
    sShip = t.Turtle(); sShip.ht(); sShip.up(); sShip.shape(ship); sShip.goto(580,0); sShip.st()
    
    # 텍스트 + 3초 + 사라짐
    t.ht(); t.up(); t.goto(-310,-20)
    t.write(" \" 별을 획득해서, 먼저 우주선에 도착하자 ! \" ", font=("KCC-은영체",40))
    time.sleep(3); t.clear(); t.ht()
    
    # 외계인 + 주인공 + 결승라인 셋팅
    r1 = t.Turtle(); r1.ht(); r1.up(); r1.shape(Enem1); r1.goto(-650,-70); r1.st()
    r2 = t.Turtle(); r2.ht(); r2.up(); r2.shape(Enem2); r2.goto(-620,-140); r2.st()
    r3 = t.Turtle(); r3.ht(); r3.up(); r3.shape(Enem3); r3.goto(-570,-210); r3.st()
    m2 = t.Turtle(); m2.ht(); m2.up(); m2.shape(mCharacter); m2.goto(-600,-280); m2.st()

    # 첫 아이템 생성
    item = t.Turtle(); item.ht(); item.up(); item.shape(items)
    item.setposition(300,200); item.st()

    # 반복 실행 함수
    def Running():
        global StampN

        # x 좌표 셋팅 (결승선 도착 기준)
        r1x = r1.xcor(); r2x = r2.xcor(); r3x = r3.xcor(); myX = m2.xcor()

        # 속도 ( 반복 리셋 )
        rs1=random.randint(1,8); rs2=random.randint(1,8); rs3=random.randint(1,8)
        DefSpeed=2

        # 통과 기준  ( 결승선 + 별 ) 
        if myX and r1x and r2x and r3x < 600:
            t.ontimer(Running,50)

        # 외계인들 먼저 도착하면 Stop
        elif r1x and r2x and r3x > 600:
            Stop()

        # 내가 먼저 도착하면, 스탬프 갯수에 따라 replay or ending
        elif myX > 600:
            t.clearscreen(); t.ht(); t.up(); t.goto(-250,0); t.write(" \" 두번째 게임, 성공! \" ", font=("KCC-은영체",50))
            time.sleep(3)
            if StampN >= 10:
                Ending()
            else:
                t.clearscreen(); t.ht(); t.up(); t.goto(-300,0); t.write(" \" 별이 부족해요.. 한번 더 모아요! \" ", font=("KCC-은영체",50))
                time.sleep(3)
                SecondGame()

        # 마우스 클릭 위치를 보고,
        def getM(x,y):
            global StampN
            Xp=x; Yp=y

            # 아이템의 근사값 설정
            ixp = int(item.xcor())+20
            ixm = int(item.xcor())-20
            iyp = int(item.ycor())+20
            iym = int(item.ycor())-20
            ApproxyX=range(ixm, ixp)
            ApproxyY=range(iym, iyp)
            print("아이템위치:",ixp,iyp,"마우스위치:",Xp,Yp)

            # 잘 클릭했다면.
            if (Xp in ApproxyX) and (Yp in ApproxyY):
                StampN += 1
                m2.forward(100)
                item.write(str(StampN)+"개!",font=("KCC-은영체",40)); item.ht()
                item.goto(random.randint(-300,200), random.randint(-300,2-0)); item.st()

        # 이동
        r1.forward(rs1); r2.forward(rs2); r3.forward(rs3)
        print(myX)
        m2.forward(DefSpeed)
        t.onscreenclick(getM)
    Running()

# 게임오버
def Stop():
    t.clearscreen(); t.ht();  t.penup(); s.bgpic('back_lose.gif'); s.update(); main.stamp()
    t.goto(-230,50); t.write("G a m e   O v e r ",font=("KCC-은영체",60))
    time.sleep(1)
    t.goto(-150,-80); t.write("S c o r e   :   "+str(StampN),font=("KCC-은영체",40))
    time.sleep(5)
    exit()

# 끝
def Ending():
    t.clearscreen()
    s.bgpic('back_come.gif'); s.update()
    t.ht(); t.up(); t.setposition(-300, 100); t.color("white")
    t.write(" \" 축하합니다! 함께 지구로 돌아갑니다! \" ",font=("KCC-은영체",40)); t.ht()
    time.sleep(1)
    bye = t.Turtle(); bye.ht(); bye.up(); bye.shape(byes); bye.setposition(120,-130); bye.st()
    time.sleep(5)
    exit()

# 이미지 주소 저장
mCharacter = "maincat.gif"; Enemy = "alien.gif"; itemss = ["star.gif","moon.gif","stardust.gif"]; byes = "back_come2.gif"
items = random.choice(itemss); Enem1 = "alien1.gif"; Enem2 = "alien2.gif"; Enem3 = "alien3.gif"; ship = "spaceship.gif"
# 이미지 screen에 추가
s.addshape(mCharacter); s.addshape(Enemy); s.addshape(items); s.addshape(Enem1)
s.addshape(Enem2); s.addshape(Enem3); s.addshape(ship); s.addshape(byes)
# 주인공 ( 맨 처음부터 등장해서 여기에 선언 )
main = t.Turtle(); main.ht(); main.shape(mCharacter); main.up()

mainF()
t.listen()
t.mainloop()