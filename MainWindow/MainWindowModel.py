import datetime
from apscheduler.schedulers.background import BackgroundScheduler


class MainWindowModel:
    def __init__(self):
        self.dateTime = ""
        self.observers = []
        self.update_date()
        self.scheduler = BackgroundScheduler()
        self.scheduler.add_job(self.update_date, 'interval', seconds=1)
        self.scheduler.start()

    @property
    def date(self):
        return self.dateTime

    def update_date(self):
        self.dateTime = 'Сегодня: {}'.format(datetime.datetime.today().strftime("%d.%m.%Y %H:%M:%S"))
        self.notify_observers()

    def add_observer(self, in_observer):
        self.observers.append(in_observer)

    def remove_observer(self, in_observer):
        self.observers.remove(in_observer)

    def notify_observers(self):
        for observer in self.observers:
            observer.model_is_changed()
