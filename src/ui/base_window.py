#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName:    base_window.py
# @Author:      周立兵
# @CreationTime:2025/2/18 20:53
# @Description: the script is used to do something.
from PyQt6.QtGui import QIcon
from PyQt6.QtWidgets import QMainWindow


class BaseWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('Xeris')
        self.setWindowIcon(QIcon('../../icon.png'))