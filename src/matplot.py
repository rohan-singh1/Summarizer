import matplotlib.pyplot as plt
from PySide6.QtWidgets import QWidget, QVBoxLayout
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas

class MatplotlibWidget(QWidget):
    def __init__(self, parent=None):
        super(MatplotlibWidget, self).__init__(parent)
        
        self.figure = plt.figure()
        self.canvas = FigureCanvas(self.figure)
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.canvas)
        self.setLayout(self.layout)
        
        self.ax = self.figure.add_subplot(111)

        self.setWindowTitle("Privacy Policy")
        self.setGeometry(100, 100, 800, 600)
        
    #Box plot
    def boxplot(self, x):
        self.ax.clear()
        self.ax.boxplot(x)
        self.canvas.draw()

    #bar plot
    def barlot(self, x,y):
        self.ax.clear()
        self.ax.bar(x,y)
        self.canvas.draw()

    #histogram
    def histogram(self,x):
        self.ax.clear()
        self.ax.hist(x)
        self.canvas.draw()
