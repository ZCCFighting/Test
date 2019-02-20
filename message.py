import sys 
from PyQt5.QtWidgets import QWidget,QMessageBox,QApplication,QDesktopWidget

class Example(QWidget):
	def __init__(self):
		super().__init__()
		self.initUI()

	def initUI(self):
		self.setGeometry(300,200,1500,800)
		self.setWindowTitle('MessageBox')
		self.show()


	def closeEvent(self,event):

		reply=QMessageBox.question(self,'Message',"Are you sure to quit",QMessageBox.Yes | QMessageBox.No,QMessageBox.Yes) #第三个按钮表示的默认的按钮
		if reply==QMessageBox.Yes:
			event.accept()
		else:
			event.ignore()



if __name__ == '__main__':
	app=QApplication(sys.argv) #所有的pyqt应用必须创建一个应用（Application）对象。sys.argv参数是一个来自命令行的参数列表。Python脚本可以在shell中运行。这是我们用来控制我们应用启动的一种方法。
	ex=Example()
	sys.exit(app.exec_())