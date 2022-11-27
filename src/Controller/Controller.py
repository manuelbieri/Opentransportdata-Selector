import os.path
import datetime
import threading

from tkinter import StringVar
import DataSelector.driver


class Controller:
    def __init__(self):
        self.filters = []
        self.input_dir = StringVar()
        self.output_dir = StringVar()
        self.start_date = StringVar()
        self.end_date = StringVar()
        self.status = StringVar()
        self.setDefaultVars()

    def setDefaultVars(self):
        self.input_dir.set("/Users/manuelbieri/Downloads/ist-daten-2022-09")
        self.output_dir.set("/Users/manuelbieri/Downloads/output")
        self.start_date.set("9/1/22")
        self.end_date.set("9/2/22")
        self.status.set("No current process")

    def set_input_path(self, new_path: str):
        assert new_path is not None
        assert os.path.isdir(new_path)
        self.input_dir.set(new_path)

    def set_output_path(self, new_path: str):
        assert new_path is not None
        assert os.path.isdir(new_path)
        self.output_dir.set(new_path)

    def invoke_merge(self):
        th = threading.Thread(target=self.merge_files)
        th.start()

    def merge_files(self):
        self.status.set("merging...")
        driver = DataSelector.driver.Driver(
            self.output_dir.get(),
            self.input_dir.get()
        )
        driver.setFilters(
            [{'name': 'HALTESTELLEN_NAME', 'value': 'Bern'}, {'name': 'VERKEHRSMITTEL_TEXT', 'value': 'IC'}])
        path = driver.filterDateRange(
            datetime.datetime.strptime(self.start_date.get(), "%m/%d/%y"),
            datetime.datetime.strptime(self.end_date.get(), "%m/%d/%y"),
        )
        self.status.set("Written to: " + path)
