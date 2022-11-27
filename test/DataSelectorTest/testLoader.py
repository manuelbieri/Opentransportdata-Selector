import DataSelectorTest.testAbstract

import DataSelector.loader


class TestFile(DataSelectorTest.testAbstract.AbstractTest):
    def setUp(self) -> None:
        self.file = DataSelector.loader.File(path=TestFile.input_path + "/testFile.csv")
        self.file.readCSV()

    def test_load(self):
        self.assertEqual('header1;header2;header3\nvalue11;value12;value13\nvalue21;;value23', self.file.getRaw())

    def test_loadJSON(self):
        self.file = DataSelector.loader.File(path=TestFile.input_path + "/testFile.json")
        self.file.readJSON()
        self.assertEqual([{'header1': 'value11', 'header2': 'value12', 'header3': 'value13'},
                          {'header1': 'value21', 'header2': '', 'header3': 'value23'}], self.file.getDictList())

    def test_read(self):
        self.assertEqual([{'header1': 'value11', 'header2': 'value12', 'header3': 'value13'},
                          {'header1': 'value21', 'header2': '', 'header3': 'value23'}], self.file.getDictList())

    def test_invalidFile(self):
        self.assertRaises(AssertionError, lambda: DataSelector.loader.File(path="resources/invalidFile.csv"))

    def test_invalidDelimiter(self):
        self.assertRaises(AssertionError, lambda: DataSelector.loader.File(path="resources/testFile.csv", delimiter=None))

    def test_emptyFile(self):
        test_file = DataSelector.loader.File(path=TestFile.input_path + "/emptyFile.csv")
        self.assertRaises(AssertionError, test_file.getRaw)
        self.assertRaises(AssertionError, test_file.getDictList)
