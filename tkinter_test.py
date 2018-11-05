#%matplotlib inline
from PIL import Image, ImageTk
from matplotlib import pyplot as plt
import cv2
import numpy as np
from copy import deepcopy
import tkinter

class FindLocation(object):
    def __init__(self):
        # 创建主窗口,用于容纳其它组件
        self.root = tkinter.Tk()
        # 给主窗口设置标题内容
        self.root.title("图像处理")
        self.root.geometry('450x400')
        #welcom image
        self.canvas = tkinter.Canvas(height=200, width=450)  # 创建画布
        self.image_file = tkinter.PhotoImage(file='welcome.gif')  # 加载图片文件
        self.image = self.canvas.create_image(0, 0, anchor='nw', image=self.image_file)  # 将图片置于画布上
        # 创建一个输入框,并设置尺寸
        self.ip_input = tkinter.Entry(self.root, width=30)
        self.snr_input = tkinter.Entry(self.root, width=30)
        # 创建一个文本框
        self.label1 = tkinter.Label(self.root, text='处理的图片名（格式）：')
        self.label2 = tkinter.Label(self.root, text='输入信噪比：')
        self.label = tkinter.Label(self.root, width=50)
        # 创建一个查询结果的按钮
        self.result_button = tkinter.Button(self.root, command=self.add_salt_noise, text="椒盐处理")
        self.result_button2 = tkinter.Button(self.root, command=self.pinghua_photo, text="平滑处理")
        # self.result_button2.place(x=250,y=350)
        # self.result_button.place(x=100,y=350)


    # 完成布局
    def gui_arrang(self):
        self.canvas.pack(side='top')
        self.label1.pack()
        self.ip_input.pack()
        self.label2.pack()
        self.snr_input.pack()
        self.label.pack()
        self.result_button.pack()
        self.result_button2.pack()






    def add_salt_noise(self):
        # 获取输入信息
        img_name = self.ip_input.get()
        # img = Image.open(img_name)
        img = cv2.imread(img_name)
        # img_png = ImageTk.PhotoImage(img_open)
        snr = self.snr_input.get()
        snr = float(snr)
        print(snr)
        # 指定信噪比
        SNR = snr
        # 获取总共像素个数
        size = img.size
        print(size)
        # 因为信噪比是 SNR ，所以噪声占据百分之10，所以需要对这百分之10加噪声
        noiseSize = int(size * (1 - SNR))
        # 对这些点加噪声
        for k in range(0, noiseSize):
            # 随机获取 某个点
            xi = int(np.random.uniform(0, img.shape[1]))
            xj = int(np.random.uniform(0, img.shape[0]))
            # 增加噪声
            if img.ndim == 2:
                img[xj, xi] = 255
            elif img.ndim == 3:
                img[xj, xi] = 0
        cv2.imwrite("person2.jpg", img)
        img_open2 = Image.open('person2.jpg')
        new_img = ImageTk.PhotoImage(img_open2)
        print(new_img)
        self.label2 = tkinter.Label(self.root, image=new_img).pack()
        self.img = img
        return self.img

    def pinghua_photo(self):
        img_medianblur = cv2.medianBlur(self.img, 11)
        cv2.imwrite("person3.jpg", img_medianblur)



def main():
    # 初始化对象
    FL = FindLocation()
    # 进行布局
    FL.gui_arrang()
    # 主程序执行
    tkinter.mainloop()
    pass


if __name__ == "__main__":
    main()

