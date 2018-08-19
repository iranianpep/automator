import unittest
from collections import OrderedDict
from iautomate.resources.directory_resource import DirectoryResource
from iautomate.global_variables import GlobalVariables


class TestDirectoryResource(unittest.TestCase):
    def test_name(self):
        properties = OrderedDict([('name', '{$doc_root}'), ('action', 'create')])
        global_variables = GlobalVariables(OrderedDict([('doc_root', '/var/www/html')]))
        directory_resource = DirectoryResource(properties, global_variables)
        self.assertEquals('/var/www/html', directory_resource.name)

    def test_owner(self):
        properties = OrderedDict([('name', '{$doc_root}'), ('owner', 'www-data')])
        directory_resource = DirectoryResource(properties)
        self.assertEquals('www-data', directory_resource.owner)

    def test_group(self):
        properties = OrderedDict([('name', '{$doc_root}'), ('group', 'www-data')])
        directory_resource = DirectoryResource(properties)
        self.assertEquals('www-data', directory_resource.group)

    def test_mode(self):
        properties = OrderedDict([('name', '{$doc_root}'), ('mode', 644)])
        directory_resource = DirectoryResource(properties)
        self.assertEquals('644', directory_resource.mode)
