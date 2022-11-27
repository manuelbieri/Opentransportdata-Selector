from tkinter import StringVar


class Observer:
    def __init__(self):
        self.status = ""

    def set_status(self, value: str):
        self.status = value


class Observable:
    def __init__(self):
        self.observers = []
        self.value = ""

    def subscribe(self, obs: Observer):
        self.observers.append(obs)

    def notify(self):
        for observer in self.observers:
            observer.set_status(self.value)

    @property
    def status(self) -> str:
        return self.value

    @status.setter
    def status(self, value: str) -> None:
        self.value = value
        self.notify()


if __name__ == "__main__":
    observer = Observer()
    observable = Observable()
    observable.subscribe(observer)
    print(observer.status)
    observable.value = "test"
    print(observer.status)