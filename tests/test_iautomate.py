import unittest
import os
from iautomate.iautomate import IAutomate


class TestAutomator(unittest.TestCase):
    def setUp(self):
        self.config_file = os.path.join(os.path.dirname(__file__), os.path.pardir, 'sample-config.json')
        self.iautomate = IAutomate(self.config_file)

    def test_config_file(self):
        self.assertEquals(self.iautomate.config_file, self.config_file)

        # check the setter directly too
        self.iautomate.config_file = self.config_file
        self.assertEquals(self.iautomate.config_file, self.config_file)

    def test_config_file_invalid_file(self):
        try:
            IAutomate('invalid-config')
        except OSError as e:
            self.assertEquals('Config file does not exist: invalid-config', str(e))

    def test_config(self):
        self.assertIsNotNone(self.iautomate.config)

    def test_config_empty_value(self):
        try:
            self.iautomate.config = ''
        except OSError as e:
            self.assertEquals('Config cannot be empty', str(e))
