import os.path
import datetime

import DataSelector.loader
import DataSelector.parser
import DataSelector.writer


class Driver:
    def __init__(self, output_dir: str, data_path: str) -> None:
        assert output_dir is not None
        assert data_path is not None
        assert os.path.isdir(output_dir), "No valid output path specified"
        assert os.path.isdir(data_path), "No valid data input path specified"

        self.output_path = output_dir
        self.data_path = data_path
        self.filtered = []
        self.filter = []
        self.writer = DataSelector.writer.Writer(self.output_path)

    def filterDateRange(self, start_date: datetime, end_date: datetime) -> str:
        assert start_date is not None
        assert end_date is not None
        assert start_date <= end_date

        while start_date <= end_date:
            filename = start_date.strftime("%Y-%m-%d") + '_istdaten.csv'
            file = self.loadFile(filename)
            self.filtered.extend(self.filterDate(file))
            start_date += datetime.timedelta(days=1)

        return self.writer.write_csv(self.filtered)

    def loadFile(self, filename: str) -> DataSelector.loader.File:
        assert filename is not None
        return DataSelector.loader.File(self.data_path + '/' + filename)

    def filterDate(self, file: DataSelector.loader.File) -> list:
        file.readCSV()
        if self.filter:
            parser = DataSelector.parser.Selector(file)
            filtered_result = parser.filter(self.filter)
        else:
            filtered_result = file.getDictList()
        return filtered_result

    def getFiltered(self) -> list:
        assert len(self.filtered) > 0
        return self.filtered

    def setFilters(self, filter_args: list) -> None:
        assert len(filter_args) > 0
        self.filter = filter_args

    @staticmethod
    def convertStringToDate(input_date: str, date_format="%Y-%m-%d") -> datetime:
        assert len(date_format) == 8
        assert input_date is not None
        return datetime.datetime.strptime(input_date, date_format)


if __name__ == '__main__':
    selector = Driver('output', 'data')
    selector.setFilters([{'name': 'HALTESTELLEN_NAME', 'value': 'Bern'}, {'name': 'VERKEHRSMITTEL_TEXT', 'value': 'IC'}])
    selector.filterDateRange(Driver.convertStringToDate('2021-01-01'), Driver.convertStringToDate('2021-01-3'))
