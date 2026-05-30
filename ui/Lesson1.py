from PySide6.QtCore import QRect, Qt
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QLineEdit, QWidget

from qt_ui_py.login_ui import Ui_Form

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        btn = QPushButton("按钮", self)
        btn.setGeometry(QRect(0, 0, 200, 100))
        btn.setToolTip("看点提示")

        label = QLabel("我是你爹我是你爹我是你爹我是你爹我是你爹",self)

        line_edit = QLineEdit(self)
        line_edit.setPlaceholderText("输入点什么")
        return

class WindowWithUiForm(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        # 也可以私有这个ui  self.ui_form = Ui_Form() self.ui_form.setupUi(self)
        self.setupUi(self)
        pass

def run_lesson_one() -> None:
    """
    连续执行两次 会出现错误 libshiboken: Please destroy the QApplication singleton before creating a new QApplication instance.
    """
    app = QApplication([])
    # window = MyWindow()
    # window.show()

    window = WindowWithUiForm()
    window.show()

    return_code = app.exec()
    print("程序运行结束: {}".format(return_code))
    return