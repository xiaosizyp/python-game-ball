#######创建游戏画布####
from tkinter import *
import random
import time

class Ball:
    def __init__(self,canvas,paddle,color,x,y):
        self.canvas = canvas
        self.paddle = paddle
        self.id = canvas.create_oval(10,10,25,25,fill=color)
        self.canvas.move(self.id,245,100)
        self.x=x
        self.y=y
        self.hit_bottom=False
        ##参数化水平x参数与垂直y参数

    def draw(self):
        self.canvas.move(self.id,self.x,self.y)
        pos = self.canvas.coords(self.id)
        if pos[0]<=0:
            self.x=3
        if pos[1] <=0:
            self.y=1
        if pos[2] >=self.canvas.winfo_width():
            self.x=-3
        if pos[3]>=self.canvas.winfo_height(): ###canvas.winfo_height()当前窗口的高度
            self.y=-1
        ####判断球是否击到球拍#####
        if self.hit_paddle()==True:
            self.y=-1
        if self.canvas.winfo_height() <= pos[3]:
            self.hit_bottom = True
    def hit_paddle(self):
        ball_pos=self.canvas.coords(self.id)
        paddle_pos=self.canvas.coords(self.paddle.id)
        if ball_pos[2]>=paddle_pos[0] and ball_pos[0]<=paddle_pos[2]:
            if ball_pos[3]>=paddle_pos[1] and ball_pos[3] <= paddle_pos[3]:
                return True
        return  False

class Paddle:
    def __init__(self,canvas,color):
        self.canvas = canvas
        self.id = canvas.create_rectangle(0,0,100,10,fill=color)
        self.canvas.move(self.id,200,300)
        self.x=0
        ###绑定事件到到键盘上
        self.canvas.bind_all('<KeyPress-Left>',self.turn_left)
        self.canvas.bind_all('<KeyPress-Right>',self.turn_right)

    def draw(self):
        self.canvas.move(self.id,self.x,0)
        pos = self.canvas.coords(self.id)
        if pos[0]<=0:
            self.x=0
        if pos[2] >= self.canvas.winfo_width():
            self.x=0

    def turn_left(self , evt):
        self.x=-2
    def turn_right(self , evt):
        self.x=2

tk = Tk()
tk.title("Game")
tk.resizable(0,0)
# tk.vm_attributes("-topmost",1)
canvas = Canvas(tk,width=500,height=400,bd=0,highlightthickness=0)
canvas.pack()
tk.update()

####创建球拍#####
paddle = Paddle(canvas,'blue')

##初始化ball参数，第3个位水平移动参数，第4个位垂直移动参数
xs=[-3,-2,-1,0,1,2,3]
x = random.choice(xs)
print("x水平移动参数：%s" %x)
######将球拍传入球函数中########
ball = Ball(canvas,paddle,'red',x,-1)
while 1:
    if ball.hit_bottom==False:
        paddle.draw()
        ball.draw() ###让小球移动起来
    tk.update_idletasks()
    tk.update()
    time.sleep(0.01)

# tk.mainloop()








