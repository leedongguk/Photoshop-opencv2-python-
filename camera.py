import glob
from pickle import BYTEARRAY8
from PyQt5.QtWidgets import * 
from PyQt5 import QtCore
from PyQt5.QtGui import * 
from PyQt5 import QtGui
import sys
import cv2
import numpy as np
from selecet import Gallery_select_Window

class CameraWindow(QMainWindow):
    def __init__(self):  
        super().__init__()
        
        palette = QPalette()
        palette.setBrush(QPalette.Background,QBrush(QPixmap("image/cameraback.png")))
        self.setPalette(palette)
        self.setGeometry(100, 50, 600, 900)

        capture = cv2.VideoCapture(0)

        if capture.isOpened() == False:
            raise Exception("카메라 연결 안됨")
        
        width = capture.get(cv2.CAP_PROP_FRAME_WIDTH)
        height = capture.get(cv2.CAP_PROP_FRAME_HEIGHT)
        print("Oringinal width: %d, height: %d" %(width, height))
        capture.set(cv2.CAP_PROP_FRAME_WIDTH, 600)
        capture.set(cv2.CAP_PROP_FRAME_HEIGHT, 800)
        width = capture.get(cv2.CAP_PROP_FRAME_WIDTH)
        height = capture.get(cv2.CAP_PROP_FRAME_HEIGHT)
        print('Resized width: %d, height: %d' % (width, height))

        self.lbl1 = QLabel(self)#카메라 본체
        self.lbl1.setGeometry(0,100,600,660)

        self.lbl2 = QLabel(self)
        self.lbl2.setGeometry(250,800,100,100)
        pixmap2 = QPixmap("image/click.png")#촬영버튼
        pixmap2 = pixmap2.scaledToWidth(100)
        self.lbl2.setPixmap(QPixmap(pixmap2))

        self.lbl3 = QLabel(self)
        self.lbl3.setGeometry(10,20,70,70)
        self.origin_photo = True
        self.capture = True
        self.lbl3.mousePressEvent = self.fresh_press
        self.lbl2.mousePressEvent = self.capture_video

        #사진
        self.lbl4 = QLabel(self)
        self.lbl4.setGeometry(20,790,80,80)

        self.lbl5 = QLabel(self)
        self.lbl5.setGeometry(80,15,70,70)
        self.lbl5.mousePressEvent = self.bad
        pixmap5 = QPixmap("image/몰카.png")#몰카버튼
        pixmap5 = pixmap5.scaledToWidth(70)
        self.lbl5.setPixmap(QPixmap(pixmap5))

        pixmap3 = QPixmap("image/후레쉬.png")#후레쉬버튼
        pixmap3 = pixmap3.scaledToWidth(70)
        self.lbl3.setPixmap(QPixmap(pixmap3))

        self.lbl7 = QLabel(self)
        self.lbl7.setGeometry(230,10,70,70)
        pixmap7 = QPixmap("image/water.png")#워터마크
        pixmap7 = pixmap7.scaledToWidth(70)
        self.lbl7.setPixmap(QPixmap(pixmap7))
        self.lbl7.mousePressEvent = self.water_press

        self.lbl6 = QLabel(self)
        self.lbl6.setGeometry(160,15,70,70)
        self.lbl6.mousePressEvent = self.digit
        pixmap6 = QPixmap("image/digit.png")#분활
        pixmap6 = pixmap6.scaledToWidth(70)
        self.lbl6.setPixmap(QPixmap(pixmap6))

        self.lbl8 = QLabel(self)
        self.lbl8.setGeometry(300,15,70,70)
        pixmap8 = QPixmap("image/mask.png")#마스크
        pixmap8 = pixmap8.scaledToWidth(70)
        self.lbl8.setPixmap(QPixmap(pixmap8))
        self.lbl8.mousePressEvent = self.mask_press

        #마우스이벤트
        self.edit = True 
        self.lbl4.mousePressEvent = self.edits
        
        #사진첩
        img_files = glob.glob('.\\capture\\*.png')
        idx = 0
       #이미지를 불러오기
        while True:
            img2 = cv2.imread(img_files[idx], cv2.IMREAD_COLOR)
            img = cv2.cvtColor(img2, cv2.COLOR_BGR2RGB)
            
            if img is None:
                print('Image load failed')
                break

            if cv2.waitKeyEx(1000) >= 0:
               break
            
            h, w, c = img.shape
            qImg = QtGui.QImage(img.data, w, h, w * c, QtGui.QImage.Format_RGB888)
            pixmap4 = QtGui.QPixmap.fromImage(qImg)
            pixmap4 = pixmap4.scaledToHeight(80)
            self.lbl4.setPixmap(pixmap4)
            self.show()
            idx += 1
            if idx == 1:
                break

        global fresh
        global end2
        end2 = 0
        fresh = 0
        #카메라
        while True:

            global ret, frame
            global stack3
            global waterstack
            global mask_stack

            ret, frame = capture.read()
            frame = cv2.add(frame, fresh)
            if not ret: break
            if end2 == 1: 
                break
            if cv2.waitKey(30) >= 0: break #종료조건 - 스페이스바

            if(stack3==1): 
                #RED분활
                frame[:,:,0] = 0
                frame[:,:,1] = 0

                #프레임 읽어오기
                ret, frame1 = capture.read()
                ret, frame2 = capture.read()
                ret, frame3 = capture.read()
                
                #RED분활
                frame1[:,:,0] = 0
                frame1[:,:,1] = 0
                frame2[:,:,0] = 0
                frame2[:,:,1] = 0
                frame3[:,:,0] = 0
                frame3[:,:,1] = 0
            
                one = cv2.cvtColor(frame1, cv2.COLOR_BGR2GRAY)
                two = cv2.cvtColor(frame2, cv2.COLOR_BGR2GRAY)
                third = cv2.cvtColor(frame3, cv2.COLOR_BGR2GRAY)
                #절대값 차 구하기.
                diff1 = cv2.absdiff(one, two)
                diff2 = cv2.absdiff(two, third)
                #문턱값
                ret, diff1 = cv2.threshold(diff1, 20, 255, cv2.THRESH_BINARY)
                ret, diff2 = cv2.threshold(diff2, 20, 255, cv2.THRESH_BINARY)
                #각 픽셀에 대해 AND 연산
                diff = cv2.bitwise_and(diff1, diff2)
                cv2.imshow("Camera", diff)

            #선으로 분활 구현
            if(stack4==1):
              cv2.line(frame, (0, 160), (600, 160), (0,0,255))#가로선
              cv2.line(frame, (0, 320), (600, 320), (0,0,255))#가로선
              cv2.line(frame, (210, 0), (210, 500), (0,0,255))#세로선
              cv2.line(frame, (420, 0), (420, 500), (0,0,255))#세로선
            
            #add연산에 가중치를 더해서 워터마크 구현
            if(waterstack==1):
                watermark = cv2.imread('image/watermark.png')
                frame = cv2.addWeighted(frame,0.8,watermark,0.2,0)
            
            if(mask_stack==1):
                #합성에 사용할 영상 읽기, 전경 영상은 4채널 png 파일
                img_fg = cv2.imread('image/teacher.png', cv2.IMREAD_UNCHANGED)
                img_bg = frame
                #알파채널을 이용해서 마스크와 역마스크 생성
                _, mask = cv2.threshold(img_fg[:, :, 3], 1, 255, cv2.THRESH_BINARY)
                mask_inv = cv2.bitwise_not(mask)
                #전경 영상 크기로 배경 영상에서 ROI 잘라내기
                img_fg = cv2.cvtColor(img_fg, cv2.COLOR_BGRA2BGR)
                h, w = img_fg.shape[:2]
                roi = img_bg[10:10+h, 10:10+w]
                #마스크 이용해서 오려내기
                masked_fg = cv2.bitwise_and(img_fg, img_fg, mask=mask)
                masked_bg = cv2.bitwise_and(roi, roi, mask=mask_inv)
                #이미지 합성
                added = masked_fg + masked_bg
                frame[10:10+h, 10:10+w] = added

            img = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)#RGB컬러공건으로 변환 시킴.
            h, w, c = img.shape
            qImg = QtGui.QImage(img.data, w, h, w * c, QtGui.QImage.Format_RGB888)
            pixmap = QtGui.QPixmap.fromImage(qImg)
            self.lbl1.setPixmap(pixmap)
            self.show()
        capture.release()

    #카메라 후레시 효과를 위한 함수
    global stack2
    stack2 = 0
    def fresh_press(self, event) :
        global fresh
        global stack2
        if self.origin_photo:
            if stack2 == 0:
             fresh += 20
             stack2 += 1
             pixmap3 = QPixmap("image/후레쉬1.png")#후레쉬버튼
             pixmap3 = pixmap3.scaledToWidth(70)
             self.lbl3.setPixmap(QPixmap(pixmap3))
             self.lbl3.show()
            
            elif stack2 == 1:
                fresh -= 20
                stack2 -= 1
                pixmap3 = QPixmap("image/후레쉬.png")#후레쉬버튼
                pixmap3 = pixmap3.scaledToWidth(70)
                self.lbl3.setPixmap(QPixmap(pixmap3))
                self.lbl3.show()
    
    #사진 촬영.
    global stack
    stack = 0
    def capture_video(self, event) :
        global stack4
        if self.capture :
            global stack
            #이미지를 순서대로 저장.
            stack4 = 0
            cv2.imwrite('capture/' + str(stack) + '.png', frame)
            stack = stack + 1

    #분활.
    global stack4
    stack4 = 0
    def digit(self, event) :
        global stack4
        if self.capture :
            if(stack4==0):
                stack4 += 1
            elif(stack4==1):
                stack4 -= 1

    #워터마크
    global waterstack
    waterstack = 0
    def water_press(self, event) :
        global waterstack
        if self.capture :
            if(waterstack==0):
                waterstack += 1
            elif(waterstack==1):
                waterstack -= 1

    #마스크
    global mask_stack
    mask_stack = 0
    def mask_press(self, event) :
        global mask_stack
        if self.capture :
            if(mask_stack==0):
                mask_stack += 1
            elif(mask_stack==1):
                mask_stack -= 1

    #몰카 잡아내기.
    global stack3
    stack3 = 0
    def bad(self, event) :
        global stack3
        if self.capture :
            if(stack3 == 0):
                stack3 += 1
            elif(stack3==1):
                stack3 -= 1
                

    global end2
    end2 = 0
    #마우스이벤트 호출함수.
    def edits(self, event) :    
        if self.edit: 
         self.hide()
         self.a = Gallery_select_Window()
         self.a.show()
         end2 += 1     


if __name__ == "__main__" :
  App = QApplication(sys.argv)
  window = CameraWindow()
  window.show()
  sys.exit(App.exec())