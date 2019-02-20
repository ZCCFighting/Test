import sys 
from PyQt5.QtWidgets import QApplication,QWidget,QPushButton,QToolTip,QMessageBox,QFileDialog
from PyQt5.QtGui import QIcon,QFont,QPixmap
from PyQt5.QtCore import QCoreApplication
from PyQt5 import QtCore,QtGui,QtWidgets
import cv2
import os
from theord import *
import gdal 
#pyqt5 时间处理系统由信号和槽机制建立 注意QCoreAppli类由QApplication创建
class Example(QWidget):
	def __init__(self):
		super().__init__() #super方法返回的Example的父类对象调用父类的构造方法
		self.timer_camera = QtCore.QTimer()
		self.cap = cv2.VideoCapture()
		self.CAM_NUM = 0
		self.initUI()
		self.solt_init()
		self.__flag_work = 0
		self.x =0
		self.picflag=0 #判断label_img中是否存在图片
		self.show()


	def initUI(self):
		# QToolTip.setFont(QFont('SansSerif',10))
		# self.setToolTip('this is a <b>QPushButton</b> widget')
		self.qbtn=QPushButton('打开相机',self)
		# self.qbtn.setStyleSheet('QPushButton{border-image:url(MMC.png)}')  #button按钮背景颜色
		self.qbtn.setIcon(QIcon('MMC.png'))
		#点击信号连接到quit()方法，将结束应用。事件通信在两个对象之间进行：发送者和接受者。发送者是按钮，接受者是应用对象。
		self.qbtn.resize(100,60)
		self.qbtn.move(0,0)#在widget中显示的位置

		self.obtn=QPushButton('打开图像',self)
		self.obtn.resize(100,60)
		self.obtn.move(100,0)


		self.pbtn=QPushButton('处理图像',self)
		self.pbtn.resize(100,60)
		self.pbtn.move(200,0)

		self.cbtn=QPushButton('关闭',self)
		#self.cbtn.clicked.connect(QCoreApplication.instance().quit)#点击信号连接到quit()方法，将结束应用。事件通信在两个对象之间进行：发送者和接受者。发送者是按钮，接受者是应用对象。
		self.cbtn.resize(100,60)
		self.cbtn.move(300,0)#在widget中显示的位置


		self.label_show_camera=QtWidgets.QLabel(self)
		self.label_show_camera.setGeometry(50,80,800,600)

		self.lable_show_img=QtWidgets.QLabel(self)
		self.lable_show_img.setGeometry(850,80,500,400)
		# self.label_show_camera.resize(800,600)
		# self.label_show_camera.move(50,100)
		# self.label_show_camera.setFixedSize(641, 481)
		# self.label_show_camera.setAutoFillBackground(False)


		self.setGeometry(300,200,1500,800)#将窗口在屏幕上显示，设置尺寸resize 和move融合
		self.setWindowTitle('Icon')
		self.setWindowIcon(QIcon('MMC.png'))

	def solt_init(self):
		self.qbtn.clicked.connect(self.button_open_camera_click)
		self.cbtn.clicked.connect(self.close)
		self.timer_camera.timeout.connect(self.show_camera)
		#self.pbtn.clicked.connect(self.picture_theord)
		self.obtn.clicked.connect(self.loadFile)

	#def picture_theord(self):

		

	def button_open_camera_click(self):
		if self.timer_camera.isActive() == False:
			flag = self.cap.open(self.CAM_NUM)
			if flag == False:
				msg = QtWidgets.QMessageBox.warning(self, u"Warning", u"请检测相机与电脑是否连接正确", buttons=QtWidgets.QMessageBox.Ok,
                                                defaultButton=QtWidgets.QMessageBox.Ok)
            # if msg==QtGui.QMessageBox.Cancel:
            #                     pass
			else:
				self.timer_camera.start(30)
				self.qbtn.setText(u'关闭相机')
		else:
			self.timer_camera.stop()
			self.cap.release()
			self.label_show_camera.clear()
			self.qbtn.setText(u'打开相机')
	
	def show_camera(self):
		flag, self.image = self.cap.read()
		# face = self.face_detect.align(self.image)
		# if face:
		#     pass
		show = cv2.resize(self.image, (800, 600))
		show = cv2.cvtColor(show, cv2.COLOR_BGR2RGB)
		showImage = QtGui.QImage(show.data, show.shape[1], show.shape[0], QtGui.QImage.Format_RGB888)
		self.label_show_camera.setPixmap(QtGui.QPixmap.fromImage(showImage))
	def loadFile(self):
		if self.picflag==0:
			print("load--file")
			fname, _ = QFileDialog.getOpenFileName(self, '选择图片', 'c:\\', 'Image files(*.jpg *.gif *.png *.tif *.tiff)')
			self.frame=fname
			self.lable_show_img.setPixmap(QPixmap(self.frame))
			self.lable_show_img.setScaledContents(True) #图片自适应label大小
			self.obtn.setText(u'清除图片')
			self.picflag=1
		else:
			self.lable_show_img.setPixmap(QPixmap(""))
			self.obtn.setText(u'打开图像')
			self.picflag=0
	
	def closeEvent(self,event):
		ok = QPushButton()
		cacel = QPushButton()
		msg = QMessageBox(QMessageBox.Warning, "关闭", "是否关闭！")
		msg.addButton(ok,QMessageBox.ActionRole)
		msg.addButton(cacel,QMessageBox.RejectRole)
		ok.setText('确定')
		cacel.setText('取消')
		# msg.setDetailedText('sdfsdff')
		if msg.exec_() == QMessageBox.RejectRole:
			event.ignore()
		else:
            #             self.socket_client.send_command(self.socket_client.current_user_command)
			if self.cap.isOpened():
				self.cap.release()
			if self.timer_camera.isActive():
				self.timer_camera.stop()
			event.accept()

if __name__ == '__main__':
	app=QApplication(sys.argv) #所有的pyqt应用必须创建一个应用（Application）对象。sys.argv参数是一个来自命令行的参数列表。Python脚本可以在shell中运行。这是我们用来控制我们应用启动的一种方法。
	ex=Example()
	sys.exit(app.exec_())
	# w=QWidget() #Qwidget是所有用户界类的基础类，我们给QWidget提供了默认的构造方法。默认构造方法没有父类。没有父类的widget组件将被作为窗口使用。
	# w.resize(500,500)#调整窗口的大小
	# w.move(1000,300)#移动widget到一个位置
	# w.setWindowTitle('Test')#设置窗口的标题
	# w.show()#第一次在内存中创建，之后显示在屏幕上面
	# sys.exit(app.exec_())#exec是python保留关键字，使用exec_代替

