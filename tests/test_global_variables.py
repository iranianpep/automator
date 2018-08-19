import unittest
from collections import OrderedDict
from iautomate.global_variables import GlobalVariables


class TestGlobalVariables(unittest.TestCase):
    def setUp(self):
        self.properties = OrderedDict([('sudo', True), ('debug', True), ('doc_root', '/var/www/html')])
        self.properties2 = OrderedDict([('sudo', False), ('debug', True), ('doc_root', '/var/www/html')])
        self.properties3 = OrderedDict([('sudo', True), ('debug', False)])
        self.properties4 = OrderedDict([('sudo', False), ('debug', False), ('doc_root', '/var/www/html')])
        self.properties5 = OrderedDict([('sudo', False), ('debug', False)])
        self.properties6 = OrderedDict([('sudo', True), ('debug', True)])
        self.properties7 = OrderedDict([('sudo', True)])
        self.properties8 = OrderedDict([('debug', True)])

    def test_is_debug_mode(self):
        global_variables = GlobalVariables(self.properties)
        self.assertTrue(global_variables.is_debug_mode())

        global_variables = GlobalVariables(self.properties2)
        self.assertTrue(global_variables.is_debug_mode())

        global_variables = GlobalVariables(self.properties3)
        self.assertFalse(global_variables.is_debug_mode())

        global_variables = GlobalVariables(self.properties7)
        self.assertFalse(global_variables.is_debug_mode())

    def test_sudo(self):
        global_variables = GlobalVariables(self.properties)
        self.assertTrue(global_variables.sudo)

        global_variables = GlobalVariables(self.properties2)
        self.assertFalse(global_variables.sudo)

        global_variables = GlobalVariables(self.properties8)
        self.assertIsNone(global_variables.sudo)

    def tes_debug(self):
        global_variables = GlobalVariables(self.properties)
        self.assertTrue(global_variables.debug)

        global_variables = GlobalVariables(self.properties3)
        self.assertFalse(global_variables.debug)

        global_variables = GlobalVariables(self.properties7)
        self.assertIsNone(global_variables.debug)

    def test_doc_root(self):
        global_variables = GlobalVariables(self.properties)
        self.assertEquals('/var/www/html', global_variables.doc_root)

        global_variables = GlobalVariables(self.properties3)
        self.assertIsNone(global_variables.doc_root)
