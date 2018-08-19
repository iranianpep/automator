import unittest
from collections import OrderedDict
from iautomate.resources.package_resource import PackageResource


class TestPackageResource(unittest.TestCase):
    def test_name(self):
        properties = OrderedDict([('name', 'apache2'), ('version', 'latest')])
        package_resource = PackageResource(properties)
        self.assertEquals('latest', package_resource.version)
