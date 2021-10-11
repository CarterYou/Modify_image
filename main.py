import sys
from PyQt5 import uic
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PIL import Image

Image.MAX_IMAGE_PIXELS = 933120000
form_class = uic.loadUiType("modify_pic.ui")[0]

#사진의 경로를 찾아서 배열에 저장 yes
#저장된 파일경로를 윈도우에 표시  yes
#변경할 값들 읽어오기
#파일경로들을 가져와서 사진 수정
#저장경로 가져오기 yes
#저장경로
#화면을 띄우는데 사용되는 Class 선언
class WindowClass(QMainWindow, form_class) :
    def __init__(self) :
        super().__init__()
        self.setWindowTitle("Modify Pic")
        self.setupUi(self)

        self.pic_data = []
        self.save_loc = ''

        self.plus_bt.clicked.connect(self.add_pic)
        self.save_bt.clicked.connect(self.save_pic)
        self.minus_bt.clicked.connect(self.delete_pic)
        self.percentage_sp.valueChanged.connect(self.get_value_sp)
        self.direction_cb.currentIndexChanged.connect(self.get_value_cb)
        self.convert_bt.clicked.connect(self.convert)
        self.pic_list.itemClicked.connect(self.image_show)

    def add_pic(self):
        add_pic_list = QFileDialog.getOpenFileNames(self, "Open files", "/", "Images (*.png *.xpm *.jpg)")
        self.pic_data = self.pic_data + add_pic_list[0]
        self.view_add()

    def get_pic_name(self, data):
        last = data.rfind('/')
        return data[last:]

    def view_add(self):
        self.pic_list.clear()
        for i in self.pic_data:
            self.pic_list.addItem(self.get_pic_name(i))

    def image_show(self):
        self.selectedRow = self.pic_list.currentRow()
        self.qPixmapVar = QPixmap()
        self.qPixmapVar.load(self.pic_data[self.selectedRow])
        self.qPixmapVar = self.qPixmapVar.scaledToWidth(421)
        self.image_show_l.setPixmap(self.qPixmapVar)

    def get_value_sp(self):
        self.percentage = self.percentage_sp.value()

    def get_value_cb(self):
        self.direction = self.direction_cb.currentText()


    def delete_pic(self):
        self.removeItemRow = self.pic_list.currentRow()
        self.pic_list.takeItem(self.removeItemRow)
        del self.pic_data[self.removeItemRow]
        print(self.pic_data)


    def convert(self):
        self.get_value_sp()
        self.get_value_cb()
        if self.direction == "좌 우":
            for i in self.pic_data:
                try:
                    img = Image.open(i)
                    img_resize = img.resize((int(img.width * (1 - self.percentage/100)), int(img.height)))
                    img_resize.save(self.save_loc + self.get_pic_name(i))
                    self.progress_show_l.setText(self.get_pic_name(i) + " converted")
                except OSError as e:
                    self.error_show_l.setText(e)
                    pass

        elif self.direction == "상 하":
            for i in self.pic_data:
                try:
                    img = Image.open(i)
                    img_resize = img.resize((int(img.width), int(img.height * (1 - self.percentage/100))))
                    img_resize.save(self.save_loc + self.get_pic_name(i))
                    self.progress_show_l.setText(self.get_pic_name(i) + " converted")
                except OSError as e:
                    self.error_show_l.setText(e)
                    pass
        elif self.direction == "상하좌우":

            for i in self.pic_data:
                try:
                    img = Image.open(i)
                    img_resize = img.resize((int(img.width * (1 - self.percentage/100)), int(img.height * (1 - self.percentage/100))))
                    img_resize.save(self.save_loc + self.get_pic_name(i))
                    self.progress_show_l.setText(self.get_pic_name(i) + " converted")
                except OSError as e:
                    self.error_show_l.setText(e)
                    pass
            self.progress_show_l.setText("Process Finished")
        else :
            self.error_show_l.setText("No location has selected")

    def save_pic(self):
        self.save_loc = QFileDialog.getExistingDirectory(self, "Save Folder")
        self.save_loc_lb.setText(self.save_loc)



if __name__ == "__main__" :
    #QApplication : 프로그램을 실행시켜주는 클래스
    app = QApplication(sys.argv)
    #WindowClass의 인스턴스 생성
    myWindow = WindowClass()
    #프로그램 화면을 보여주는 코드
    myWindow.show()
    #프로그램을 이벤트루프로 진입시키는(프로그램을 작동시키는) 코드
    app.exec_()