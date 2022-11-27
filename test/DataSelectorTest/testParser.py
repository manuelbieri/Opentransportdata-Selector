import unittest
from unittest.mock import Mock
import DataSelector.parser
import DataSelector.loader


class TestFile(unittest.TestCase):
    def setUp(self) -> None:
        self.mock = Mock()
        self.mock.getDictList = Mock(return_value=[{'header1': 'value11', 'header2': 'value12', 'header3': 'value13'}, {'header1': 'value21', 'header2': '', 'header3': 'value23'}])
        self.parser = DataSelector.parser.Selector(self.mock)

    def test_filter(self):
        self.assertEqual([{'header1': 'value11', 'header2': 'value12', 'header3': 'value13'}], self.parser.filter([{'name': 'header1', 'value': 'value11'}]))

    def test_filterWithEmptyResult(self):
        self.assertEqual([], self.parser.filter([{'name': 'header1', 'value': 'value44'}]))

    def test_filterWithEmptyFilter(self):
        self.assertRaises(AssertionError, lambda: self.parser.filter([]))

    def test_filterWithIllegalFilter(self):
        self.assertRaises(KeyError, lambda: self.parser.filter([{'flawedName': 'header1', 'flawedValue': 'value44'}]))
