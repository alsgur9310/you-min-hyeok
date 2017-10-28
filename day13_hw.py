# you-min-hyeok
import turtle as t
t.shape("turtle")
t.speed(0)
t.up()
t.goto(-300,-300)
t.down()
for x in range(4):             #정사각형 만들기
    t.fd(500)
    t.left(90)

t.up()
t.goto(-50,-50)
t.down()
import random                  
n = random.randint(-180,180)   #각도의 범위를 지정
t.seth(n)

def ozil():
    n=t.heading()             
    X = t.xcor()
    Y = t.ycor()
    if 180< n < 360:
        n = n-360
        
    
    while -300<t.ycor()<200 and -300<t.xcor()<200:              # 정사각형의 x,y 범위 지정
        t.fd(2)

    if   -1 <  t.xcor() -200 < 1: #-45<n<45: 각도지정   
        t.seth(180-n)
        t.fd(30)

    elif  (-1 <  t.ycor() +300 < +1 or -1 <  t.ycor() -200 < +1) and t.xcor() > X: # 45<n<90 or -90<n<-45: 각도지정
        t.seth(360-n)
        t.fd(10)

    elif  (-1 <  t.ycor() +300 < +1 or -1 <  t.ycor() -200 < +1) and t.xcor() < X: #90<n<135 or -135<n<-90: 각도지정
        t.seth(360-n)
        t.fd(10)

    elif  -1 <  t.xcor() +300 < +1: #135<n<180 or -180<n<-135: 각도지정
        t.seth(180-n)
        t.fd(10)

    

    ozil()
    

ozil()
