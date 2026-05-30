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

#### QPushButton、QLabel、QLineEditor

将parent设为self好像就能挂到窗体上

```txt
btn = QPushButton("按钮", self)
```

label 里面不只是可以放纯文本，像是图片、富文本都可以

line_editor 是用来做单行输入的

控件可以被修改的属性都可以通过设计师查看

#### 信号与槽

实现界面交互

ui 逻辑有两种实现

- pysimplegui -> 使用while循环不停刷新检查窗体状态 -> 不停地轮询
- pyqt -> 回调机制 -> 窗体发信号给 app的 slot -> app 进行处理这个signal


