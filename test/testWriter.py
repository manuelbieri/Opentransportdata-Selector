import os.path
import unittest
import DataSelector.writer
import DataSelector.loader


class TestFile(unittest.TestCase):
    def setUp(self) -> None:
        self.dir = 'output'
        self.writer = DataSelector.writer.Writer(self.dir)

    def tearDown(self) -> None:
        for f in os.listdir(self.dir):
            os.remove(os.path.join(self.dir, f))

    def test_invalidFile(self):
        self.assertRaises(AssertionError, lambda: DataSelector.writer.Writer(output_dir="uotput"))

    def test_emptyFile(self):
        self.assertRaises(AssertionError, lambda: DataSelector.writer.Writer(output_dir=None))

    def test_writeCSV(self):
        path = self.writer.write_csv([{'header1': 'value11', 'header2': 'value12', 'header3': 'value13'}, {'header1': 'value21', 'header2': '', 'header3': 'value23'}])
        self.loader = DataSelector.loader.File(path)
        self.loader.readCSV()
        self.assertEqual([{'header1': 'value11', 'header2': 'value12', 'header3': 'value13'}, {'header1': 'value21', 'header2': '', 'header3': 'value23'}], self.loader.getDictList())

    def test_writeJSON(self):
        path = self.writer.write_json([{'header1': 'value11', 'header2': 'value12', 'header3': 'value13'}, {'header1': 'value21', 'header2': '', 'header3': 'value23'}])
        self.loader = DataSelector.loader.File(path)
        self.loader.readJSON()
        self.assertEqual([{'header1': 'value11', 'header2': 'value12', 'header3': 'value13'}, {'header1': 'value21', 'header2': '', 'header3': 'value23'}], self.loader.getDictList())
