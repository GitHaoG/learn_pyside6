from loguru import logger

from PySide6.QtCore import QRect, Qt
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QLineEdit


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

if __name__ == '__main__':
    app = QApplication([])
    window = MyWindow()
    window.show()

    return_code = app.exec()
    logger.info("程序运行结束: {}".format(return_code))
    pass
