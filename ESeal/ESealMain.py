from tkinter import *
from PIL import Image, ImageDraw, ImageFont

#電子判子作成

class ESealMainClass:
    #コンストラクタ
    def __init__(self) -> None:
        self.sizeX = 100
        self.sizeY = 100

        self.font= u'ＭＳ 明朝'
        self.charSize = 12
        self.name = u'前田'
        self.day = '20210611'
        self.otherWord = 'test'
    
    def drawCircle(self):
        space = 19
        img = Image.new("RGBA",(self.sizeX, self.sizeY), 'WHITE' )
        c = ImageDraw.Draw(img)
        #font=(self.font, self.charSize)
        font = ImageFont.truetype(self.font, 200)
        c.ellipse([(space,space), (self.sizeX - space, self.sizeY - space)], outline = 'red', width = 4)

        charW,charH = c.textsize(self.name, font=font)
        c.text(((self.sizeX - charW)/2,((self.sizeY - charH)/2) - (charH - charW)), self.name, font=font, fill='red')


        img.save('C:\\pg\\output\\test.png')


if __name__=='__main__':

        eSeal = ESealMainClass()

        eSeal.drawCircle()







