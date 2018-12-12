import sys
from PyQt5.QtWidgets import *

class my_widget(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.url_and_comments()     #url 입력 박스가 포함된 스크롤 에리어
        self.dictionary()           #사전 내용을 포함하는 프레임
        self.translation()          #번역 내용을 포함하는 프레임

        self.show()
        self.resize(1000,500)
        self.setStyleSheet('background: #DDDDDD')

    #위젯의 왼쪽에 해당하는 부분
    def url_and_comments(self):
        url_and_comments = QScrollArea(self)
        url_and_comments.resize(500, 500)
        url_and_comments.move(0, 0)
        url_and_comments.setStyleSheet('background: #DDDDDD')

        # URL 입력박스
        url_input = QLineEdit(url_and_comments)
        url_input.resize(300, 35)
        url_input.move(50, 50)
        url_input.setStyleSheet('color:black; background:white')  # color는 폰트의 색깔을 의미함

        # 댓글 분석 버튼
        url_analysis = QPushButton('분석', url_and_comments)
        url_analysis.resize(55, 40)
        url_analysis.move(360, 47)
        url_analysis.setStyleSheet('color:black; background:white')

        #스크롤 바 생성(동작 안함)
        scroll_bar = QScrollBar(url_and_comments)
        scroll_bar.setOrientation(0)
        scroll_bar.move(479, 0)
        scroll_bar.resize(20, 500)

        self.add_coments()

    #덧글 추가 메소드(반복문을 통해 자동생성 가능하도록 수정해야 함)
    def add_coments(self):
        comment_label = QLabel(self)
        comment_label.resize(300,25)
        comment_label.move(45,120+50)
        comment_label.setStyleSheet('background : white')

        comment_button = QPushButton('사전 검색', self)
        comment_button.resize(80,29)
        comment_button.move(355, 118+50)

    #사전 내용 추가 메소드
    def dictionary(self):
        dic_label = QLabel('<b>사전 내용<b/>', self)
        dic_label.resize(500,250)
        dic_label.move(500,0)
        dic_label.setStyleSheet('background: white')

    #번역 내용 추가 메소드
    def translation(self):
        trans_label = QLabel('<b>번역 내용<b/>', self)
        trans_label.resize(500, 250)
        trans_label.move(500, 251)
        trans_label.setStyleSheet('background: #AAAAAA')




app = QApplication(sys.argv)
w = my_widget()
sys.exit(app.exec_())
