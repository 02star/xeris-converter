#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName:    first.py
# @Author:      周立兵
# @CreationTime:2025/2/12 20:47
# @Description: the script is used to do something.
import sys

from PyQt6.QtGui import QIcon
from PyQt6.QtWidgets import QApplication, QPushButton, QVBoxLayout, QFileDialog

from base_window import BaseWindow
from second import SecondWindow


# first.py
class FirstWindow(BaseWindow):

    def __init__(self):
        super().__init__()
        self.second_window = None
        self.init_ui()

    def init_ui(self):
        btn = QPushButton('选择文件', self)
        btn.clicked.connect(self.open_file)
        layout = QVBoxLayout()

        layout.addWidget(btn)

        self.setLayout(layout)

        self.resize(300, 200)

    def open_file(self):
        files = self.select_file()
        if files:
            self.second_window = SecondWindow(files)
            self.second_window.show()
            self.close()


def main():
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon('../../icon.png'))
    first = FirstWindow()
    first.show()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()