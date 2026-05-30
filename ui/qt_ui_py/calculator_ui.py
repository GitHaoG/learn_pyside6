# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'calculator.ui'
##
## Created by: Qt User Interface Compiler version 6.11.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLineEdit, QPushButton,
    QSizePolicy, QVBoxLayout, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(342, 260)
        self.verticalLayout_3 = QVBoxLayout(Form)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.input = QLineEdit(Form)
        self.input.setObjectName(u"input")
        self.input.setMinimumSize(QSize(200, 50))

        self.verticalLayout_2.addWidget(self.input)

        self.back = QPushButton(Form)
        self.back.setObjectName(u"back")

        self.verticalLayout_2.addWidget(self.back)

        self.delete_all = QPushButton(Form)
        self.delete_all.setObjectName(u"delete_all")

        self.verticalLayout_2.addWidget(self.delete_all)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.btn_7 = QPushButton(Form)
        self.btn_7.setObjectName(u"btn_7")

        self.horizontalLayout_4.addWidget(self.btn_7)

        self.btn_8 = QPushButton(Form)
        self.btn_8.setObjectName(u"btn_8")

        self.horizontalLayout_4.addWidget(self.btn_8)

        self.btn_9 = QPushButton(Form)
        self.btn_9.setObjectName(u"btn_9")

        self.horizontalLayout_4.addWidget(self.btn_9)

        self.btn_divide = QPushButton(Form)
        self.btn_divide.setObjectName(u"btn_divide")

        self.horizontalLayout_4.addWidget(self.btn_divide)


        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.btn_4 = QPushButton(Form)
        self.btn_4.setObjectName(u"btn_4")

        self.horizontalLayout_3.addWidget(self.btn_4)

        self.btn_5 = QPushButton(Form)
        self.btn_5.setObjectName(u"btn_5")

        self.horizontalLayout_3.addWidget(self.btn_5)

        self.btn_6 = QPushButton(Form)
        self.btn_6.setObjectName(u"btn_6")

        self.horizontalLayout_3.addWidget(self.btn_6)

        self.btn_multiple = QPushButton(Form)
        self.btn_multiple.setObjectName(u"btn_multiple")

        self.horizontalLayout_3.addWidget(self.btn_multiple)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.btn_1 = QPushButton(Form)
        self.btn_1.setObjectName(u"btn_1")

        self.horizontalLayout_2.addWidget(self.btn_1)

        self.btn_2 = QPushButton(Form)
        self.btn_2.setObjectName(u"btn_2")

        self.horizontalLayout_2.addWidget(self.btn_2)

        self.btn_3 = QPushButton(Form)
        self.btn_3.setObjectName(u"btn_3")

        self.horizontalLayout_2.addWidget(self.btn_3)

        self.btn_minus = QPushButton(Form)
        self.btn_minus.setObjectName(u"btn_minus")

        self.horizontalLayout_2.addWidget(self.btn_minus)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.btn_dot = QPushButton(Form)
        self.btn_dot.setObjectName(u"btn_dot")

        self.horizontalLayout.addWidget(self.btn_dot)

        self.btn_zero = QPushButton(Form)
        self.btn_zero.setObjectName(u"btn_zero")

        self.horizontalLayout.addWidget(self.btn_zero)

        self.btn_calculate = QPushButton(Form)
        self.btn_calculate.setObjectName(u"btn_calculate")

        self.horizontalLayout.addWidget(self.btn_calculate)

        self.btn_add = QPushButton(Form)
        self.btn_add.setObjectName(u"btn_add")

        self.horizontalLayout.addWidget(self.btn_add)


        self.verticalLayout.addLayout(self.horizontalLayout)


        self.verticalLayout_2.addLayout(self.verticalLayout)


        self.verticalLayout_3.addLayout(self.verticalLayout_2)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"\u8ba1\u7b97\u5668", None))
        self.back.setText(QCoreApplication.translate("Form", u"\u9000\u683c", None))
        self.delete_all.setText(QCoreApplication.translate("Form", u"\u5220\u9664", None))
        self.btn_7.setText(QCoreApplication.translate("Form", u"7", None))
        self.btn_8.setText(QCoreApplication.translate("Form", u"8", None))
        self.btn_9.setText(QCoreApplication.translate("Form", u"9", None))
        self.btn_divide.setText(QCoreApplication.translate("Form", u"/", None))
        self.btn_4.setText(QCoreApplication.translate("Form", u"4", None))
        self.btn_5.setText(QCoreApplication.translate("Form", u"5", None))
        self.btn_6.setText(QCoreApplication.translate("Form", u"6", None))
        self.btn_multiple.setText(QCoreApplication.translate("Form", u"x", None))
        self.btn_1.setText(QCoreApplication.translate("Form", u"1", None))
        self.btn_2.setText(QCoreApplication.translate("Form", u"2", None))
        self.btn_3.setText(QCoreApplication.translate("Form", u"3", None))
        self.btn_minus.setText(QCoreApplication.translate("Form", u"-", None))
        self.btn_dot.setText(QCoreApplication.translate("Form", u".", None))
        self.btn_zero.setText(QCoreApplication.translate("Form", u"0", None))
        self.btn_calculate.setText(QCoreApplication.translate("Form", u"\u8ba1\u7b97", None))
        self.btn_add.setText(QCoreApplication.translate("Form", u"+", None))
    # retranslateUi

