import login
import interface
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow


class LoginWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = login.Ui_LoginWindow()
        self.ui.setupUi(self)
        # 隐藏窗口
        self.setWindowFlag(login.QtCore.Qt.FramelessWindowHint)
        self.setAttribute(login.QtCore.Qt.WA_TranslucentBackground)

        self.ui.pushButton_3.clicked.connect(self.login_in)
        self.show()

    def login_in(self):
        account = self.ui.lineEdit.text()
        passord = self.ui.lineEdit_2.text()
        if account == 'admin' and passord == '123456':
            self.win = interface.Ui_MainWindow()
            self.close()
        else:
            print('wrong!!!')

    def mousePressEvent(self, event):
        if event.button() == login.QtCore.Qt.LeftButton and self.isMaximized() == False:
            self.m_flag = True
            self.m_Position = event.globalPos() - self.pos()  # 获取鼠标相对窗口的位置
            event.accept()
            self.setCursor(login.QtGui.QCursor(login.QtCore.Qt.OpenHandCursor))  # 更改鼠标图标

    def mouseMoveEvent(self, mouse_event):
        if login.QtCore.Qt.LeftButton and self.m_flag:
            self.move(mouse_event.globalPos() - self.m_Position)  # 更改窗口位置
            mouse_event.accept()

    def mouseReleaseEvent(self, mouse_event):
        self.m_flag = False
        self.setCursor(login.QtGui.QCursor(login.QtCore.Qt.ArrowCursor))


def MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = interface.Ui_MainWindow()
        self.ui.setupUi(self)
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = LoginWindow()
    loginUi = login.Ui_LoginWindow()
    loginUi.setupUi(win)
    loginUi.widget_3.hide()
    def change_widget3():
        loginUi.widget_2.hide()
        loginUi.widget_3.show()
    def change_widget2():
        loginUi.widget_3.hide()
        loginUi.widget_2.show()

    loginUi.pushButton.clicked.connect(change_widget2)
    loginUi.pushButton_2.clicked.connect(change_widget3)
    win.show()
    sys.exit(app.exec_())
