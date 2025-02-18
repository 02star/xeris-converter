#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName:    main.py
# @Author:      周立兵
# @CreationTime:2025/2/18 20:40
# @Description: the script is used to do something.
import sys

from PyQt6.QtGui import QIcon
from PyQt6.QtWidgets import QApplication, QFileDialog, QWidget

from customWidgets.card import CardWidget
from src.ui.base_window import BaseWindow
from src.ui.flow_layout import FlowLayout


# first.py
class MainWindow(BaseWindow):

    def __init__(self):
        super().__init__()
        self.second_window = None
        self.init_ui()

    def init_ui(self):
        container = QWidget()
        layout = FlowLayout(container)

        card = CardWidget(['../../assets/pdf.png','../../assets/arrow.png','../../assets/word.png'],'PDF转WORD')
        card.clicked.connect(self.select_file)
        layout.addWidget(card)

        self.setCentralWidget(container)
        self.resize(300, 200)


    def select_file(self):
        file_path, _ = QFileDialog.getOpenFileName(
            self,
            "选择PDF文件",
            "",
            "PDF Files (*.pdf)"
        )
        if file_path:
            pass



def main():
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon('../../assets/icon.png'))
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()