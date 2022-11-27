import DataSelectorTest.testAbstract
import unittest.mock

import DataSelector.parser
import DataSelector.loader
import DataSelector.driver


class TestFile(DataSelectorTest.testAbstract.AbstractTest):
    def setUp(self) -> None:
        self.driver = DataSelector.driver.Driver(TestFile.output_path, TestFile.input_path)
        self.file = unittest.mock.Mock()
        self.file.getDictList = unittest.mock.Mock(return_value=[{'header1': 'value11', 'header2': 'value12', 'header3': 'value13'}, {'header1': 'value21', 'header2': '', 'header3': 'value23'}])
        self.file1 = unittest.mock.Mock()
        self.file1.getDictList = unittest.mock.Mock(return_value=[{'header1': 'value31', 'header2': 'value32', 'header3': 'value33'}, {'header1': 'value41', 'header2': 'value42', 'header3': 'value43'}])

    def test_setUpWithInvalidPaths(self):
        self.assertRaises(AssertionError, lambda: DataSelector.driver.Driver('invalidOutput', 'invalidResources'))

    def test_filterDateWithoutArguments(self):
        self.assertEqual([{'header1': 'value11', 'header2': 'value12', 'header3': 'value13'}, {'header1': 'value21', 'header2': '', 'header3': 'value23'}], self.driver.filterDate(self.file))

    def test_filterDateWithArguments(self):
        self.driver.setFilters([{'name': 'header1', 'value': 'value11'}])
        self.assertEqual([{'header1': 'value11', 'header2': 'value12', 'header3': 'value13'}], self.driver.filterDate(self.file))

    def test_filterDateRangeWithoutFilter(self):
        return_values = {
            '2021-01-01_istdaten.csv': self.file,
            '2021-01-02_istdaten.csv': self.file1
        }
        self.driver.loadFile = unittest.mock.MagicMock()
        self.driver.loadFile.side_effect = return_values.get

        self.driver.filterDateRange(DataSelector.driver.Driver.convertStringToDate('2021-01-01'), DataSelector.driver.Driver.convertStringToDate('2021-01-02'))
        self.assertEqual([{'header1': 'value11', 'header2': 'value12', 'header3': 'value13'}, {'header1': 'value21', 'header2': '', 'header3': 'value23'},{'header1': 'value31', 'header2': 'value32', 'header3': 'value33'}, {'header1': 'value41', 'header2': 'value42', 'header3': 'value43'}], self.driver.getFiltered())

    def test_filterDateRangeWithFilter(self):
        return_values = {
            '2021-01-01_istdaten.csv': self.file,
            '2021-01-02_istdaten.csv': self.file1
        }
        self.driver.loadFile = unittest.mock.MagicMock()
        self.driver.loadFile.side_effect = return_values.get
        self.driver.setFilters([{'name': 'header1', 'value': 'value11'}])

        self.driver.filterDateRange(DataSelector.driver.Driver.convertStringToDate('2021-01-01'), DataSelector.driver.Driver.convertStringToDate('2021-01-02'))
        self.assertEqual([{'header1': 'value11', 'header2': 'value12', 'header3': 'value13'}], self.driver.getFiltered())
