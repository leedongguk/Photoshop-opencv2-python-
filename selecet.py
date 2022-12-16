from calendar import different_locale
import os
from PyQt5 import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import*
from PyQt5 import uic
from PyQt5.QtWidgets import QSlider
from PyQt5 import QtGui
import cv2
import sys
import glob
import numpy as np
  
class Gallery_select_Window(QMainWindow):
    def __init__(self):
        super().__init__()
        
        #배경 이미지
        global palette
        palette = QPalette()
        palette.setBrush(QPalette.Background,QBrush(QPixmap("image/사진선택.png")))
        self.setPalette(palette)

        self.setWindowTitle("Dongsta")
        self.setGeometry(100, 50, 500, 900)
        
        #사진
        self.lbl1 = QLabel(self)
        self.lbl1.setGeometry(0,50,500,900)
        
        #편집버튼
        self.lbl2 = QLabel(self)
        self.lbl2.setGeometry(430,55,50,30)
        pixmap2 = QPixmap("image/편집.png")
        self.lbl2.setPixmap(QPixmap(pixmap2))
        pixmap2 = pixmap2.scaledToWidth(30)
        self.edit = True 
        self.lbl2.mousePressEvent = self.edit_press

        #색 편집용
        self.lbl3 = QLabel(self)
        self.lbl3.mousePressEvent = self.color_press

        #상세한 편집용
        self.lbl4 = QLabel(self)
        self.lbl4.mousePressEvent = self.detail_press

        #크기조절 편집용
        self.lbl5 = QLabel(self)
        self.lbl5.mousePressEvent = self.size_press

        #복귀버튼
        self.lbl6 = QLabel(self)
        self.lbl6.mousePressEvent = self.back

        #저장벝느
        self.lbl7 = QLabel(self)
        self.lbl7.mousePressEvent = self.clear
        
        #그림
        self.lbl8 = QLabel(self)
        self.lbl8.mousePressEvent = self.edit_press

        #사진원본
        self.lbl9 = QLabel(self)
        self.lbl9.mousePressEvent = self.original_img

        #색1
        self.lbl10 = QLabel(self)
        #self.lbl10.mousePressEvent = self.edit_press

        #색2
        self.lbl11 = QLabel(self)
        #self.lbl11.mousePressEvent = self.edit_press

        #색3
        self.lbl12 = QLabel(self)
        #self.lbl12.mousePressEvent = self.edit_press

        #색4
        self.lbl13 = QLabel(self)
        #self.lbl13.mousePressEvent = self.edit_press

        #디테일한 편집1
        self.lbl14 = QLabel(self)
        #self.lbl14.mousePressEvent = self.edit_press

        #디테일한 편집2
        self.lbl15 = QLabel(self)
        #self.lbl14.mousePressEvent = self.edit_press

        #디테일한 편집3
        self.lbl16 = QLabel(self)
        #self.lbl14.mousePressEvent = self.edit_press

        #디테일한 편집4
        self.lbl17 = QLabel(self)
        #self.lbl14.mousePressEvent = self.edit_press

        #디테일한 편집5
        self.lbl18 = QLabel(self)
        #self.lbl14.mousePressEvent = self.edit_press

        #사이즈조절 트랙바
        self.lbl19 = QLabel(self)
        
        #원본사진
        self.original_lbl = QLabel(self)

        self.timer = QTimer(self)# timer 변수에 QTimer 할당

        global img_files
        #capture폴더에 png 파일 모두 저장
        img_files = glob.glob('.\\capture\\*.png')
        cnt = len(img_files)
        global idx
        idx = 0

        #끝내기 위한 변수
        global end
        end = 0
        global save
        save = idx
        global img
        global img2
        while True:
            
            img2 = cv2.imread(img_files[idx], cv2.IMREAD_COLOR)
            img = cv2.cvtColor(img2, cv2.COLOR_BGR2RGB)
            if img is None:
                print('Image load failed')
                break

            if cv2.waitKeyEx(1000) >= 0:
               break
            
            #edit를 클릭시 종료
            if end == 1:
                break
            
            h, w, c = img.shape
            qImg = QtGui.QImage(img.data, w, h, w * c, QtGui.QImage.Format_RGB888)
            pixmap1 = QtGui.QPixmap.fromImage(qImg)
            pixmap1 = pixmap1.scaledToWidth(500)
            self.lbl1.setPixmap(pixmap1)
            self.show()

            if idx >= cnt :
                idx = 0
    
    #오른쪽 버튼을 누르면 다음 이미지를 불러 옴
    def keyPressEvent(self, e):
        global idx
        global end
        global save
        if e.key() == Qt.Key_Right:
            idx += 1
            save = idx
    
    #edit 버튼을 누르면 끝내고 편집으로 넘어가기 위한 함수.
    def edit_press(self, event) :
        global end
        if self.edit:
            end += 1
            palette.setBrush(QPalette.Background,QBrush(QPixmap("image/edit_page.png")))
            self.setPalette(palette)
            self.setGeometry(100, 50, 500, 900)
            self.show()
            self.lbl2.hide()
            
            #색편집
            self.lbl3.setGeometry(160,830,50,50)
            pixmap3 = QPixmap("image/edit/7.png")
            self.lbl3.setPixmap(QPixmap(pixmap3))
            self.lbl3.show()
            
            #상세한 편집
            self.lbl4.setGeometry(230,830,50,50)
            pixmap4 = QPixmap("image/edit/9.png")
            self.lbl4.setPixmap(QPixmap(pixmap4)) 
            self.lbl4.show()
            
            #크기 조절용
            self.lbl5.setGeometry(310,830,50,50)
            pixmap5 = QPixmap("image/edit/8.png")
            self.lbl5.setPixmap(QPixmap(pixmap5))
            self.lbl5.show()

            #복귀버튼
            self.lbl6.setGeometry(420,830,70,50)
            pixmap6 = QPixmap("image/edit/21.png")
            self.lbl6.setPixmap(QPixmap(pixmap6))
            self.lbl6.show()
            
            #완료버튼
            self.lbl7.setGeometry(20,830,70,50)
            pixmap7 = QPixmap("image/edit/11.png")
            self.lbl7.setPixmap(QPixmap(pixmap7))
            self.lbl7.show()
            self.lbl7.mousePressEvent = self.saveimg

            #그림버튼
            self.lbl8.setGeometry(460,50,40,40)
            pixmap8 = QPixmap("image/edit/23.png")
            self.lbl8.setPixmap(QPixmap(pixmap8))
            self.lbl8.show()
            self.lbl8.mousePressEvent = self.drawing_img

            #원본사진 버트
            self.lbl9.setGeometry(400,50,58,40)
            pixmap9 = QPixmap("image/edit/24.png")
            self.lbl9.setPixmap(QPixmap(pixmap9))
            self.lbl9.show()
    
    #색변경 버튼.
    global color_change
    color_change = 0
    def color_press(self, event) :
        global save
        global img_files
        global color_change
        global img2
        global img
        if self.edit:
            
          if color_change == 0:
            #색변경 1차
            img = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
            h, w = img.shape[:2]
            qImg2 = QtGui.QImage(img.data, w, h, img.strides[0], QtGui.QImage.Format_Grayscale8)
            pixmap10 = QtGui.QPixmap.fromImage(qImg2)
            pixmap10 = pixmap10.scaledToWidth(100)
            self.lbl10.setPixmap(pixmap10)
            self.lbl10.setGeometry(10,700,100,100)
            self.lbl10.show()
            self.lbl10.mousePressEvent = self.s1
            #색변경 2차
            img = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
            img=cv2.GaussianBlur(img,(5,5),0)
            canny_edges=cv2.Canny(img,10,70)
            _, img=cv2.threshold(canny_edges,70,255,cv2.THRESH_BINARY_INV)
            h, w = img.shape[:2]
            qImg3 = QtGui.QImage(img.data, w, h, img.strides[0], QtGui.QImage.Format_Grayscale8)
            pixmap11 = QtGui.QPixmap.fromImage(qImg3)
            pixmap11 = pixmap11.scaledToWidth(100)
            self.lbl11.setPixmap(pixmap11)
            self.lbl11.setGeometry(130,700,100,100)
            self.lbl11.show()
            self.lbl11.mousePressEvent = self.s2

            #색 변경 3차
            img7 = cv2.imread(img_files[save], cv2.IMREAD_COLOR)
            img8 = cv2.cvtColor(img7, cv2.COLOR_BGR2RGB)
            white = np.array([255,255,255], np.uint8)
            img8 = white - img8
            h, w, c = img8.shape
            qImg4 = QtGui.QImage(img8.data, w, h, w * c, QtGui.QImage.Format_RGB888)
            pixmap12 = QtGui.QPixmap.fromImage(qImg4)
            pixmap12 = pixmap12.scaledToWidth(100)
            self.lbl12.setPixmap(pixmap12)
            self.lbl12.setGeometry(250,700,100,100)
            self.lbl12.show()
            self.lbl12.mousePressEvent = self.s3

            #색 변경 4차
            img9 = cv2.imread(img_files[save], cv2.IMREAD_COLOR)
            img10 = cv2.cvtColor(img9, cv2.COLOR_BGR2YCrCb)
            #img10_1 = img10[:, :, 0].astype(np.float32)
            #img10_2 = cv2.GaussianBlur(img10_1, (0, 0), 2.0)
            #img10[:, :, 0] = np.clip(2. * img10_1 - img10_2, 0, 255).astype(np.uint8)
            h, w, c = img10.shape
            qImg5 = QtGui.QImage(img10.data, w, h, w * c, QtGui.QImage.Format_RGB888)
            pixmap13 = QtGui.QPixmap.fromImage(qImg5)
            pixmap13 = pixmap13.scaledToWidth(100)
            self.lbl13.setPixmap(pixmap13)
            self.lbl13.setGeometry(370,700,100,100)
            self.lbl13.show()
            self.lbl13.mousePressEvent = self.s4
            color_change += 1

          elif color_change == 1:
            self.lbl10.hide()
            self.lbl11.hide()
            self.lbl12.hide()
            self.lbl13.hide()
            color_change -= 1
    
    #상세 버튼을 누르면 끝내고 상세편집으로 넘어가기 위한 함수.
    global detail_open
    detail_open = 0
    def detail_press(self, event) :
        global detail_open
        if self.edit:
          if detail_open == 0:
            #대비
            self.lbl14.setGeometry(20,730,80,80)
            pixmap14 = QPixmap("image/edit/1.png")
            self.lbl14.setPixmap(QPixmap(pixmap14))
            self.lbl14.show()
            self.lbl14.mousePressEvent = self.d1
            

            #디테일2
            self.lbl15.setGeometry(120,730,80,80)
            pixmap15 = QPixmap("image/edit/2.png")
            self.lbl15.setPixmap(QPixmap(pixmap15))
            self.lbl15.show()
            self.lbl15.mousePressEvent = self.d2

            #디테일3
            self.lbl16.setGeometry(220,730,80,80)
            pixmap16 = QPixmap("image/edit/3.png")
            self.lbl16.setPixmap(QPixmap(pixmap16))
            self.lbl16.show()
            self.lbl16.mousePressEvent = self.d3
            #디테일4
            self.lbl17.setGeometry(320,730,80,80)
            pixmap17 = QPixmap("image/edit/4.png")
            self.lbl17.setPixmap(QPixmap(pixmap17))
            self.lbl17.show()
            self.lbl17.mousePressEvent = self.d4
            
            #디테일5
            self.lbl18.setGeometry(410,730,80,80)
            pixmap18 = QPixmap("image/edit/5.png")
            self.lbl18.setPixmap(QPixmap(pixmap18))
            self.lbl18.show()
            self.lbl18.mousePressEvent = self.d5

            detail_open += 1

          elif detail_open == 1:
            self.lbl14.hide()
            self.lbl15.hide()
            self.lbl16.hide()
            self.lbl17.hide()
            self.lbl18.hide()
            detail_open -=1

    global size_open
    size_open = 0
    global img2
    def size_press(self, event) :
        global size_open
        if self.edit:
            if size_open == 0:
              cv2.namedWindow('mosaic')
              while True:
                k = cv2.waitKey(1) & 0xFF
                x, y, w, h = cv2.selectROI('mosaic', img2, False)
                if w and h:
                    roi = img2[y:y+h, x:x+w]
                    # 축소
                    roi = cv2.resize(roi, (w//15, h//15))
                    # INTER_AREA 방식으로 확대
                    roi = cv2.resize(roi, (w, h), interpolation=cv2.INTER_AREA)
                    img2[y:y+h, x:x+w] = roi
                    cv2.imshow('mosaic', img2)
                    img = cv2.cvtColor(img2, cv2.COLOR_BGR2RGB)
                    h, w, c = img.shape
                    qImg = QtGui.QImage(img.data, w, h, w * c, QtGui.QImage.Format_RGB888)
                    pixmap1 = QtGui.QPixmap.fromImage(qImg)
                    pixmap1 = pixmap1.scaledToWidth(500)
                    self.lbl1.setPixmap(pixmap1)
                    self.show()
                elif k == 27:
                  cv2.destroyAllWindows()
                  break
                  
            
            elif size_open == 1:
              size_open -= 1
    
    global img
    global img2
    global stack 
    stack = 0
    def saveimg(self, event) :
        global stack
        if self.edit:
            cv2.imwrite('save/'+str(stack)+'.png', img2)
            stack+=1
    
    #첫번째 필터
    global stack2
    stack2 = 0
    def s1(self, event) :
        global stack2
        global img2
        global img
        if self.edit:
          if(stack2==0):
            img = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
            h, w = img.shape[:2]
            qImg2 = QtGui.QImage(img.data, w, h, img.strides[0], QtGui.QImage.Format_Grayscale8)
            pixmap10 = QtGui.QPixmap.fromImage(qImg2)
            pixmap10 = pixmap10.scaledToWidth(500)
            self.lbl1.setPixmap(pixmap10)
            self.lbl1.show()
            stack2 += 1
          elif(stack2==1):
            img2 = cv2.imread(img_files[idx], cv2.IMREAD_COLOR)
            img = cv2.cvtColor(img2, cv2.COLOR_BGR2RGB)
            h, w, c = img.shape
            qImg = QtGui.QImage(img.data, w, h, w * c, QtGui.QImage.Format_RGB888)
            pixmap1 = QtGui.QPixmap.fromImage(qImg)
            pixmap1 = pixmap1.scaledToWidth(500)
            self.lbl1.setPixmap(pixmap1)
            self.show()
            stack2 -= 1
    
    #두번째 필터
    global stack3
    stack3 = 0
    def s2(self, event) :
        global stack3
        global img2
        global img
        if self.edit:
          if(stack3==0):

            #색 변경 2차
            img = cv2.imread(img_files[save], cv2.IMREAD_COLOR)
            img = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
            img=cv2.GaussianBlur(img,(5,5),0)
            canny_edges=cv2.Canny(img,10,70)
            _, img=cv2.threshold(canny_edges,70,255,cv2.THRESH_BINARY_INV)
            h, w = img.shape[:2]
            qImg3 = QtGui.QImage(img.data, w, h, img.strides[0], QtGui.QImage.Format_Grayscale8)
            pixmap11 = QtGui.QPixmap.fromImage(qImg3)
            pixmap11 = pixmap11.scaledToWidth(500)
            self.lbl1.setPixmap(pixmap11)
            self.lbl1.show()
            stack3 += 1


          elif(stack3==1):
            img2 = cv2.imread(img_files[idx], cv2.IMREAD_COLOR)
            img = cv2.cvtColor(img2, cv2.COLOR_BGR2RGB)
            h, w, c = img.shape
            qImg = QtGui.QImage(img.data, w, h, w * c, QtGui.QImage.Format_RGB888)
            pixmap1 = QtGui.QPixmap.fromImage(qImg)
            pixmap1 = pixmap1.scaledToWidth(500)
            self.lbl1.setPixmap(pixmap1)
            self.show()
            stack3 -= 1

    #세번째 필터
    global stack4
    stack4 = 0
    def s3(self, event) :
        global stack4
        if self.edit:
          if(stack4==0):

            #색 변경 3차
            img7 = cv2.imread(img_files[save], cv2.IMREAD_COLOR)
            img8 = cv2.cvtColor(img7, cv2.COLOR_BGR2RGB)
            white = np.array([255,255,255], np.uint8)
            img8 = white - img8
            h, w, c = img8.shape
            qImg4 = QtGui.QImage(img8.data, w, h, w * c, QtGui.QImage.Format_RGB888)
            pixmap12 = QtGui.QPixmap.fromImage(qImg4)
            pixmap12 = pixmap12.scaledToWidth(500)
            self.lbl1.setPixmap(pixmap12)
            self.lbl1.show()
            stack4 += 1

          elif(stack4==1):
            img2 = cv2.imread(img_files[idx], cv2.IMREAD_COLOR)
            img = cv2.cvtColor(img2, cv2.COLOR_BGR2RGB)
            h, w, c = img.shape
            qImg = QtGui.QImage(img.data, w, h, w * c, QtGui.QImage.Format_RGB888)
            pixmap1 = QtGui.QPixmap.fromImage(qImg)
            pixmap1 = pixmap1.scaledToWidth(500)
            self.lbl1.setPixmap(pixmap1)
            self.show()
            stack4 -= 1

    #네번째 필터
    global stack5
    stack5 = 0
    def s4(self, event) :
        global stack5
        if self.edit:
          if(stack5==0):

            #색 변경 4차
            img9 = cv2.imread(img_files[save], cv2.IMREAD_COLOR)
            img10 = cv2.cvtColor(img9, cv2.COLOR_BGR2YCrCb)
            #img10_1 = img10[:, :, 0].astype(np.float32)
            #img10_2 = cv2.GaussianBlur(img10_1, (0, 0), 2.0)
            #img10[:, :, 0] = np.clip(2. * img10_1 - img10_2, 0, 255).astype(np.uint8)
            h, w, c = img10.shape
            qImg5 = QtGui.QImage(img10.data, w, h, w * c, QtGui.QImage.Format_RGB888)
            pixmap13 = QtGui.QPixmap.fromImage(qImg5)
            pixmap13 = pixmap13.scaledToWidth(500)
            self.lbl1.setPixmap(pixmap13)
            self.lbl1.show()
            stack5 += 1

          elif(stack5==1):
            img2 = cv2.imread(img_files[idx], cv2.IMREAD_COLOR)
            img = cv2.cvtColor(img2, cv2.COLOR_BGR2RGB)
            h, w, c = img.shape
            qImg = QtGui.QImage(img.data, w, h, w * c, QtGui.QImage.Format_RGB888)
            pixmap1 = QtGui.QPixmap.fromImage(qImg)
            pixmap1 = pixmap1.scaledToWidth(500)
            self.lbl1.setPixmap(pixmap1)
            self.show()
            stack5 -= 1



    

    global d_s1
    d_s1 = 0
    def d1(self, value):
        global d_s1
        global img2
        global idx
        global img
        if self.edit:
            if(d_s1==0):
                img2 = cv2.imread(img_files[idx], cv2.IMREAD_GRAYSCALE)
                noimage = np.zeros(img2.shape[:2], img2.dtype)
                img = cv2.scaleAdd(img2, 0.5, noimage)
                img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
                h, w, c = img.shape
                qImg = QtGui.QImage(img.data, w, h, w * c, QtGui.QImage.Format_RGB888)
                pixmap1 = QtGui.QPixmap.fromImage(qImg)
                pixmap1 = pixmap1.scaledToWidth(500)
                self.lbl1.setPixmap(pixmap1)
                self.show()
                d_s1 += 1
            
            elif(d_s1==1):
                img2 = cv2.imread(img_files[idx], cv2.IMREAD_GRAYSCALE)
                noimage = np.zeros(img2.shape[:2], img2.dtype)
                img = cv2.scaleAdd(img2, 1.0, noimage)
                img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
                h, w, c = img.shape
                qImg = QtGui.QImage(img.data, w, h, w * c, QtGui.QImage.Format_RGB888)
                pixmap1 = QtGui.QPixmap.fromImage(qImg)
                pixmap1 = pixmap1.scaledToWidth(500)
                self.lbl1.setPixmap(pixmap1)
                self.show()
                d_s1 += 1
            
            elif(d_s1==2):
                img2 = cv2.imread(img_files[idx], cv2.IMREAD_GRAYSCALE)
                noimage = np.zeros(img2.shape[:2], img2.dtype)
                img = cv2.scaleAdd(img2, 1.5, noimage)
                img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
                h, w, c = img.shape
                qImg = QtGui.QImage(img.data, w, h, w * c, QtGui.QImage.Format_RGB888)
                pixmap1 = QtGui.QPixmap.fromImage(qImg)
                pixmap1 = pixmap1.scaledToWidth(500)
                self.lbl1.setPixmap(pixmap1)
                self.show()
                d_s1 += 1
            
            elif(d_s1==3):
                img2 = cv2.imread(img_files[idx], cv2.IMREAD_GRAYSCALE)
                noimage = np.zeros(img2.shape[:2], img2.dtype)
                img = cv2.scaleAdd(img2, 2.0, noimage)
                img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
                h, w, c = img.shape
                qImg = QtGui.QImage(img.data, w, h, w * c, QtGui.QImage.Format_RGB888)
                pixmap1 = QtGui.QPixmap.fromImage(qImg)
                pixmap1 = pixmap1.scaledToWidth(500)
                self.lbl1.setPixmap(pixmap1)
                self.show()
                d_s1 += 1
            elif(d_s1==4):
                img2 = cv2.imread(img_files[idx], cv2.IMREAD_COLOR)
                img = cv2.cvtColor(img2, cv2.COLOR_BGR2RGB)
                h, w, c = img.shape
                qImg = QtGui.QImage(img.data, w, h, w * c, QtGui.QImage.Format_RGB888)
                pixmap1 = QtGui.QPixmap.fromImage(qImg)
                pixmap1 = pixmap1.scaledToWidth(500)
                self.lbl1.setPixmap(pixmap1)
                self.show()
                d_s1 = 0

    global d_s2
    d_s2 = 0
    def d2(self, value):
        global d_s2
        global img2
        global img
        if self.edit:
            def mouse(event, x, y, flags, param):
              if event == cv2.EVENT_LBUTTONDOWN:
                print('EVENT_LBUTTONDOWN: %d, %d' % (x, y))
                roi = img[y:y+10, x:x+10]   # 관심영역 지정
                roi = cv2.blur(roi, (5, 5)) # 블러 처리
                img2[y:y+10, x:x+10] = roi   # 원본 이미지에 적용
              
            
            if(d_s2==0):
              cv2.namedWindow('blur')
              cv2.setMouseCallback('blur', mouse)

              while True:
                cv2.imshow('blur', img2)
                k = cv2.waitKey(1) & 0xFF

                if k == 27:
                  img = cv2.cvtColor(img2, cv2.COLOR_BGR2RGB)
                  h, w, c = img.shape
                  qImg = QtGui.QImage(img.data, w, h, w * c, QtGui.QImage.Format_RGB888)
                  pixmap1 = QtGui.QPixmap.fromImage(qImg)
                  pixmap1 = pixmap1.scaledToWidth(500)
                  self.lbl1.setPixmap(pixmap1)
                  self.show()
                  d_s2 +=1
                  break

            
            
            elif(d_s2==1):
              d_s2 -= 1
    #랜덤선
    global ds_3
    ds_3 = 0
    def d3(self, event) :
        global ds_3
        global img2
        global idx
        global fresh
        fresh = 0

        if self.edit:
          def next():
            global fresh
            global img2

            a1 = np.random.randint(1,639)
            a2 = np.random.randint(1,477)
            a3 = np.random.randint(1,639)
            a4 = np.random.randint(1,477)

            a5 = np.random.randint(0,255)
            a6 = np.random.randint(0,255)
            a7 = np.random.randint(0,255)

            a8 = np.random.randint(2,10)

            cv2.line(img2, (a1,a2), (a3,a4), (a5,a6,a7), a8) 


            print(fresh)
            img = cv2.cvtColor(img2, cv2.COLOR_BGR2RGB)
            h, w, c = img.shape
            qImg = QtGui.QImage(img.data, w, h, w * c, QtGui.QImage.Format_RGB888)
            pixmap1 = QtGui.QPixmap.fromImage(qImg)
            pixmap1 = pixmap1.scaledToWidth(500)
            self.lbl1.setPixmap(pixmap1)
            self.show()
            img = cv2.subtract(img, fresh)

          if(ds_3==0):
            self.timer.start(50)
            self.timer.timeout.connect(next)
            ds_3 += 1
          elif(ds_3==1):
            self.timer.stop()
            ds_3 -= 1
    #뽀샤시
    ds_4 = 0
    def d4(self, value):
        global ds_4
        global img2
        global img
        if self.edit:
          if(ds_4==0):
            img = cv2.cvtColor(img2, cv2.COLOR_BGR2RGB)
            img = cv2.GaussianBlur(img, (5,5),0)
            h, w, c = img.shape
            qImg = QtGui.QImage(img.data, w, h, w * c, QtGui.QImage.Format_RGB888)
            pixmap1 = QtGui.QPixmap.fromImage(qImg)
            pixmap1 = pixmap1.scaledToWidth(500)
            self.lbl1.setPixmap(pixmap1)
            self.show()
              
    #랜덤색
    global ds_5
    ds_5 = 0
    def d5(self, event) :
        global ds_5
        global img2
        global idx
        if self.edit:
          if(ds_5==0):

            img2 = cv2.imread(img_files[save], cv2.IMREAD_GRAYSCALE)
            img2 = cv2.Canny(img2,50,200)
            img2 = cv2.cvtColor(img2, cv2.COLOR_BGR2RGB)

            #이미지 읽기
            img3 = img2
            #결과 이미지 생성
            img2 = np.zeros_like(img3)
            #그레이 스케일과 바이너리 스케일 변환
            gray = cv2.cvtColor(img3, cv2.COLOR_BGR2GRAY)
            _, th = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)

            #연결된 요소 레이블링 적용
            cnt, labels = cv2.connectedComponents(th)

            #레이블 갯수 만큼 순회
            for i in range(cnt):
            #레이블이 같은 영역에 랜덤한 색상 적용
              img2[labels==i] =  [int(j) for j in np.random.randint(0,255, 3)]

            img = cv2.cvtColor(img2, cv2.COLOR_BGR2RGB)
            h, w, c = img.shape
            qImg = QtGui.QImage(img.data, w, h, w * c, QtGui.QImage.Format_RGB888)
            pixmap1 = QtGui.QPixmap.fromImage(qImg)
            pixmap1 = pixmap1.scaledToWidth(500)
            self.lbl1.setPixmap(pixmap1)
            self.show()
            ds_5 += 1
          elif(ds_5==1):
            img2 = cv2.imread(img_files[idx], cv2.IMREAD_COLOR)
            img = cv2.cvtColor(img2, cv2.COLOR_BGR2RGB)
            h, w, c = img.shape
            qImg = QtGui.QImage(img.data, w, h, w * c, QtGui.QImage.Format_RGB888)
            pixmap1 = QtGui.QPixmap.fromImage(qImg)
            pixmap1 = pixmap1.scaledToWidth(500)
            self.lbl1.setPixmap(pixmap1)
            self.show()
            ds_5 -= 1


              
    

    #그림그리기
    global drawing
    drawing = False
    global ix, iy
    ix = -1
    iy = -1
    global pen
    pen = (0,0,0)
    global drawing_stack
    drawing_stack = 0
    def drawing_img(self, value):
        global drawing_stack
        global img2
        if self.edit:
          def draw_circle(event, x, y, flags, param):
            global img2
            global ix
            global iy
            global drawing

            if event == cv2.EVENT_LBUTTONDOWN:
              drawing = True
              ix, iy = x, y

            if event == cv2.EVENT_MOUSEMOVE:
              if drawing == True:
                cv2.circle(img2, (x, y), 5, pen, -1 )

            elif event == cv2.EVENT_LBUTTONUP:
              drawing = False
            
          if(drawing_stack==0):
              cv2.namedWindow('drawingimg')
              cv2.setMouseCallback('drawingimg', draw_circle)
              self.showColorDlg()

              while True:
                cv2.imshow('drawingimg', img2)
                k = cv2.waitKey(1) & 0xFF

                if k == 27:
                  img = cv2.cvtColor(img2, cv2.COLOR_BGR2RGB)
                  h, w, c = img.shape
                  qImg = QtGui.QImage(img.data, w, h, w * c, QtGui.QImage.Format_RGB888)
                  pixmap1 = QtGui.QPixmap.fromImage(qImg)
                  pixmap1 = pixmap1.scaledToWidth(500)
                  self.lbl1.setPixmap(pixmap1)
                  self.show()
                  drawing_stack +=1
                  break

          elif(drawing_stack==1):
              cv2.destroyAllWindows()
              drawing_stack -= 1

    def showColorDlg(self):
      global pen    
      #색상 대화상자 생성      
      color = QColorDialog.getColor()
      print(color.getRgb())
      #색상이 유효한 값이면 참, QFrame에 색 적용
      if color.isValid():           
          pen = color.getRgb()

    global original
    original =0
    def original_img(self, value):
      global original
      if self.edit:
        if(original==0):
            original_img2 = cv2.imread(img_files[idx], cv2.IMREAD_COLOR)
            original_img = cv2.cvtColor(original_img2, cv2.COLOR_BGR2RGB) 
            h, w, c = img.shape
            original_qImg = QtGui.QImage(original_img.data, w, h, w * c, QtGui.QImage.Format_RGB888)
            original_pixmap1 = QtGui.QPixmap.fromImage(original_qImg)
            original_pixmap1 = original_pixmap1.scaledToWidth(500)
            self.original_lbl.setPixmap(original_pixmap1)
            self.original_lbl.setGeometry(550,300,500,400)
            self.setGeometry(100, 50, 1080, 900)
            self.show()
            original += 1

        elif(original==1):
            self.setGeometry(100, 50, 500, 900)
            self.original_lbl.hide()
            self.show()
            original -= 1

    def back(self, value):
      global img
      if self.edit:
        img2 = cv2.imread(img_files[idx], cv2.IMREAD_COLOR)
        img = cv2.cvtColor(img2, cv2.COLOR_BGR2RGB)
        h, w, c = img.shape
        qImg = QtGui.QImage(img.data, w, h, w * c, QtGui.QImage.Format_RGB888)
        pixmap1 = QtGui.QPixmap.fromImage(qImg)
        pixmap1 = pixmap1.scaledToWidth(500)
        self.lbl1.setPixmap(pixmap1)
        self.show()

    global save_stack
    save_stack = 0
    def clear(self, value):
      global img
      if self.edit:
        cv2.imwrite('save/' + str(save_stack) + '.png', img)
      
        
   
if __name__ == "__main__" :
    App = QApplication(sys.argv)
    mywindow = Gallery_select_Window()
    mywindow.show()
    sys.exit(App.exec())