from PyQt5 import QtWidgets  # import PyQt5 widgets
from MainWindow.MainWindowController import MainWindowController
from MainWindow.MainWindowModel import MainWindowModel
import sys

# Create the application object
app = QtWidgets.QApplication(sys.argv)

# Create the form object
model = MainWindowModel()

controller = MainWindowController(model)
#first_window.setStyleSheet(open('MainWindow/MainWindow.qss').read())

# Run the program
sys.exit(app.exec())
