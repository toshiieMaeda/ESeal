from tkinter import *
from PIL import Image, ImageDraw, ImageFont
#import numpy as np
#import cv2
import math
from datetime import datetime 

#電子判子作成
#Copyright ©2021 TM. All rights reserved.
class ESealMainClass:
    #コンストラクタ
    def __init__(self) -> None:
        self.sizeW = 80
        self.sizeH = 80

        #self.font= u'ＭＳ 明朝'
        self.font= u'msgothic.ttc'
        self.charSize = 14
        self.name = u'前田利家ですがなにか'        
        self.day = datetime(2021,6,14)
        self.otherWord = 'test'
        self.lineWidth = 2 
 
    # #opencv
    # def drawCircle2(self):
    #     space = 0
    #     cBottom = self.sizeH + space
    #     cRight = self.sizeW + space
    #     cCenter = int(self.sizeH / 2 + space)

    #     img = np.full((), 128, dtype=np.uint8)

    #     #背景色を透明に設定
    #     img = np.where(np.all(img == 255, axis=-1), 0, 255)
        
    #     ###円描画
    #     cv2.circle(img, (cCenter,cCenter), int(self.sizeW / 2), (255,0,0), thickness=1, lineType=cv2.LINE_AA)
    
    #     ###線分描画
    #     line1H = int(self.sizeH / 3)     #1/3のラインのTop
    #     line2H = int(self.sizeH / 3 * 2) #2/3のラインのTop

    #     # ラインの長さ
    #     lineLength = int(self.calcLine(cCenter - line1H))

    #     # ラインのleft
    #     lineLeft = int((self.sizeH - lineLength) / 2 + space)
        
    #     cv2.line(img, (lineLeft,line1H), (lineLeft + lineLength,line1H), (255,0,0), thickness=4, lineType=cv2.LINE_AA)
    #     cv2.line(img, (lineLeft,line2H), (lineLeft + lineLength,line2H), (255,0,0), thickness=4, lineType=cv2.LINE_AA)
        
    #     # #cv2→PIL変換
    #     # imgpil = self.cv2Topil(img)
    #     # c = ImageDraw.Draw(imgpil)

    #     # ###文字描画
    #     # font = ImageFont.truetype(self.font, self.charSize)
    #     # charW,charH = c.textsize(self.name, font=font)
    #     # c.text(((self.sizeW / 4) + space, (self.sizeH / 3 * 2) + space), self.name, font=font, fill='red')

    #     cv2.imwrite('C:\\pg\\output\\test.png',img)
    #     # imgpil.save('C:\\pg\\output\\test.png')

    #pillow
    def drawCircle(self):
        space = 0
        cBottom = self.sizeH + space
        cRight = self.sizeW + space
        cCenter = (self.sizeH / 2) + space

        img = Image.new("RGBA",(self.sizeW + 2, self.sizeH + 2), 'WHITE' )
        #背景色を透明に設定
        img.putalpha(0)
        c = ImageDraw.Draw(img)

        ###円描画
        #font=(self.font, self.charSize)
        c.ellipse([(space,space), (self.sizeW - space, self.sizeH - space)], outline = 'red', width = self.lineWidth)
    
        ###線分描画
        line1H = self.sizeH / 3     #1/3のラインのTop
        line2H = self.sizeH / 3 * 2 #2/3のラインのTop

        # ラインの長さ
        lineLength = self.calcLine(cCenter - line1H)

        # ラインのleft
        lineLeft = (self.sizeH - lineLength) / 2 + space
        
        c.line([(lineLeft,line1H),(lineLeft + lineLength,line1H)], fill='red', width = self.lineWidth)
        c.line([(lineLeft,line2H),(lineLeft + lineLength,line2H)], fill='red', width = self.lineWidth)

        ###文字描画
        font = ImageFont.truetype(self.font, self.charSize)

        #日付
        day ='{0:%Y/%m/%d}'.format(self.day)
        charW,charH = c.textsize(day, font=font)

        charLeft, charTop = self.getTextPosition(cCenter, cCenter, charW, charH)
        c.text((charLeft, charTop), day, font=font, fill='red')

        #上段
        font = ImageFont.truetype(self.font, self.charSize)

        #下段
        charSize = self.charSize
        font = ImageFont.truetype(self.font, charSize)
        while (charSize > 1):
            charW,charH = c.textsize(self.name, font=font)
            if charW < line2H and charH < line1H :
                break;
            charSize -= 1
            font = ImageFont.truetype(self.font, charSize)

        charLeft, charTop = self.getTextPosition(cCenter, line2H + (line1H / 2) , charW, charH)
        c.text((charLeft, charTop), self.name, font=font, fill='red')

        #保存
        img.save('C:\\pg\\output\\test.png')

    def calcLine(self,centerDis):
        hypotenuse = self.sizeH / 2
        return math.sqrt(hypotenuse**2 - centerDis**2) * 2

    def getTextPosition(self, centerW, centerH, charW, charH):
        charLeft = centerW - (charW / 2)
        charTop = centerH - (charH / 2)

        return charLeft,charTop
            
    # def pilTocv2(self,imgPIL):
    #     imgCV_RGB = np.array(imgPIL, dtype = np.uint8)
    #     imgCV_BGR = np.array(imgPIL)[:, :, ::-1]
    #     return imgCV_BGR

    # def cv2Topil(self,imgCV):
    #     #imgCV_RGB = imgCV
    #     #imgPIL = Image.fromarray(imgCV_RGB)
    #     imgPIL = imgCV.copy()
    #     imgPIL = Image.fromarray(imgPIL)
    #     return imgPIL

if __name__=='__main__':

        eSeal = ESealMainClass()

        eSeal.drawCircle()







