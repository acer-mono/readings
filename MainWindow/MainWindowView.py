from PyQt5.QtWidgets import QMainWindow
from MainWindow.MainWindowObserver import MainWindowObserver
from MainWindow.MainWindow import Ui_MainWindow
from MainWindow.MainWindowMeta import MainWindowMeta


class MainWindowView(QMainWindow, MainWindowObserver, metaclass=MainWindowMeta):
    """
    Класс отвечающий за визуальное представление CplusDModel.
    """

    def __init__(self, in_model, parent=None):
        """
        Конструктор принимает ссылки на модель и контроллер.
        """
        super(MainWindowView, self).__init__(parent)
        self.model = in_model

        # подключаем визуальное представление
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setStyleSheet(open('MainWindow/MainWindow.qss').read())

        # регистрируем представление в качестве наблюдателя
        self.model.add_observer(self)

        self.ui.currentDate.setText(self.model.date)

    def model_is_changed(self):
        self.ui.currentDate.setText(self.model.date)
