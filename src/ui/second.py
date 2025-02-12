#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName:    second.py.py
# @Author:      周立兵
# @CreationTime:2025/2/12 20:48
# @Description: the script is used to do something.
import os

from PyQt6.QtGui import QIcon
from PyQt6.QtWidgets import QWidget, QLabel, QVBoxLayout, QPushButton, QHBoxLayout, QComboBox, QFrame, QFileIconProvider
from base_window import BaseWindow


# second.py
def format_file_size(size_bytes):
    for unit in ['B', 'KB', 'MB', 'GB', 'TB']:
        if size_bytes < 1024:
            return f"{size_bytes:.2f} {unit}"
        size_bytes /= 1024
    return f"{size_bytes:.2f} PB"


def populate_combo_box(combo_box, file_path):
    ext = os.path.splitext(file_path)[1].lower()
    if ext == '.txt':
        combo_box.addItems(["Text Option 1", "Text Option 2"])
    elif ext == '.pdf':
        combo_box.addItems(["PDF Option 1", "PDF Option 2"])
    elif ext == '.docx':
        combo_box.addItems(["Word Option 1", "Word Option 2"])
    elif ext == '.xlsx':
        combo_box.addItems(["Excel Option 1", "Excel Option 2"])
    else:
        combo_box.addItems(["暂未支持该类型"])


class SecondWindow(BaseWindow):

    def __init__(self, files):
        super().__init__()
        self.files = files
        self.init_ui()

    def init_ui(self):
        main_layout = QVBoxLayout()
        for file_path in self.files:
            item = self.add_file_item(file_path)
            main_layout.addLayout(item)

        bottom_layout = QHBoxLayout()
        # 文件选择按钮
        select_button = QPushButton("Select File", self)
        select_button.clicked.connect(self.select_file)
        bottom_layout.addWidget(select_button)

        hint_label = QLabel("使用Ctrl或Shift一次添加多个文件", self)
        bottom_layout.addWidget(hint_label)

        # 转换按钮
        convert_button = QPushButton("Convert", self)
        convert_button.clicked.connect(self.convert_file)
        bottom_layout.addWidget(convert_button)

        # 将结束布局添加到主布局
        main_layout.addLayout(bottom_layout)
        # 设置布局
        self.setLayout(main_layout)

        self.resize(400, 300)
        self.show()

    def delete_file(self, file_path):
        if file_path in self.files:
            self.files.remove(file_path)
            self.update_ui()

    def update_ui(self):
        # 清空当前布局并重新初始化 UI
        while self.layout().count():
            child = self.layout().takeAt(0)
            if child.widget():
                child.widget().deleteLater()
        self.init_ui()

    def add_file_item(self, file_path):
        file_name = os.path.basename(file_path)
        try:
            file_size = os.path.getsize(file_path)
        except FileNotFoundError:
            file_size = 0
        file_size_str = format_file_size(file_size)

        # 创建一个水平布局来放置按钮、下拉列表、删除按钮和文件大小标签
        item_layout = QHBoxLayout()

        item_layout.setContentsMargins(0, 0, 0, 0)
        item_layout.setSpacing(5)

        button = QPushButton(file_name, self)
        item_layout.addWidget(button)

        hint_label = QLabel("到", self)
        item_layout.addWidget(hint_label)

        combo_box = QComboBox(self)
        populate_combo_box(combo_box, file_path)
        item_layout.addWidget(combo_box)

        size_label = QLabel(f"Size: {file_size_str}", self)
        item_layout.addWidget(size_label)

        delete_button = QPushButton(QIcon.fromTheme("edit-delete"), "", self)
        delete_button.clicked.connect(lambda checked, fp=file_path: self.delete_file(fp))
        item_layout.addWidget(delete_button)

        return item_layout

    def convert_file(self):
        pass  # 你的转换逻辑