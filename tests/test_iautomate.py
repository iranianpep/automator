import unittest
import os
from iautomate.iautomate import IAutomate
import copy


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
            self.assertEquals('Config file does not exist: invalid-config', e.message)

    def test_config(self):
        self.assertIsNotNone(self.iautomate.config)

    def test_config_empty_value(self):
        try:
            self.iautomate.config = ''
        except OSError as e:
            self.assertEquals('Config cannot be empty', e.message)

    def test_is_sudo_enabled(self):
        # keep the original config
        original_config = copy.deepcopy(self.iautomate.config)

        self.iautomate.config['vars']['sudo'] = False
        self.assertFalse(self.iautomate.is_sudo_enabled())

        self.assertTrue(self.iautomate.is_sudo_enabled(True))
        self.assertFalse(self.iautomate.is_sudo_enabled(False))
        self.assertFalse(self.iautomate.is_sudo_enabled(None))

        self.iautomate.config['vars']['sudo'] = True
        self.assertTrue(self.iautomate.is_sudo_enabled())

        self.assertTrue(self.iautomate.is_sudo_enabled(True))
        self.assertFalse(self.iautomate.is_sudo_enabled(False))
        self.assertTrue(self.iautomate.is_sudo_enabled(None))

        del self.iautomate.config['vars']['sudo']
        self.assertFalse(self.iautomate.is_sudo_enabled())

        self.assertTrue(self.iautomate.is_sudo_enabled(True))
        self.assertFalse(self.iautomate.is_sudo_enabled(False))
        self.assertFalse(self.iautomate.is_sudo_enabled(None))

        # revert all the changes back in the config
        self.iautomate.config = original_config
