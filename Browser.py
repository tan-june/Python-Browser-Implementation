import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import QWebEngineView  

class Browser(QMainWindow):
    def __init__(self):
        super().__init__()

        self.browser = QWebEngineView()
        self.browser.setUrl(QUrl("http://www.google.com"))

        navbar = QToolBar()
        self.addToolBar(navbar)

        back_btn = QAction(QIcon('icons/left.png'), 'Go Back', self)
        back_btn.triggered.connect(self.browser.back)
        navbar.addAction(back_btn)

        forward_btn =QAction(QIcon('icons/right.png'), 'Go Right', self)
        forward_btn.triggered.connect(self.browser.forward)
        navbar.addAction(forward_btn)

        reload_btn = QAction(QIcon('icons/reload.png'), 'Reload', self)
        reload_btn.triggered.connect(self.browser.reload)
        navbar.addAction(reload_btn)

        home_btn = QAction(QIcon('icons/home.png'), 'Home', self)
        home_btn.triggered.connect(self.navigate_home)
        navbar.addAction(home_btn)

        self.url_bar = QLineEdit()
        self.url_bar.returnPressed.connect(self.navigate_to_url)
        navbar.addWidget(self.url_bar)

        exit = QAction(QIcon('icons/close.png'), 'Close', self)
        exit.triggered.connect(self.close)
        navbar.addAction(exit)
        
        self.setCentralWidget(self.browser)

        self.showFullScreen()

    def close(self):
        exit()

    def navigate_home(self):
        self.browser.setUrl(QUrl("http://www.google.com"))

    def navigate_to_url(self):
        q = QUrl(self.url_bar.text())
        if q.scheme() == "":
            q.setScheme("http")

        self.browser.setUrl(q)

app = QApplication(sys.argv)
QApplication.setApplicationName("Tanmay's Browser")

app_icon = QIcon('icons/icon.png')
app.setWindowIcon(app_icon)

window = Browser()
app.exec_()
