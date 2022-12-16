from PyQt5 import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import*
from PyQt5 import uic
from PyQt5 import QtWidgets
from PyQt5 import QtGui
from selecet import Gallery_select_Window

import sys
  
class GalleryWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        #사진첩
        self.lbl1 = QLabel(self)
        self.lbl1.setGeometry(20,190,170,150)
        pixmap1 = QPixmap("capture/0.png")#gallery
        pixmap1 = pixmap1.scaledToHeight(150)
        self.lbl1.setPixmap(QPixmap(pixmap1))

        #lbl라벨에 마우스 이벤트 추가.
        self.lbl1.mousePressEvent = self.Select
        self.gallery = True 
        
        #라벨(텍스트 추가)
        self.lbl2 = QLabel(self)
        self.lbl2.setGeometry(30,340, 100,50)
        self.lbl2.setText("최근 항목") #텍스트 변환
        self.lbl2.setFont(QtGui.QFont("Arial",11)) #폰트,크기 조절
        self.lbl2.setStyleSheet("Color : gray") #글자색 변환

        #배경이미지
        palette = QPalette()
        palette.setBrush(QPalette.Background,QBrush(QPixmap("image/보관함2.png")))
        self.setPalette(palette)

        self.setWindowTitle("Dongsta")
        self.setGeometry(100, 50, 500, 900)
        self.show()

    #마우스이벤트 호출함수.
    def Select(self, event) :
        
        if self.gallery:
         self.hide()
         self.w = Gallery_select_Window()
         self.w.show()

    
if __name__ == "__main__" :
    App = QApplication(sys.argv)
    mywindow = GalleryWindow()
    mywindow.show()
    sys.exit(App.exec())