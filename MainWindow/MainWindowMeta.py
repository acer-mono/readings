from PyQt5 import QtCore
from abc import ABCMeta


class MainWindowMeta(type(QtCore.QObject), ABCMeta): pass
