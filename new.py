import turtle as t
import random
import time
# 두번째 게임 미완성 > 달에서 1등으로 달려서 우주선에 제일 먼저 도착하면! 지구로 복귀 성공!
t.ht()
s = t.Screen()   #  스크린 생성
s.setup(1500,800)   #  스크린 사이즈 지정
t.bgcolor("white")
mCharacter = "cat.gif" # 캐릭터로 쓸 이미지 가져오기
Enemy = "alien.gif"
items = ["star.gif","moon.gif","stardust.gif"]
item = random.choice(items)
s.addshape(mCharacter) # 이미지 목록에 더해주기
s.addshape(Enemy)
s.addshape(item)
stampN = 0    #   맞은개수 찍을때 필요

def mainF():
    t.penup()  # 선 긋지 말고
    t.ht()  # 거북이 숨기고
    t.setposition(-400, 0)  # 이 좌표에 글씨쓰려고 정해줌.
    t.write(" \" 우주에서 길을 잃은 고양이를 데리고 지구로 돌아오세요! \" ",font=("KCC-은영체",40))
    time.sleep(3)  # 3초 동안 붙잡았다가,
    t.clear()  # 클리어 해줌
    s.bgpic('bg1.gif')  # 스크린 이미지 설정
    s.update()  # 스크린 업데이트
    time.sleep(0.5)
    main.setposition(0,-50)
    main.st()
    t.onkeypress(firstGame, "space")  # space를 누르면, 게임 시작

def firstGame(): # 도망다니면서 별모으기
    s.bgpic('bg2.gif')  # 우주 배경으로 바뀜
    s.update()  # 바뀐 배경 적용
    alien.st()  # 적 보이게
    stars.st()  # 아이템 보이게
    def r(): main.setheading(0)  # 조종
    def u(): main.setheading(90)
    def l(): main.setheading(180)
    def d(): main.setheading(270)
    t.onkeypress(r, "Right")  # 키보드 조종 연결
    t.onkeypress(u, "Up")
    t.onkeypress(l, "Left")
    t.onkeypress(d, "Down")
    t.penup()  # 선 긋지 말고
    t.ht()  # 거북이 숨기고
    t.setposition(-280, 30)  # 이 좌표에 글씨쓰려고 정해줌.
    t.color("white")
    t.write(" \" 외계인을 피해서 별을 모아보자 ! \" ", font=("KCC-은영체",40))
    time.sleep(2)  # 3초 동안 붙잡았다가,
    t.clear()  # 클리어 해줌
    def goOn():
        main.forward(12) # 주인공은 12씩 이동
        alien.forward(5) # 적은 5씩 이동
        global stampN # 맞힌 값 누적시킬때 필요.
        if main.distance(alien) > 12: # 적과 나의 거리가 12보다 크면, (아직 안잡힘)
            t.ontimer(goOn, 200)  # play를, 0,05초마다 호출
            t.ontimer(alienMove, 250)  # 적이 따라오는 함수를, 0.1초마다 호출
        else: stop() # 적에게 잡히면 stop함수 호출.
        if main.distance(stars) < 12: # 아이템 먹을때마다, (가까워질때마다)
            tfx = random.randint(-400,300) # 아이템 자리를
            tfy = random.randint(-400,300) # 랜덤으로 정해서
            stars.goto(tfx, tfy) # 새로 아이템 만들어서 이동.
            stampN += 1 # 먹은 개수 누적 +1
            main.write(str(stampN),False,font=("Impact",50)) # 자리에, 누적 갯수 적어줌.
        #if stampN >= 1: # 아이템 5개 먹으면,
            #SecondGame() # ??
    goOn()

def SecondGame(): # keypress or click으로 더 빠르게 도망가기
    # 마우스로 공을 제대로 클릭해야만 앞으로 forward하는 게임으로 해서, 우주선 탑승하는걸로 가야겠다.
    # enemy가 나보다 먼저 우주선에 도착하면 지는것으로 설정하기 !
    t.clearscreen()
    s.bgpic('bg3.gif') # 이 파일로
    s.update() # 새로운 배경 입혀주고,
    t.penup() # 선 긋지 말고
    t.ht() # 거북이 숨기고
    t.setposition(-250,0) # 이 좌표에 글씨쓰려고 정해줌.
    t.write(" \" 잡히지 않게, 열심히 도망가자 ! \" ", font=("KCC-은영체",40))
    time.sleep(2) # 3초 동안 붙잡았다가,
    t.clear() # 글씨 지워줌.

def stop(): # 적이랑 부딪히면 이거 출력. 게임오버
    t.clearscreen()
    t.penup() # 안보이게
    t.ht() # 안보이게
    s.bgpic('bg_lose.gif') # 배경 바꾸고
    s.update() # 배경 적용
    main.stamp() # 잡힌 위치 보여주고,
    t.setposition(-550,50) # 이 위치에 글씨 써주고
    t.write("  ㅡ  ㅡ  ㅡ    Game Over    ㅡ ㅡ  ㅡ ",font=("Impact",60))
    time.sleep(1)
    t.setposition(-150,-80) #이 위치에 글씨 써주고
    t.write("S c o r e   :   "+str(stampN),font=("Impact",40))
    time.sleep(5)
    exit()

def alienMove():
    angle = alien.towards(main.pos()) #적 > 내 쪽으로 각도를 구해서
    alien.setheading(angle) # 적의 머리 방향을 바꿔 줌.

alien = t.Turtle() #       적
alien.ht()
alien.up()
alien.shape(Enemy)
alien.speed(0)
alien.goto(400, 200) #적의 위치 셋팅

stars = t.Turtle()#       먹이
stars.ht()
stars.speed(0)
stars.up()
stars.shape(item)
stars.goto(-400, 200)

main = t.Turtle()
main.ht()
main.color("white")
main.shape(mCharacter)
main.speed(0)
main.up()

mainF()
t.listen() #   이제 t가 말 들음.
t.mainloop() #   무한 루프