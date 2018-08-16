import unittest
import os
from automator.automator import Automator
import copy


class TestAutomator(unittest.TestCase):
    def setUp(self):
        self.config_file = os.path.join(os.path.dirname(__file__), os.path.pardir, 'sample-config.json')
        self.automator = Automator(self.config_file)

    def test_config_file(self):
        self.assertEquals(self.automator.config_file, self.config_file)

        # check the setter directly too
        self.automator.config_file = self.config_file
        self.assertEquals(self.automator.config_file, self.config_file)

    def test_config_file_invalid_file(self):
        try:
            Automator('invalid-config')
        except IOError, e:
            self.assertEquals('Config file does not exist: invalid-config', e.message)

    def test_config(self):
        self.assertIsNotNone(self.automator.config)

    def test_config_empty_value(self):
        try:
            self.automator.config = ''
        except IOError, e:
            self.assertEquals('Config cannot be empty', e.message)

    def test_is_sudo_enabled(self):
        # keep the original config
        original_config = copy.deepcopy(self.automator.config)

        self.automator.config['vars']['sudo'] = False
        self.assertFalse(self.automator.is_sudo_enabled())

        self.assertTrue(self.automator.is_sudo_enabled(True))
        self.assertFalse(self.automator.is_sudo_enabled(False))
        self.assertFalse(self.automator.is_sudo_enabled(None))

        self.automator.config['vars']['sudo'] = True
        self.assertTrue(self.automator.is_sudo_enabled())

        self.assertTrue(self.automator.is_sudo_enabled(True))
        self.assertFalse(self.automator.is_sudo_enabled(False))
        self.assertTrue(self.automator.is_sudo_enabled(None))

        del self.automator.config['vars']['sudo']
        self.assertFalse(self.automator.is_sudo_enabled())

        self.assertTrue(self.automator.is_sudo_enabled(True))
        self.assertFalse(self.automator.is_sudo_enabled(False))
        self.assertFalse(self.automator.is_sudo_enabled(None))

        # revert all the changes back in the config
        self.automator.config = original_config
