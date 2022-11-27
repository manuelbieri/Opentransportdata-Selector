import tkinter
import tkinter.filedialog
from tkinter import *
from tkinter.ttk import *
from tkcalendar import DateEntry

import Controller.Controller as Controller


class CustomDateEntry(DateEntry):
    def __init__(self, frame: tkinter.Frame, **kwargs):
        super(CustomDateEntry, self).__init__(frame, **kwargs)
        self.bind("<1>", lambda e: self.drop_down())


class MainWindow(Tk):
    def __init__(self):
        super().__init__()
        self.title("Open Transport Data Selector")
        self.controller = Controller.Controller()
        self.mainframe = Frame(self)
        self.set_up_widgets()
        self.set_up_window()

    def set_up_window(self):
        self.resizable(False, False)

    def set_up_widgets(self):
        self.mainframe.pack()
        self._path_widget(is_input_path=True)
        self._path_widget(is_input_path=False)
        self._date_inputs()
        self._status_label()

    def _status_label(self):
        frame = Frame(self.mainframe)
        frame.pack(side=LEFT)
        Label(frame, textvariable=self.controller.status).pack(side=LEFT)

    def _date_inputs(self):
        frame = Frame(self.mainframe)
        frame.pack(fill='x')
        CustomDateEntry(
            frame,
            year=2022,
            month=9,
            day=1,
            textvariable=self.controller.start_date
        ).pack(side=LEFT, expand=True, fill='x')
        CustomDateEntry(
            frame,
            year=2022,
            month=9,
            day=2,
            textvariable=self.controller.end_date
        ).pack(side=LEFT, expand=True, fill='x')
        Button(frame, text="Merge", command=self.invoke_merge)\
            .pack(side=LEFT, expand=True, fill='x')

    def _path_widget(self, is_input_path=True):
        path_var = self.controller.input_dir if is_input_path else self.controller.output_dir
        frame = Frame(self.mainframe)
        frame.pack()
        Entry(frame, textvariable=path_var, width=40) \
            .pack(side=LEFT)
        Button(frame, text="...", command=lambda: self.open_file_dialog(is_input_path), width=1) \
            .pack(side=LEFT)

    def invoke_merge(self):
        self.controller.invoke_merge()

    def open_file_dialog(self, input=True):
        assert input is not None
        path: str = tkinter.filedialog.askdirectory(mustexist=True)
        if input:
            self.controller.set_input_path(path)
        else:
            self.controller.set_output_path(path)


if __name__ == "__main__":
    root = MainWindow()
    root.mainloop()
