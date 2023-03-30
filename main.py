import tkinter

window=tkinter.Tk()

window.title("free-falling motion") # 윈도우 창 이름설정
window.geometry("640x400+600+300") # 윈도우 창 크기설정 너비x높이+x좌표+y좌표 (윈도우 창을 실행 했을 때 나타나는 위치로 보임)
window.resizable(True, True) # 윈도우 창 크기 조절 가능 여부


# cavas_com = can

# ball = tkinter.PhotoImage(file="image/ball.png")

ball = file="image/ball.png"

# window.create_image

# label3 = tkinter.Label(window, text="11", width=45, height=25, bg="blue", relief="flat")
# label3.pack()

C_ball = tkinter.Label(window, image=ball, width=25, height=40)
C_ball.pack()

window.mainloop() # 윈도우 창을 윈도우가 종료될 때 까지 실행



# im_rock = tkinter.PhotoImage(file="Scissors_c.png")
# cavas_com.create_image(150, 150, image=im_rock, tag="im_scissors")