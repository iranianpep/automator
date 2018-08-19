import unittest
from collections import OrderedDict
from iautomate.service_resource import ServiceResource


class TestServiceResource(unittest.TestCase):
    def test_name(self):
        properties = OrderedDict([('name', 'apache2'), ('ensure', 'running')])
        service_resource = ServiceResource(properties)
        self.assertEquals('running', service_resource.ensure)
