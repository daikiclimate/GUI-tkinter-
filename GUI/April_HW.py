
# coding: utf-8

# In[7]:

import numpy as np
import tkinter as tk

class bullls_cows:
    global field_label, hidden_num, sub_txt, turn_arrow, result
    def __init__(self):
        self.hidden_hand = None
        self.pred_hand = None
        self.cows = None
        self.bulls = None
        self.turn = 0 #40で初期化する
        self.subnum = None
        self.hidden_seq = 0
        self.result_num = 0
        
    def pred_hands_detect(self):
        if self.turn % 4 == 0:
      #  if self.turn % 4==0:　#４つ入力された時
            self.pred_hand = np.zeros(4)
            for i, j in enumerate(np.arange(self.turn - 4, self.turn)):
                #self.pred_hand[i] =　field_label[j]["text"]
                self.pred_hand[i] = field_label[j]["text"]
            #self.cows = self.count_cows() 　#count_cow
            self.cows = self.count_cows()
            self.bulls = self.count_bulls()  #count_bulls
            
    #count bulls(input hands)
    def count_bulls(self):
        bulls = 0
        for i in range(4):
                if self.hidden_hand[i] == self.pred_hand[i]:
                    bulls += 1
        return bulls
    
    # count cows(input = hands)
    def count_cows(self):
        cows = 0
        for i in range(4):
            for j in range(4):
                if i != j:# not bulls
                    if self.hidden_hand[i] == self.pred_hand[j]:
                        cows+=1
        return cows
    
    def result_change(self):
        if int((self.turn)%4) == 0:
            bulls = self.count_bulls()
            cows = self.count_cows()
            result[self.result_num ]["text"] = "B{0} C{1}".format(self.bulls, self.cows)
            self.result_num += 1      
            
    #button control
    def button_control(self, x):
        #buttonを配列で格納するために必要
        def y():
            
            field_label[self.turn]["text"] = x 
            self.turn += 1              #row = 012301230123, column = 000011112222
            turn_label["text"] = "{}  turn".format(int((self.turn-1)/4)+1)
            turn_arrow.grid(row = int((self.turn)/4), column = 0)
            self.pred_hands_detect()
            self.result_change()            
            
        return y
    
    #define hidden number
    def sub_button_control(self, x):
        def y():
            if self.hidden_seq < 4:#数字は４つまで
                    self.hidden_hand.append(x)
                    hidden_num[self.hidden_seq] = self.hidden_hand[-1]
                    self.hidden_seq += 1
                    sub_txt["text"] = hidden_num
            if self.hidden_seq == 4:
                self.hidden_hand = hidden_num
        return y

#クラスの宣言
bc = bullls_cows()
bc.hidden_hand = []

#入力用サブウィンドウ
sub = tk.Tk()
sub.title("bulls and cows")
sub_num = tk.Frame(sub)
sub_num.grid(row = 2, column = 0)
sub_buttons = []
for i in range(10):
    sub_buttons.append(tk.Button(sub_num, text = " {} ".format(int(i)), command = bc.sub_button_control(i) ))
    sub_buttons[i].grid(row = 2, column = int(i))

hidden_num = ["_","_","_","_"]
sub_txt = tk.Label(sub, text = hidden_num)
sub_txt.grid(row = 1, column = 0)

sub_label = tk.Label(sub, text = "input HIDDEN 4 numbers").grid(row = 0, column = 0)

#メインのウィンドウ
root = tk.Tk()
root.title("bulls and cows")
#root.geometry("320x400")

#ターン表示用ラベル
turn_label = tk.Label(root, text = "1  turn")
turn_label.grid (row = 1, column =1)

#ゲームフィールド用Frame
field_frame = tk.Frame(root)
field_frame.grid(row = 3, column = 1)

# 数字をおくためのスペース. このラベルを入力におきかえる
field = np.full(40," o ")
field_label = []
for i in range(40):
    field_label.append(tk.Label(field_frame, text = field[i]))
    field_label[i].grid(row = int(i/4) , column = int(i%4+3))
    
#盤面の整備
for i in range(10):
    field_num = tk.Label(field_frame, text = "{} : ".format(i))
    field_num.grid(row = i, column = 1)
    field_bar = tk.Label(field_frame, text = "｜")
    field_bar.grid(row = i, column = 2)

#ターンやじるしの表示
turn_arrow = tk.Label(field_frame, text = "⇨")
turn_arrow.grid(row = 0, column = 0)

#result の表示
#column = 7
result_frame = tk.Frame(root)
result_frame.grid(row = 3, column = 2)
result= []
for i in range(10):
    result.append( tk.Label(result_frame, text= "None") )
    result[i].grid(row = i, column = 0)

#盤面
result_label = tk.Label(root, text = "Result").grid(row = 2, column = 2)
Guess_label = tk.Label(root, text = "        Guess").grid(row = 2, column = 1)

#ボタン表示用Frame
number_frame = tk.Frame(root)
number_frame.grid(row = 4, column = 1)
buttons = []
for i in range(10):
    buttons.append(tk.Button(number_frame, text = " {} ".format(int(i)), command = bc.button_control(i)))
    buttons[i].grid(row = 3, column = int(i))
    
root.mainloop()
    


# In[ ]:



