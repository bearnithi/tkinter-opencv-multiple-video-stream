import tkinter
import cv2 as cv2
import PIL.Image, PIL.ImageTk
import videocapture
import login
import settings

class App:
    def __init__(self, window, window_title, video_source = 0):
        self.window = window
        self.window.title(window_title)
        self.window.geometry('{}x{}'.format(window.winfo_screenwidth(), window.winfo_screenheight()))
        self.window.rowconfigure(0, weight=1)
        self.window.columnconfigure(0, weight=1)
        self.window.rowconfigure(1, weight=1)
        self.window.columnconfigure(1, weight=1)

        self.ctr_left = tkinter.Frame(window, bg='blue', width=200, height=200, padx=3, pady=3)
        self.ctr_mid = tkinter.Frame(window, bg='yellow', width=200, height=200, padx=3, pady=3)
        self.ctr_right = tkinter.Frame(window, bg='green', width=200, height=200, padx=3, pady=3)
        self.ctr_end = tkinter.Frame(window, bg ='black', padx=3, pady=3)

        self.video_source = video_source
        self.vidLeft = videocapture.MyVideoCapture(video_source)
        # self.vidRight = MyVideoCapture('rtsp://192.168.10.72:8080/video/h264')
        # self.vidBack = MyVideoCapture('rtsp://digitalbroadcast.streamguys.net/live-studio.sdp')
        
        self.canvasLeft = tkinter.Canvas(self.ctr_left, width = self.vidLeft.width, height = self.vidLeft.height)
        self.canvasRight = tkinter.Canvas(self.ctr_mid, width = self.vidLeft.width, height = self.vidLeft.height)
        self.canvasBack = tkinter.Canvas(self.ctr_right, width = self.vidLeft.width, height = self.vidLeft.height)
        login.Login().loginUI(self.ctr_end)
        settings.Settings(self.ctr_end)
        self.canvasLeft.pack()
        self.canvasRight.pack()
        self.canvasBack.pack()

        self.ctr_left.grid(row=0, column=0, sticky="nsnew")
        self.ctr_mid.grid(row=0, column=1, sticky="nsnew")
        self.ctr_right.grid(row=1, column=0, sticky="nsnew")
        self.ctr_end.grid(row = 1, column = 1, sticky="nsnew")

        self.delay = 15
        self.update()
        self.window.mainloop()


    def update(self):
        retLeft, frameLeft = self.vidLeft.get_frame()
        if retLeft:
            self.photoLeft = PIL.ImageTk.PhotoImage(image = PIL.Image.fromarray(frameLeft))
            self.canvasLeft.create_image(0, 0, image = self.photoLeft, anchor = tkinter.NW)
            self.canvasLeft.create_text(20, 20, anchor=tkinter.W, font="Purisa", fill="white", text="Camera Left")
        
        retRight, frameRight = self.vidLeft.get_frame()
        if retRight:
            self.photoRight = PIL.ImageTk.PhotoImage(image = PIL.Image.fromarray(frameRight))
            self.canvasRight.create_image(0, 0, image = self.photoRight, anchor = tkinter.NW)
            self.canvasRight.create_text(20, 20, anchor=tkinter.W, font="Purisa", fill="white", text="Camera Right")
        
        retBack, frameBack = self.vidLeft.get_frame()
        if retBack:
            self.photoBack = PIL.ImageTk.PhotoImage(image = PIL.Image.fromarray(frameBack))
            self.canvasBack.create_image(0, 0, image = self.photoBack, anchor = tkinter.NW)
            self.canvasBack.create_text(20, 20, anchor=tkinter.W, font="Purisa", fill="white", text="Camera Back")

        self.window.after(self.delay, self.update)

App(tkinter.Tk(), "Viact")


