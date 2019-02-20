import cv2 as cv
import numpy as np

class piecture_theord():
    #全局阈值


    def threshold_demo(self,image,filena):
        gray = cv.cvtColor(image, cv.COLOR_RGB2GRAY)  #把输入图像灰度化
        #直接阈值化是对输入的单通道矩阵逐像素进行阈值分割。
        img_mean=cv.blur(gray,(5,5)) #均值滤波
        cv.imwrite(filena+'binary0.tif',img_mean)
        img_Guassian=cv.GaussianBlur(gray,(5,5),0) #高斯滤波
        cv.imshow("img_Guassian", img_Guassian)
        img_median=cv.medianBlur(img_mean,5)#中值滤波
        cv.imshow("img_median", img_median)
        img_bilater=cv.bilateralFilter(gray,9,75,75)#双边滤波
        cv.imshow("img_bilater", img_bilater)
        ret, binary = cv.threshold(img_median, 0, 255, cv.THRESH_BINARY | cv.THRESH_TRIANGLE)
        print("threshold value %s"%ret)
        kernels=np.ones((10,10),np.uint8)
        closing=cv.morphologyEx(binary, cv.MORPH_CLOSE, kernels)
        opening=cv.morphologyEx(closing,cv.MORPH_OPEN,kernels)
        cv.namedWindow("binary0", cv.WINDOW_NORMAL)
        cv.imshow("binary0", opening)
        cv.imwrite(filena+'binary0.tif',opening)

    #局部阈值
    def local_threshold(self,image,filena):
        gray = cv.cvtColor(image, cv.COLOR_RGB2GRAY)  #把输入图像灰度化
        #自适应阈值化能够根据图像不同区域亮度分布，改变阈值
        binary =  cv.adaptiveThreshold(gray, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C,cv.THRESH_BINARY, 25, 10)
        cv.namedWindow("binary1", cv.WINDOW_NORMAL)
        cv.imshow("binary1", binary)
        cv.imwrite(filena+'binary1.tif',binary)

    #用户自己计算阈值
    def custom_threshold(self,image,filena):
        gray = cv.cvtColor(image, cv.COLOR_RGB2GRAY)  #把输入图像灰度化
        h, w =gray.shape[:2]
        m = np.reshape(gray, [1,w*h])
        mean = m.sum()/(w*h)
        print("mean:",mean)
        ret, binary =  cv.threshold(gray, mean, 255, cv.THRESH_BINARY)
        cv.namedWindow("binary2", cv.WINDOW_NORMAL)
        cv.imshow("binary2", binary)
        cv.imwrite(filena+'binary2.tif',binary)


def pic_the():
    filename='image/22.png'
    filena=str(filename.split('.')[0])
    print(filena)

    src = cv.imread(filename)
    cv.namedWindow('input_image', cv.WINDOW_NORMAL) #设置为WINDOW_NORMAL可以任意缩放
    cv.imshow('input_image', src)
    self.threshold_demo(src,filena)
    #local_threshold(src,filena)
    #custom_threshold(src,filena)
    cv.waitKey(1000)
    cv.destroyAllWindows()
#     filename='22.png'
#     filena=str(filename.split('.')[0])
#     print(filena)

#     src = cv.imread(filename)
#     cv.namedWindow('input_image', cv.WINDOW_NORMAL) #设置为WINDOW_NORMAL可以任意缩放
#     cv.imshow('input_image', src)
#     threshold_demo(src,filena)
#     #local_threshold(src,filena)
#     #custom_threshold(src,filena)
#     cv.waitKey(1000)
#     cv.destroyAllWindows()
