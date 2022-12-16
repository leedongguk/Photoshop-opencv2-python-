from PyQt5 import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import*
from PyQt5 import uic
from camera import CameraWindow
from gallery import GalleryWindow

import sys
  
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.lbl1 = QLabel(self)
        self.lbl2 = QLabel(self)
        self.lbl3 = QLabel(self)
        #갤러리
        self.lbl1.setGeometry(20,770,100,100)
        #카메라
        self.lbl2.setGeometry(130,770,100,100)
        #로딩
        self.lbl3.setGeometry(110,100,290,490)
        
        #로딩 gif파일 호출.
        self.movie = QMovie('image/loding.gif', QByteArray(), self)
        self.movie.setCacheMode(QMovie.CacheAll)
        #self label에 gif삽입
        self.lbl3.setMovie(self.movie)
        self.movie.start()
        
        pixmap1 = QPixmap("image/gallery.png")#gallery
        pixmap2 = QPixmap("image/camera.png")#camera
        pixmap1 = pixmap1.scaledToWidth(100)
        pixmap2 = pixmap2.scaledToWidth(100)
        self.lbl1.setPixmap(QPixmap(pixmap1))
        self.lbl2.setPixmap(QPixmap(pixmap2))

        #라벨에 마우스 이벤트 주는 곳
        self.origin_photo = True
        self.Gallery = True
        #마우스 이벤트
        self.lbl1.mousePressEvent = self.gallery_press
        self.lbl2.mousePressEvent = self.camera_press

        self.gallery = True 

        #배경 이미지 설정
        palette = QPalette()
        palette.setBrush(QPalette.Background,QBrush(QPixmap("image/back3.png")))
        self.setPalette(palette)
        self.setWindowTitle("Dongsta")
        self.setGeometry(100, 50, 500, 885)
        self.show()


   #갤러리 클릭시 마우스이벤트 호출함수.
    def gallery_press(self, event) :
        
        if self.Gallery:
         self.hide()
         self.w = GalleryWindow()
         self.w.show()
            
    
    #카메라 클릭 시 마우스이벤트 호출함수.
    def camera_press(self, event) :
        
        if self.origin_photo:
         self.hide()
         self.w = CameraWindow()
         self.w.show()
    
if __name__ == "__main__" :
    App = QApplication(sys.argv)
    mywindow = MainWindow()
    mywindow.show()
    sys.exit(App.exec())