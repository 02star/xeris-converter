import ttkbootstrap as ttk
from ttkbootstrap.constants import *


class ModernApp(ttk.Window):
    def __init__(self):
        super().__init__(themename="morph")

        # 界面布局
        self.title("现代风格OCR工具")
        self.geometry("800x600")

        # 顶部工具栏
        toolbar = ttk.Frame(self, bootstyle=PRIMARY)
        toolbar.pack(fill=X, padx=5, pady=5)

        ttk.Button(toolbar, text="打开文件", command=self.open_files,
                   bootstyle=(OUTLINE, SUCCESS)).pack(side=LEFT, padx=2)
        ttk.Button(toolbar, text="开始转换", command=self.start_process,
                   bootstyle=(OUTLINE, INFO)).pack(side=LEFT, padx=2)

        # 文件列表
        self.file_list = ttk.Treeview(
            self,
            columns=("status",),
            show="headings",
            bootstyle=INFO
        )
        self.file_list.heading("#0", text="文件路径")
        self.file_list.heading("status", text="状态")
        self.file_list.pack(fill=BOTH, expand=True, padx=10, pady=10)

        # 进度条
        self.progress = ttk.Progressbar(
            self,
            orient=HORIZONTAL,
            mode="determinate",
            bootstyle=(SUCCESS, STRIPED)
        )
        self.progress.pack(fill=X, padx=10, pady=5)

    def open_files(self):
        # 文件选择逻辑
        pass

    def start_process(self):
        # 处理逻辑
        pass


if __name__ == "__main__":
    app = ModernApp()
    app.mainloop()