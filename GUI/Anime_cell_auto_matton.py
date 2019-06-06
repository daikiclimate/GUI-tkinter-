
# coding: utf-8

# In[ ]:

import tkinter as tk
import numpy as np
import random

class cell_auto_matton:
    global canvas, turn_label, field_x, field_y
    
    def __init__(self):
        self.turn = 0#世代
        #fieldの初期化
        self.field_num = np.zeros((field_x,field_y))
        
    def rewrite(self):
        for x in range(field_x):
            for y in range(field_y):
                #(i, j)の四角の削除
                canvas.delete("{},{}".format(x, y))
                
                #色の指定
                if self.field_num[x, y] == 0:
                    color = "white"
                else:
                    color = "black"
                #新しい四角の記述
                canvas.create_rectangle(x*grid_space ,y * grid_space ,(x+1) * grid_space,(y+1)*grid_space,fill = color, tag = "{},{}".format(x, y))
    
    def status_update(self):
        #zero padding
        copy = np.zeros((field_x+2,field_y+2))
        copy[1:-1, 1:-1] = self.field_num
        
        #calucurate sum
        for i in range(1,field_x+1):#paddingしたところは中心にしない
            for j in range(1,field_y+1):
                #target = self.field_num[i, j]
                sum_area = np.sum(copy[i-1, j-1 : j+2]) + np.sum(copy[ i +1, j -1: j+2]) + copy[i, j-1]+ copy[i, j+1]
                if sum_area >= 4:#過密
                    self.field_num[i-1, j-1] = 0
                elif sum_area ==3:#生存or誕生
                    self.field_num[i-1, j-1] = 1
                elif sum_area == 2 and self.field_num[i-1, j-1] == 1: #誕生
                    self.field_num[i-1, j-1] = 1
                else:#過疎
                    self.field_num[i-1, j-1] = 0
                
    #リセットボタン
    def reset(self):
        for i in range(field_x):
            for j in range(field_y):
                cam.field_num[i, j] = random.randint(0 ,1)
                self.turn = 0
                
    #グライダー配置用初期値
    def graide(self):
        self.turn = 0
        self.field_num = np.zeros((field_x,field_y))
        self.field_num[2:4,6:8] = 1
        #self.field_num[12, 6:9] = 1
        self.field_num[12, 6] = 1
        self.field_num[12, 7] = 1
        self.field_num[12, 8] = 1
        self.field_num[13,5] = 1
        self.field_num[13,9] = 1
        self.field_num[14:16,4] = 1
        self.field_num[14:16,10] = 1 
        self.field_num[16, 7] = 1
        self.field_num[17, 5] = 1
        self.field_num[17, 9] = 1
        self.field_num[18, 6:9] =1
        self.field_num[19, 7] = 1
        self.field_num[22:24, 4:7] = 1
        self.field_num[24, 3] = 1
        self.field_num[24, 7] = 1
        self.field_num[26, 2:4] = 1
        self.field_num[26, 7:9] = 1
        self.field_num[36:38, 4:6] = 1
    
    #しゅっしゅぽっぽ列車の初期値
    def shushu(self):
        self.turn = 0
        self.field_num = np.zeros((field_x,field_y))
        self.field_num[3,3] = 1
        self.field_num[3,8] = 1
        self.field_num[3,17] = 1
        self.field_num[4:8,4] = 1
        self.field_num[6,1] = 1
        self.field_num[7,2:5]=1
        self.field_num[4,9] = 1
        self.field_num[5,9:12] =1
        self.field_num[4,12] = 1
        self.field_num[6,15] =1
        self.field_num[7,16:19] = 1
        self.field_num[4:8,18] = 1
        
    def diehard(self):
        self.turn = 0
        self.field_num = np.zeros((field_x,field_y))
        self.field_num[2:4, 3] = 1
        self.field_num[3,4] = 1
        self.field_num[8,2] = 1
        self.field_num[7:10,4] = 1
        
#更新
def step():
        global interval
        cam.status_update()
        cam.rewrite()
        
        turn_label["text"] = cam.turn
        cam.turn += 1
        
        root.after(interval, step )
#宣言
field_x = 50#これ以上マス目を増やすと処理が追いつかなくなる
field_y = 50#
grid_space = 12
interval = 20
cam = cell_auto_matton()

root = tk.Tk()
root.geometry("800x800")
root.title = "cell_auto_matton"

#field 
field = tk.Frame(root)
field.grid(row = 1)

#canvasの宣言
canvas = tk.Canvas(field, width = 500, height = 500)

#初期フィールドの作成
for i in range(field_x):
    for j in range(field_y):
        canvas.create_rectangle(i*grid_space, j*grid_space, grid_space+i*grid_space, grid_space+j*grid_space ,fill = "white" , tag = "{},{}".format(i,j))
        cam.field_num[i, j] = random.randint(0 ,1)
canvas.pack()

#turn
turn_label = tk.Label(root, text = "1")
turn_label.grid(row = 3)

#button_frame
button_frame = tk.Frame(root)
button_frame.grid(row = 4)

#reset button
reset_button = tk.Button(button_frame, text = "reset", command = cam.reset)
reset_button.pack()

#各初期配置のボタン
graide_button = tk.Button(button_frame, text = "グライダー銃", command = cam.graide).pack()
shushu_button = tk.Button(button_frame, text = "シュシュぽっぽ列車", command = cam.shushu).pack()
diehard_button=tk.Button(button_frame, text = "ダイハード", command = cam.diehard).pack()

#最初から特定の配置
#cam.shushu()
#cam.graide()
#cam.diehard()

root.after(interval, step)
root.mainloop()


# In[ ]:



