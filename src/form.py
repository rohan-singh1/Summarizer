import os
from pathlib import Path
from PySide6.QtWidgets import (
    QWidget,
)
from PySide6.QtCore import QFile
from PySide6.QtUiTools import QUiLoader


class MainWidget(QWidget):
    def __init__(self):
        super(MainWidget, self).__init__()
        MainWidget.win = self.load_ui()

    def load_ui(self):
        loader = QUiLoader()
        path = os.fspath(Path(__file__).resolve().parent / "../ui/form.ui")
        ui_file = QFile(path)
        ui_file.open(QFile.ReadOnly)
        win = loader.load(ui_file, self)
        ui_file.close()

        win.summarize_button.clicked.connect(self.handle_summarize_button_clicked)
        win.back_button.clicked.connect(self.handle_back_button_clicked)

        return win

    def handle_summarize_button_clicked(self):
        self.win.stacked_widget.setCurrentIndex(1)

    def handle_back_button_clicked(self):
        self.win.stacked_widget.setCurrentIndex(0)
