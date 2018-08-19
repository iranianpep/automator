import unittest
from collections import OrderedDict

from iautomate.package_resource import PackageResource


class TestAbstractResource(unittest.TestCase):
    def setUp(self):
        self.properties = OrderedDict([('name', 'apache2'), ('action', 'install'), ('after_tasks', 'dummy')])
        self.properties_with_sudo_true = OrderedDict([('name', 'apache2'), ('action', 'install'), ('sudo', True)])
        self.properties_with_sudo_false = OrderedDict([('name', 'apache2'), ('action', 'install'), ('sudo', False)])
        self.global_variables_sudo_true = OrderedDict([('sudo', True), ('debug', True)])
        self.global_variables_sudo_false = OrderedDict([('sudo', False), ('debug', False)])

    def test_properties(self):
        package = PackageResource(self.properties)
        self.assertEquals(package.properties, self.properties)

    def test_name(self):
        package = PackageResource(self.properties)
        self.assertEquals(package.name, 'apache2')

    def test_action(self):
        package = PackageResource(self.properties)
        self.assertEquals(package.action, 'install')

    def test_after_tasks(self):
        package = PackageResource(self.properties)
        self.assertEquals(package.after_tasks, 'dummy')

    def test_sudo(self):
        package = PackageResource(self.properties)
        self.assertEquals(package.sudo, None)

        package = PackageResource(self.properties_with_sudo_true)
        self.assertEquals(package.sudo, True)

    def test_global_variables(self):
        package = PackageResource(self.properties)
        self.assertEquals(package.global_variables, None)

        package = PackageResource(self.properties, self.global_variables_sudo_true)
        self.assertEquals(package.global_variables, self.global_variables_sudo_true)

    def test_is_sudo_enabled(self):
        package = PackageResource(self.properties)
        self.assertFalse(package.is_sudo_enabled())

        package = PackageResource(self.properties_with_sudo_true)
        self.assertTrue(package.is_sudo_enabled())

        package = PackageResource(self.properties_with_sudo_false)
        self.assertFalse(package.is_sudo_enabled())

        package = PackageResource(self.properties, self.global_variables_sudo_true)
        self.assertTrue(package.is_sudo_enabled())

        package = PackageResource(self.properties_with_sudo_true, self.global_variables_sudo_true)
        self.assertTrue(package.is_sudo_enabled())

        package = PackageResource(self.properties_with_sudo_false, self.global_variables_sudo_true)
        self.assertFalse(package.is_sudo_enabled())

        package = PackageResource(self.properties_with_sudo_true, self.global_variables_sudo_false)
        self.assertTrue(package.is_sudo_enabled())

        package = PackageResource(self.properties_with_sudo_false, self.global_variables_sudo_false)
        self.assertFalse(package.is_sudo_enabled())

    def test_is_debug_mode(self):
        package = PackageResource(self.properties)
        self.assertFalse(package.is_debug_mode())

        package = PackageResource(self.properties, self.global_variables_sudo_true)
        self.assertTrue(package.is_debug_mode())

        package = PackageResource(self.properties, self.global_variables_sudo_false)
        self.assertFalse(package.is_debug_mode())
