import tkinter as tk
import time


# class Stop:
#     def __init__(self):
#         # ttt(3)
#         time.sleep(3)
#         window.after(1000, ttt(3))

if __name__ == "__main__":

    from tkinter import CENTER


    window = tk.Tk()

    window.title("free-falling motion") # 윈도우 창 이름설정
    window.geometry("1400x900+300+100") # 윈도우 창 크기설정 너비x높이+x좌표+y좌표 (윈도우 창을 실행 했을 때 나타나는 위치로 보임)
    window.resizable(True, True) # 윈도우 창 크기 조절 가능 여부


    photo = tk.PhotoImage(file="image/ball1.png")
    pLabel = tk.Label(window, image=photo)
    pLabel.place(x=1, y=1) # (1, 1)에다가 배치

    def Destory_ball1(i):
        pLabel.destroy() # pLabel 삭제
        # window.delete("pLabel")
        # window.after(500, add_ball1)

        add_ball1(i)
    def add_ball1(i):
        # photo = tk.PhotoImage(file="image/ball1.png")
        pLabel = tk.Label(window, image=photo)
        pLabel.place(x=i * 100, y=i * 100)
        # window.after(500, pLabel.place(x=1 * 100, y=1 * 100))


    # i = 0
    # while i < 5:
    #     window.after(1000, Destory_ball1)
    #     i += 1

    def ttt(i):
        i -= 1
        if not i:
            return 0
        print(i)
        ttt(i)
    ttt(3)

    # for i in range(1, 2):
    #     ttt(5)
    #     window.after(1000, Destory_ball1(i))

    # ttt(5)
    # window.after(1000, ttt(5))
    # window.after(1000, time.sleep(1))
    # Destory_ball1(1)

    # def click():
    #     i = 4
    #
    #     b = tk.Button(text="click me", command=Destory_ball1(i))
    #     b.pack()
    # click()


    # window.after()을 함수안에 포함시켜 after 함수로 인해 멈추는 현상을 메인 프로그램 루프와 분리시켜 실험

    # def test():
    #     # ttt(5)
    #     # window.after(10000, time.sleep())
    #     # time.sleep(10)
    #     t = Stop()
    #     Destory_ball1(1)
    # test()


    # for i in range(0, 5):
    #     window.after(1000, Destory_ball1)
    #     pLabel.place(x=i * 100, y=i * 100)


    # window.after(1000, Destory_ball1)

    # def tksleep(self, time: float) -> None:
    #     """
    #     Emulating `time.sleep(seconds)`
    #     Created by TheLizzard, inspired by Thingamabobs
    #     """
    #     self.after(int(time * 1000), self.quit)
    #     self.mainloop()
    # tk.Mick.tksleep = tksleep
    #
    #
    # tksleep(2)


    window.mainloop() # 윈도우 창을 윈도우가 종료될 때 까지 실행




#
# import tkinter
# import time
#
# class MyApp:
#     def __init__(self, parent): # window
#         self.root = parent
#         self.root.geometry("400x400")
#         self.frame = tkinter.Frame(parent)
#         self.frame.pack()
#         b = tkinter.Button(text="click me", command=self.delayed)
#         b.pack()
#
#     def delayed(self):
#         time.sleep(3)
#
# if __name__ == "__main__":
#     root = tkinter.Tk()
#     app = MyApp(root)
#     root.mainloop()