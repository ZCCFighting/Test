import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import os
class filedialogdemo(QWidget):

    def __init__(self, parent=None):
        super().__init__()
        self.setGeometry(300,200,1500,800)
        layout = QVBoxLayout()

        self.btn = QPushButton()
        self.btn.clicked.connect(self.loadFile)
        self.btn.setText("从文件中获取照片")
        layout.addWidget(self.btn)

        self.label = QLabel()
        layout.addWidget(self.label)

        self.btn_2 = QPushButton()
        self.btn_2.clicked.connect(self.load_text)
        self.btn_2.setText("加载电脑文本文件")
        layout.addWidget(self.btn_2)

        self.content = QTextEdit()
        layout.addWidget(self.content)
        self.setWindowTitle("测试")

        self.setLayout(layout)
        self.show()

    def loadFile(self):
        print("load--file")
        fname, _ = QFileDialog.getOpenFileName(self, '选择图片', 'c:\\', 'Image files(*.jpg *.gif *.png *.tif *.tiff)')
        self.label.setPixmap(QPixmap(fname))

    def load_text(self):
        print("load--text")
        dlg = QFileDialog()
        dlg.setFileMode(QFileDialog.AnyFile)
        dlg.setFilter(QDir.Files)
        if dlg.exec_():
            filenames = dlg.selectedFiles()
            f = open(filenames[0], 'r')
            with f:
                data = f.read()
                self.content.setText(data)
    def closeEvent(self,event):

        reply=QMessageBox.question(self,'Message',"Are you sure to quit",QMessageBox.Yes | QMessageBox.No,QMessageBox.No) #第三个按钮表示的默认的按钮
        if reply==QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    fileload =  filedialogdemo()
    # fileload.show()
    sys.exit(app.exec_())