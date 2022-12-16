from PyQt5 import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import*
from PyQt5 import uic
from insta import MainWindow
import sys
  
class Window(QMainWindow):
    def __init__(self):
        super().__init__()
 
        #self에 lbl라벨 추가
        self.lbl = QLabel(self)
        #라벨 사이즈 조정
        self.lbl.resize(800,600)
        #gif파일 호출.
        self.movie = QMovie('image/ad.gif', QByteArray(), self)
        self.movie.setCacheMode(QMovie.CacheAll)
        #self label에 gif삽입
        self.lbl.setMovie(self.movie)
        self.movie.start()
        #윈도우 제목
        self.setWindowTitle("Dongsta")
        #윈도우창 크기 조절
        self.resize(800,600)
        #타이머
        self.timer = QTimer(self)                # timer 변수에 QTimer 할당
        self.timer.start(6500)                  # 6500msec(6.5sec) 마다 반복
        #6.5초 후 next 함수 실행.
        self.timer.timeout.connect(self.next)
        self.show()
    
    #타이머 완료 후 
    def next(self) :
        self.hide()
        self.timer.stop()
        #insta의 MainWindow 실행
        self.w = MainWindow()
        self.w.show()
   
if __name__ == "__main__" :
    App = QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec())