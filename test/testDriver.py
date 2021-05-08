import unittest
from unittest.mock import Mock
import DataSelector.parser
import DataSelector.loader
import DataSelector.driver


class TestFile(unittest.TestCase):
    def setUp(self) -> None:
        self.driver = DataSelector.driver.Driver()
