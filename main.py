import tkinter as tk
import time
from tkinter import CENTER

window = tk.Tk()

# def Destory_ball1():



window.title("free-falling motion") # 윈도우 창 이름설정
window.geometry("640x400+600+300") # 윈도우 창 크기설정 너비x높이+x좌표+y좌표 (윈도우 창을 실행 했을 때 나타나는 위치로 보임)
window.resizable(True, True) # 윈도우 창 크기 조절 가능 여부


photo = tk.PhotoImage(file="image/ball1.png")
pLabel = tk.Label(window, image=photo)
pLabel.place(x=1, y=1) # (1, 1)에다가 배치


# textbox.after(5000, empty_textbox)


# for i in range(0, 5):
#     time.sleep(2)
#     pLabel.place(x=i * 100, y=i * 100)

window.mainloop() # 윈도우 창을 윈도우가 종료될 때 까지 실행