from PyQt6.QtGui import QColor, QIcon
from PyQt6.QtWidgets import QWidget, QFileDialog


# base_window.py

class BaseWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.init_base_ui()

    def init_base_ui(self):
        self.setWindowIcon(QIcon('../../assets/icon.png'))

        self.setWindowTitle('Xeris')

        palette = self.palette()
        palette.setColor(palette.ColorRole.Window, QColor("#ECF0F1"))
        self.setPalette(palette)

    def select_file(self) -> list[str]:
        files, _ = QFileDialog.getOpenFileNames(self)
        return files
