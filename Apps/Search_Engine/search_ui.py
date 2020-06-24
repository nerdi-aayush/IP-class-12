from PyQt5 import QtCore, QtGui, QtWidgets
import requests

API_KEY = 'API KEY FROM GOOGLE'
SEARCH_ENGINE_ID = 'EARCHID FROM GOOGLE'


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1280, 720)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.search_btn = QtWidgets.QPushButton(self.centralwidget)
        self.search_btn.setGeometry(QtCore.QRect(720, 20, 111, 41))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("assets/icons8-search.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.search_btn.setIcon(icon)
        self.search_btn.setObjectName("search_btn")
        self.search_btn.clicked.connect(lambda: self.retranslateUi(MainWindow))
        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setGeometry(QtCore.QRect(10, 70, 1261, 631))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 1238, 2048))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout.setObjectName("verticalLayout")
        self.title_1 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.title_1.setFont(font)
        self.title_1.setOpenExternalLinks(True)
        self.title_1.setObjectName("title_1")
        self.verticalLayout.addWidget(self.title_1)
        self.domain_1 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        font = QtGui.QFont()
        font.setPointSize(6)
        self.domain_1.setFont(font)
        self.domain_1.setObjectName("domain_1")
        self.verticalLayout.addWidget(self.domain_1)
        self.desc_1 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.desc_1.setFont(font)
        self.desc_1.setScaledContents(False)
        self.desc_1.setWordWrap(True)
        self.desc_1.setIndent(0)
        self.desc_1.setObjectName("desc_1")
        self.verticalLayout.addWidget(self.desc_1)
        self.blank_1 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.blank_1.setText("")
        self.blank_1.setObjectName("blank_1")
        self.verticalLayout.addWidget(self.blank_1)
        self.title_2 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.title_2.setFont(font)
        self.title_2.setOpenExternalLinks(True)
        self.title_2.setObjectName("title_2")
        self.verticalLayout.addWidget(self.title_2)
        self.domain_2 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        font = QtGui.QFont()
        font.setPointSize(6)
        self.domain_2.setFont(font)
        self.domain_2.setObjectName("domain_2")
        self.verticalLayout.addWidget(self.domain_2)
        self.desc_2 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.desc_2.setFont(font)
        self.desc_2.setWordWrap(True)
        self.desc_2.setObjectName("desc_2")
        self.verticalLayout.addWidget(self.desc_2)
        self.blank_2 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.blank_2.setText("")
        self.blank_2.setObjectName("blank_2")
        self.verticalLayout.addWidget(self.blank_2)
        self.title_3 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.title_3.setFont(font)
        self.title_3.setOpenExternalLinks(True)
        self.title_3.setObjectName("title_3")
        self.verticalLayout.addWidget(self.title_3)
        self.domain_3 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        font = QtGui.QFont()
        font.setPointSize(6)
        self.domain_3.setFont(font)
        self.domain_3.setObjectName("domain_3")
        self.verticalLayout.addWidget(self.domain_3)
        self.desc_3 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.desc_3.setFont(font)
        self.desc_3.setWordWrap(True)
        self.desc_3.setObjectName("desc_3")
        self.verticalLayout.addWidget(self.desc_3)
        self.blank_3 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.blank_3.setText("")
        self.blank_3.setObjectName("blank_3")
        self.verticalLayout.addWidget(self.blank_3)
        self.title_4 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.title_4.setFont(font)
        self.title_4.setOpenExternalLinks(True)
        self.title_4.setObjectName("title_4")
        self.verticalLayout.addWidget(self.title_4)
        self.domain_4 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        font = QtGui.QFont()
        font.setPointSize(6)
        self.domain_4.setFont(font)
        self.domain_4.setObjectName("domain_4")
        self.verticalLayout.addWidget(self.domain_4)
        self.desc_4 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.desc_4.setFont(font)
        self.desc_4.setWordWrap(True)
        self.desc_4.setObjectName("desc_4")
        self.verticalLayout.addWidget(self.desc_4)
        self.blank_4 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.blank_4.setText("")
        self.blank_4.setObjectName("blank_4")
        self.verticalLayout.addWidget(self.blank_4)
        self.title_5 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.title_5.setFont(font)
        self.title_5.setOpenExternalLinks(True)
        self.title_5.setObjectName("title_5")
        self.verticalLayout.addWidget(self.title_5)
        self.domain_5 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        font = QtGui.QFont()
        font.setPointSize(6)
        self.domain_5.setFont(font)
        self.domain_5.setObjectName("domain_5")
        self.verticalLayout.addWidget(self.domain_5)
        self.desc_5 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.desc_5.setFont(font)
        self.desc_5.setWordWrap(True)
        self.desc_5.setObjectName("desc_5")
        self.verticalLayout.addWidget(self.desc_5)
        self.blank_5 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.blank_5.setText("")
        self.blank_5.setObjectName("blank_5")
        self.verticalLayout.addWidget(self.blank_5)
        self.title_6 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.title_6.setFont(font)
        self.title_6.setOpenExternalLinks(True)
        self.title_6.setObjectName("title_6")
        self.verticalLayout.addWidget(self.title_6)
        self.domain_6 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        font = QtGui.QFont()
        font.setPointSize(6)
        self.domain_6.setFont(font)
        self.domain_6.setObjectName("domain_6")
        self.verticalLayout.addWidget(self.domain_6)
        self.desc_6 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.desc_6.setFont(font)
        self.desc_6.setWordWrap(True)
        self.desc_6.setObjectName("desc_6")
        self.verticalLayout.addWidget(self.desc_6)
        self.blank_6 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.blank_6.setText("")
        self.blank_6.setObjectName("blank_6")
        self.verticalLayout.addWidget(self.blank_6)
        self.title_7 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.title_7.setFont(font)
        self.title_7.setOpenExternalLinks(True)
        self.title_7.setObjectName("title_7")
        self.verticalLayout.addWidget(self.title_7)
        self.domain_7 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        font = QtGui.QFont()
        font.setPointSize(6)
        self.domain_7.setFont(font)
        self.domain_7.setObjectName("domain_7")
        self.verticalLayout.addWidget(self.domain_7)
        self.desc_7 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.desc_7.setFont(font)
        self.desc_7.setWordWrap(True)
        self.desc_7.setObjectName("desc_7")
        self.verticalLayout.addWidget(self.desc_7)
        self.blank_7 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.blank_7.setText("")
        self.blank_7.setObjectName("blank_7")
        self.verticalLayout.addWidget(self.blank_7)
        self.title_8 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.title_8.setFont(font)
        self.title_8.setOpenExternalLinks(True)
        self.title_8.setObjectName("title_8")
        self.verticalLayout.addWidget(self.title_8)
        self.domain_8 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        font = QtGui.QFont()
        font.setPointSize(6)
        self.domain_8.setFont(font)
        self.domain_8.setObjectName("domain_8")
        self.verticalLayout.addWidget(self.domain_8)
        self.desc_8 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.desc_8.setFont(font)
        self.desc_8.setWordWrap(True)
        self.desc_8.setObjectName("desc_8")
        self.verticalLayout.addWidget(self.desc_8)
        self.blank_8 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.blank_8.setText("")
        self.blank_8.setObjectName("blank_8")
        self.verticalLayout.addWidget(self.blank_8)
        self.title_9 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.title_9.setFont(font)
        self.title_9.setOpenExternalLinks(True)
        self.title_9.setObjectName("title_9")
        self.verticalLayout.addWidget(self.title_9)
        self.domain_9 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        font = QtGui.QFont()
        font.setPointSize(6)
        self.domain_9.setFont(font)
        self.domain_9.setObjectName("domain_9")
        self.verticalLayout.addWidget(self.domain_9)
        self.desc_9 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.desc_9.setFont(font)
        self.desc_9.setWordWrap(True)
        self.desc_9.setObjectName("desc_9")
        self.verticalLayout.addWidget(self.desc_9)
        self.blank_9 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.blank_9.setText("")
        self.blank_9.setObjectName("blank_9")
        self.verticalLayout.addWidget(self.blank_9)
        self.title_10 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.title_10.setFont(font)
        self.title_10.setOpenExternalLinks(True)
        self.title_10.setObjectName("title_10")
        self.verticalLayout.addWidget(self.title_10)
        self.domain_10 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        font = QtGui.QFont()
        font.setPointSize(6)
        self.domain_10.setFont(font)
        self.domain_10.setObjectName("domain_10")
        self.verticalLayout.addWidget(self.domain_10)
        self.desc_10 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.desc_10.setFont(font)
        self.desc_10.setWordWrap(True)
        self.desc_10.setObjectName("desc_10")
        self.verticalLayout.addWidget(self.desc_10)
        self.blank_10 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.blank_10.setText("")
        self.blank_10.setObjectName("blank_10")
        self.verticalLayout.addWidget(self.blank_10)
        # self.title_11 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        # font = QtGui.QFont()
        # font.setPointSize(15)
        # self.title_11.setFont(font)
        # self.title_11.setOpenExternalLinks(True)
        # self.title_11.setObjectName("title_11")
        # self.verticalLayout.addWidget(self.title_11)
        # self.domain_11 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        # font = QtGui.QFont()
        # font.setPointSize(6)
        # self.domain_11.setFont(font)
        # self.domain_11.setObjectName("domain_11")
        # self.verticalLayout.addWidget(self.domain_11)
        # self.desc_11 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        # font = QtGui.QFont()
        # font.setPointSize(10)
        # self.desc_11.setFont(font)
        # self.desc_11.setWordWrap(True)
        # self.desc_11.setObjectName("desc_11")
        # self.verticalLayout.addWidget(self.desc_11)
        # self.blank_11 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        # self.blank_11.setText("")
        # self.blank_11.setObjectName("blank_11")
        # self.verticalLayout.addWidget(self.blank_11)
        # self.title_12 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        # font = QtGui.QFont()
        # font.setPointSize(15)
        # self.title_12.setFont(font)
        # self.title_12.setOpenExternalLinks(True)
        # self.title_12.setObjectName("title_12")
        # self.verticalLayout.addWidget(self.title_12)
        # self.domain_12 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        # font = QtGui.QFont()
        # font.setPointSize(6)
        # self.domain_12.setFont(font)
        # self.domain_12.setObjectName("domain_12")
        # self.verticalLayout.addWidget(self.domain_12)
        # self.desc_12 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        # font = QtGui.QFont()
        # font.setPointSize(10)
        # self.desc_12.setFont(font)
        # self.desc_12.setWordWrap(True)
        # self.desc_12.setObjectName("desc_12")
        # self.verticalLayout.addWidget(self.desc_12)
        # self.blank_12 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        # self.blank_12.setText("")
        # self.blank_12.setObjectName("blank_12")
        # self.verticalLayout.addWidget(self.blank_12)
        # self.title_13 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        # font = QtGui.QFont()
        # font.setPointSize(15)
        # self.title_13.setFont(font)
        # self.title_13.setOpenExternalLinks(True)
        # self.title_13.setObjectName("title_13")
        # self.verticalLayout.addWidget(self.title_13)
        # self.domain_13 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        # font = QtGui.QFont()
        # font.setPointSize(6)
        # self.domain_13.setFont(font)
        # self.domain_13.setObjectName("domain_13")
        # self.verticalLayout.addWidget(self.domain_13)
        # self.desc_13 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        # font = QtGui.QFont()
        # font.setPointSize(10)
        # self.desc_13.setFont(font)
        # self.desc_13.setWordWrap(True)
        # self.desc_13.setObjectName("desc_13")
        # self.verticalLayout.addWidget(self.desc_13)
        # self.blank_13 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        # self.blank_13.setText("")
        # self.blank_13.setObjectName("blank_13")
        # self.verticalLayout.addWidget(self.blank_13)
        # self.title_14 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        # font = QtGui.QFont()
        # font.setPointSize(15)
        # self.title_14.setFont(font)
        # self.title_14.setOpenExternalLinks(True)
        # self.title_14.setObjectName("title_14")
        # self.verticalLayout.addWidget(self.title_14)
        # self.domain_14 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        # font = QtGui.QFont()
        # font.setPointSize(6)
        # self.domain_14.setFont(font)
        # self.domain_14.setObjectName("domain_14")
        # self.verticalLayout.addWidget(self.domain_14)
        # self.desc_14 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        # font = QtGui.QFont()
        # font.setPointSize(10)
        # self.desc_14.setFont(font)
        # self.desc_14.setWordWrap(True)
        # self.desc_14.setObjectName("desc_14")
        # self.verticalLayout.addWidget(self.desc_14)
        # self.blank_14 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        # self.blank_14.setText("")
        # self.blank_14.setObjectName("blank_14")
        # self.verticalLayout.addWidget(self.blank_14)
        # self.title_15 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        # font = QtGui.QFont()
        # font.setPointSize(15)
        # self.title_15.setFont(font)
        # self.title_15.setOpenExternalLinks(True)
        # self.title_15.setObjectName("title_15")
        # self.verticalLayout.addWidget(self.title_15)
        # self.domain_15 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        # font = QtGui.QFont()
        # font.setPointSize(6)
        # self.domain_15.setFont(font)
        # self.domain_15.setObjectName("domain_15")
        # self.verticalLayout.addWidget(self.domain_15)
        # self.desc_15 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        # font = QtGui.QFont()
        # font.setPointSize(10)
        # self.desc_15.setFont(font)
        # self.desc_15.setWordWrap(True)
        # self.desc_15.setObjectName("desc_15")
        # self.verticalLayout.addWidget(self.desc_15)
        # self.blank_15 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        # self.blank_15.setText("")
        # self.blank_15.setObjectName("blank_15")
        # self.verticalLayout.addWidget(self.blank_15)
        # self.title_16 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        # font = QtGui.QFont()
        # font.setPointSize(15)
        # self.title_16.setFont(font)
        # self.title_16.setOpenExternalLinks(True)
        # self.title_16.setObjectName("title_16")
        # self.verticalLayout.addWidget(self.title_16)
        # self.domain_16 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        # font = QtGui.QFont()
        # font.setPointSize(6)
        # self.domain_16.setFont(font)
        # self.domain_16.setObjectName("domain_16")
        # self.verticalLayout.addWidget(self.domain_16)
        # self.desc_16 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        # font = QtGui.QFont()
        # font.setPointSize(10)
        # self.desc_16.setFont(font)
        # self.desc_16.setWordWrap(True)
        # self.desc_16.setObjectName("desc_16")
        # self.verticalLayout.addWidget(self.desc_16)
        # self.blank_16 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        # self.blank_16.setText("")
        # self.blank_16.setObjectName("blank_16")
        # self.verticalLayout.addWidget(self.blank_16)
        # self.title_17 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        # font = QtGui.QFont()
        # font.setPointSize(15)
        # self.title_17.setFont(font)
        # self.title_17.setOpenExternalLinks(True)
        # self.title_17.setObjectName("title_17")
        # self.verticalLayout.addWidget(self.title_17)
        # self.domain_17 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        # font = QtGui.QFont()
        # font.setPointSize(6)
        # self.domain_17.setFont(font)
        # self.domain_17.setObjectName("domain_17")
        # self.verticalLayout.addWidget(self.domain_17)
        # self.desc_17 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        # font = QtGui.QFont()
        # font.setPointSize(10)
        # self.desc_17.setFont(font)
        # self.desc_17.setWordWrap(True)
        # self.desc_17.setObjectName("desc_17")
        # self.verticalLayout.addWidget(self.desc_17)
        # self.blank_17 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        # self.blank_17.setText("")
        # self.blank_17.setObjectName("blank_17")
        # self.verticalLayout.addWidget(self.blank_17)
        # self.title_18 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        # font = QtGui.QFont()
        # font.setPointSize(15)
        # self.title_18.setFont(font)
        # self.title_18.setOpenExternalLinks(True)
        # self.title_18.setObjectName("title_18")
        # self.verticalLayout.addWidget(self.title_18)
        # self.domain_18 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        # font = QtGui.QFont()
        # font.setPointSize(6)
        # self.domain_18.setFont(font)
        # self.domain_18.setObjectName("domain_18")
        # self.verticalLayout.addWidget(self.domain_18)
        # self.desc_18 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        # font = QtGui.QFont()
        # font.setPointSize(10)
        # self.desc_18.setFont(font)
        # self.desc_18.setWordWrap(True)
        # self.desc_18.setObjectName("desc_18")
        # self.verticalLayout.addWidget(self.desc_18)
        # self.blank_18 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        # self.blank_18.setText("")
        # self.blank_18.setObjectName("blank_18")
        # self.verticalLayout.addWidget(self.blank_18)
        # self.title_19 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        # font = QtGui.QFont()
        # font.setPointSize(15)
        # self.title_19.setFont(font)
        # self.title_19.setOpenExternalLinks(True)
        # self.title_19.setObjectName("title_19")
        # self.verticalLayout.addWidget(self.title_19)
        # self.domain_19 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        # font = QtGui.QFont()
        # font.setPointSize(6)
        # self.domain_19.setFont(font)
        # self.domain_19.setObjectName("domain_19")
        # self.verticalLayout.addWidget(self.domain_19)
        # self.desc_19 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        # font = QtGui.QFont()
        # font.setPointSize(10)
        # self.desc_19.setFont(font)
        # self.desc_19.setWordWrap(True)
        # self.desc_19.setObjectName("desc_19")
        # self.verticalLayout.addWidget(self.desc_19)
        # self.blank_19 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        # self.blank_19.setText("")
        # self.blank_19.setObjectName("blank_19")
        # self.verticalLayout.addWidget(self.blank_19)
        #
        # self.title_20 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        # font = QtGui.QFont()
        # font.setPointSize(15)
        # self.title_20.setFont(font)
        # self.title_20.setOpenExternalLinks(True)
        # self.title_20.setObjectName("title_20")
        # self.verticalLayout.addWidget(self.title_20)
        # self.domain_20 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        # font = QtGui.QFont()
        # font.setPointSize(6)
        # self.domain_20.setFont(font)
        # self.domain_20.setObjectName("domain_20")
        # self.verticalLayout.addWidget(self.domain_20)
        # self.desc_20 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        # font = QtGui.QFont()
        # font.setPointSize(10)
        # self.desc_20.setFont(font)
        # self.desc_20.setWordWrap(True)
        # self.desc_20.setObjectName("desc_20")
        # self.verticalLayout.addWidget(self.desc_20)
        # self.blank_20 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        # self.blank_20.setText("")
        # self.blank_20.setObjectName("blank_20")
        # self.verticalLayout.addWidget(self.blank_20)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.search_input = QtWidgets.QLineEdit(self.centralwidget)
        self.search_input.setGeometry(QtCore.QRect(10, 20, 701, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.search_input.setFont(font)
        self.search_input.setObjectName("search_input")
        self.search_btn.setText("Search")
        MainWindow.setCentralWidget(self.centralwidget)
        MainWindow.setWindowTitle("Search Engine")
        MainWindow.setWindowIcon(QtGui.QIcon(r'assets\icon.png'))
        #self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        if self.search_input.text().strip() != '':
            _translate = QtCore.QCoreApplication.translate
            query = self.search_input.text()
            self.search_input.setText('')
            num_pg = 1

            page = 1

            start = (page - 1) * 10 + 1
            url = f"https://www.googleapis.com/customsearch/v1?key={API_KEY}&cx={SEARCH_ENGINE_ID}&q={query}&start={start}"
            data = requests.get(url).json()
            print(data)
            search_items1 = data.get('items')

            # page = 2
            # start = (page - 1) * 10 + 1
            # url = f"https://www.googleapis.com/customsearch/v1?key={API_KEY}&cx={SEARCH_ENGINE_ID}&q={query}&start={start}"
            # data = requests.get(url).json()
            # search_items2 = data.get('items')

            z=0
            self.title_1.setText(_translate("MainWindow", f"<a href=\'{search_items1[z].get('link')}\'>{search_items1[z].get('title')}</p>"))
            self.domain_1.setText(_translate("MainWindow", search_items1[z].get('displayLink')))
            self.desc_1.setText(_translate("MainWindow", search_items1[z].get('htmlSnippet')))

            z+=1

            self.title_2.setText(
                _translate("MainWindow", f"<a href=\'{search_items1[z].get('link')}\'>{search_items1[z].get('title')}</p>"))
            self.domain_2.setText(_translate("MainWindow", search_items1[z].get('displayLink')))
            self.desc_2.setText(_translate("MainWindow", search_items1[z].get('htmlSnippet')))

            z+=1

            self.title_3.setText(
                _translate("MainWindow", f"<a href=\'{search_items1[z].get('link')}\'>{search_items1[z].get('title')}</p>"))
            self.domain_3.setText(_translate("MainWindow", search_items1[z].get('displayLink')))
            self.desc_3.setText(_translate("MainWindow", search_items1[z].get('htmlSnippet')))

            z += 1

            self.title_4.setText(
                _translate("MainWindow", f"<a href=\'{search_items1[z].get('link')}\'>{search_items1[z].get('title')}</p>"))
            self.domain_4.setText(_translate("MainWindow", search_items1[z].get('displayLink')))
            self.desc_4.setText(_translate("MainWindow", search_items1[z].get('htmlSnippet')))

            z += 1

            self.title_5.setText(
                _translate("MainWindow", f"<a href=\'{search_items1[z].get('link')}\'>{search_items1[z].get('title')}</p>"))
            self.domain_5.setText(_translate("MainWindow", search_items1[z].get('displayLink')))
            self.desc_5.setText(_translate("MainWindow", search_items1[z].get('htmlSnippet')))

            z += 1

            self.title_6.setText(
                _translate("MainWindow", f"<a href=\'{search_items1[z].get('link')}\'>{search_items1[z].get('title')}</p>"))
            self.domain_6.setText(_translate("MainWindow", search_items1[z].get('displayLink')))
            self.desc_6.setText(_translate("MainWindow", search_items1[z].get('htmlSnippet')))

            z += 1

            self.title_7.setText(
                _translate("MainWindow", f"<a href=\'{search_items1[z].get('link')}\'>{search_items1[z].get('title')}</p>"))
            self.domain_7.setText(_translate("MainWindow", search_items1[z].get('displayLink')))
            self.desc_7.setText(_translate("MainWindow", search_items1[z].get('htmlSnippet')))

            z += 1

            self.title_8.setText(
                _translate("MainWindow", f"<a href=\'{search_items1[z].get('link')}\'>{search_items1[z].get('title')}</p>"))
            self.domain_8.setText(_translate("MainWindow", search_items1[z].get('displayLink')))
            self.desc_8.setText(_translate("MainWindow", search_items1[z].get('htmlSnippet')))

            z += 1

            self.title_9.setText(
                _translate("MainWindow", f"<a href=\'{search_items1[z].get('link')}\'>{search_items1[z].get('title')}</p>"))
            self.domain_9.setText(_translate("MainWindow", search_items1[z].get('displayLink')))
            self.desc_9.setText(_translate("MainWindow", search_items1[z].get('htmlSnippet')))

            z += 1

            self.title_10.setText(
                _translate("MainWindow", f"<a href=\'{search_items1[z].get('link')}\'>{search_items1[z].get('title')}</p>"))
            self.domain_10.setText(_translate("MainWindow", search_items1[z].get('displayLink')))
            self.desc_10.setText(_translate("MainWindow", search_items1[z].get('htmlSnippet')))

            # z = 0
            #
            # self.title_11.setText(
            #     _translate("MainWindow", f"<a href=\'{search_items2[z].get('link')}\'>{search_items2[z].get('title')}</p>"))
            # self.domain_11.setText(_translate("MainWindow", search_items2[z].get('displayLink')))
            # self.desc_11.setText(_translate("MainWindow", search_items2[z].get('htmlSnippet')))
            #
            # z += 1
            #
            # self.title_12.setText(
            #     _translate("MainWindow", f"<a href=\'{search_items2[z].get('link')}\'>{search_items2[z].get('title')}</p>"))
            # self.domain_12.setText(_translate("MainWindow", search_items2[z].get('displayLink')))
            # self.desc_12.setText(_translate("MainWindow", search_items2[z].get('htmlSnippet')))
            # z += 1
            #
            # self.title_13.setText(
            #     _translate("MainWindow", f"<a href=\'{search_items2[z].get('link')}\'>{search_items2[z].get('title')}</p>"))
            # self.domain_13.setText(_translate("MainWindow", search_items2[z].get('displayLink')))
            # self.desc_13.setText(_translate("MainWindow", search_items2[z].get('htmlSnippet')))
            #
            # z += 1
            #
            # self.title_14.setText(
            #     _translate("MainWindow", f"<a href=\'{search_items2[z].get('link')}\'>{search_items2[z].get('title')}</p>"))
            # self.domain_14.setText(_translate("MainWindow", search_items2[z].get('displayLink')))
            # self.desc_14.setText(_translate("MainWindow", search_items2[z].get('htmlSnippet')))
            #
            # z += 1
            #
            # self.title_15.setText(
            #     _translate("MainWindow", f"<a href=\'{search_items2[z].get('link')}\'>{search_items2[z].get('title')}</p>"))
            # self.domain_15.setText(_translate("MainWindow", search_items2[z].get('displayLink')))
            # self.desc_15.setText(_translate("MainWindow", search_items2[z].get('htmlSnippet')))
            #
            # z += 1
            #
            # self.title_16.setText(
            #     _translate("MainWindow", f"<a href=\'{search_items2[z].get('link')}\'>{search_items2[z].get('title')}</p>"))
            # self.domain_16.setText(_translate("MainWindow", search_items2[z].get('displayLink')))
            # self.desc_16.setText(_translate("MainWindow", search_items2[z].get('htmlSnippet')))
            #
            # z += 1
            #
            # self.title_17.setText(
            #     _translate("MainWindow", f"<a href=\'{search_items2[z].get('link')}\'>{search_items2[z].get('title')}</p>"))
            # self.domain_17.setText(_translate("MainWindow", search_items2[z].get('displayLink')))
            # self.desc_17.setText(_translate("MainWindow", search_items2[z].get('htmlSnippet')))
            #
            # z += 1
            #
            # self.title_18.setText(
            #     _translate("MainWindow", f"<a href=\'{search_items2[z].get('link')}\'>{search_items2[z].get('title')}</p>"))
            # self.domain_18.setText(_translate("MainWindow", search_items2[z].get('displayLink')))
            # self.desc_18.setText(_translate("MainWindow", search_items2[z].get('htmlSnippet')))
            #
            # z += 1
            #
            # self.title_19.setText(
            #     _translate("MainWindow", f"<a href=\'{search_items2[z].get('link')}\'>{search_items2[z].get('title')}</p>"))
            # self.domain_19.setText(_translate("MainWindow", search_items2[z].get('displayLink')))
            # self.desc_19.setText(_translate("MainWindow", search_items2[z].get('htmlSnippet')))
            #
            # z += 1
            #
            # self.title_20.setText(
            #     _translate("MainWindow", f"<a href=\'{search_items2[z].get('link')}\'>{search_items2[z].get('title')}</p>"))
            # self.domain_20.setText(_translate("MainWindow", search_items2[z].get('displayLink')))
            # self.desc_20.setText(_translate("MainWindow", search_items2[z].get('htmlSnippet')))
        else:
            pass


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
