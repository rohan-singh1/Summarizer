import sys
from form import MainWidget
from PySide6.QtWidgets import QApplication
from PySide6.QtCore import QSize

WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600

if __name__ == "__main__":
    app = QApplication([])
    widget = MainWidget()
    widget.setWindowTitle("Compare")
    widget.setFixedSize(QSize(WINDOW_WIDTH, WINDOW_HEIGHT))
    widget.show()
    sys.exit(app.exec())
