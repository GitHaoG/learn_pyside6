# 学习pyside6

### 初步

#### 样板代码

初始化窗体与App类

```txt
app = QApplication([])
window = MyWindow()
window.show()

return_code = app.exec()
logger.info("程序运行结束: {}".format(return_code))
```

#### QPushButton、QLabel

将parent设为self好像就能挂到窗体上

```txt
btn = QPushButton("按钮", self)
```

label 里面能够放不只是可以放纯文本，像是图片、富文本都可以