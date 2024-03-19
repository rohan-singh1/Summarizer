import os
from pathlib import Path
from PySide6.QtWidgets import (
    QWidget, QApplication, QMainWindow
)
from PySide6.QtCore import QFile
from PySide6.QtUiTools import QUiLoader
from matplot import MatplotlibWidget
import numpy as np
import pandas as pd


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

    def visualize(self):
        # Create a MatplotlibWidget
        self.matplotlib_widget = MatplotlibWidget()

        # Visualization with dummy data
        # Bar chart plotting
        data = pd.read_csv('dummy_data.csv') 
        df = pd.DataFrame(data) 
        X = list(df.iloc[:, 0]) 
        Y = list(df.iloc[:, 1]) 

        # Boxplot plotting
        np.random.seed(10)
        box_data = np.random.normal(100, 20, 200)

        # Histogram
        hist_data = np.random.normal(loc=0, scale=1, size=1000)
        
        # Plotting
        self.matplotlib_widget.barlot(X, Y)
        self.matplotlib_widget.boxplot(box_data)
        self.matplotlib_widget.histogram(hist_data)
