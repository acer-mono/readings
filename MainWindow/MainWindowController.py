from MainWindow.MainWindowView import MainWindowView


class MainWindowController:
    """
    Класс MainWindowController представляет реализацию контроллера.
    Согласовывает работу представления с моделью.
    """

    def __init__(self, in_model):
        """
        Конструктор принимает ссылку на модель.
        Конструктор создаёт и отображает представление.
        """
        self.model = in_model
        self.mView = MainWindowView(self.model)

        self.mView.show()
