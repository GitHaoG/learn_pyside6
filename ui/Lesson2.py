import re
from PySide6.QtWidgets import QWidget, QVBoxLayout, QPushButton, QApplication
from qt_ui_py.login_ui import Ui_Form as LoginForm
from qt_ui_py.calculator_ui import Ui_Form as CalculatorForm

class MyWindowForSignal(QWidget):
    def __init__(self):
        super().__init__()

        main_layout = QVBoxLayout(self)

        button = QPushButton("点击发出信号")
        # click 信号
        button.clicked.connect(self.hello)

        main_layout.addWidget(button)
        self.setLayout(main_layout)

    def hello(self):
        print("button clicked")

class LoginWithSignal(QWidget, LoginForm):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.pushButton.clicked.connect(self.loginFunc)

    def loginFunc(self):
        name = self.lineEdit.text()
        password = self.lineEdit_2.text()

        if name == "" or password == "":
            print("请输入密码或账号")
            return

        if name == "123" and password == "123":
            print("登陆成功")
        else:
            print("密码或账号错误")

class Calculator(QWidget, CalculatorForm):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setFixedSize(self.width(), self.height())
        self.calculate_str = ""
        self.bind_signal()

    def bind_signal(self):
        self.btn_zero.clicked.connect(lambda: self.addNumber('0'))
        self.btn_1.clicked.connect(lambda: self.addNumber('1'))
        self.btn_2.clicked.connect(lambda: self.addNumber('2'))
        self.btn_3.clicked.connect(lambda: self.addNumber('3'))
        self.btn_4.clicked.connect(lambda: self.addNumber('4'))
        self.btn_5.clicked.connect(lambda: self.addNumber('5'))
        self.btn_6.clicked.connect(lambda: self.addNumber('6'))
        self.btn_7.clicked.connect(lambda: self.addNumber('7'))
        self.btn_8.clicked.connect(lambda: self.addNumber('8'))
        self.btn_9.clicked.connect(lambda: self.addNumber('9'))
        self.btn_dot.clicked.connect(lambda: self.addNumber('.'))
        self.btn_minus.clicked.connect(lambda: self.addNumber('-'))
        self.btn_add.clicked.connect(lambda: self.addNumber('+'))
        self.btn_multiple.clicked.connect(lambda: self.addNumber('*'))
        self.btn_divide.clicked.connect(lambda: self.addNumber('/'))

        self.btn_calculate.clicked.connect(self.calculateStr)
        self.back.clicked.connect(self.backOneChar)
        self.delete_all.clicked.connect(self.deleteString)
        pass

    def addNumber(self, number: str):
        self.calculate_str += number
        self.input.setText(self.calculate_str)
        return

    def backOneChar(self):
        if self.calculate_str.__len__() == 0:
            return
        self.calculate_str = self.calculate_str[:-1]
        self.input.setText(self.calculate_str)

    def deleteString(self):
        self.calculate_str = ""
        self.input.setText(self.calculate_str)

    def calculateStr(self):
        def check(s: str) -> bool:
            return bool(re.fullmatch(r'[0-9+\-*/.]+', s))

        try:
            if check(self.calculate_str):
                self.input.clear()
                self.input.setText(str(eval(self.calculate_str)))
                self.calculate_str = ""
        except Exception:
            self.input.clear()
            self.input.setText("Invalid input")

def run_lesson2_example1():
    # 介绍信号与槽
    app = QApplication([])
    window = MyWindowForSignal()
    # window = LoginWithSignal()
    window.show()
    app.exec()
    return

def run_lesson2_example2():
    # 介绍信号与槽
    app = QApplication([])
    # window = MyWindowForSignal()
    window = LoginWithSignal()
    window.show()
    app.exec()
    return

def run_calculator():
    app = QApplication([])
    window = Calculator()
    window.show()
    app.exec()
    return
