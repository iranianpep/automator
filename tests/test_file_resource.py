import unittest
from collections import OrderedDict
from iautomate.resources.file_resource import FileResource
from iautomate.global_variables import GlobalVariables


class TestFileResource(unittest.TestCase):
    def test_name(self):
        properties = OrderedDict([('name', '{$doc_root}/index.php'), ('action', 'create')])
        global_variables = GlobalVariables(OrderedDict([('doc_root', '/var/www/html')]))
        file_resource = FileResource(properties, global_variables)
        self.assertEquals('/var/www/html/index.php', file_resource.name)

        properties = OrderedDict([('name', '/home/ubuntu/index.php'), ('action', 'create')])
        file_resource = FileResource(properties)
        self.assertEquals('/home/ubuntu/index.php', file_resource.name)

    def test_owner(self):
        properties = OrderedDict([('name', '{$doc_root}/index.php'), ('owner', 'www-data')])
        file_resource = FileResource(properties)
        self.assertEquals('www-data', file_resource.owner)

    def test_group(self):
        properties = OrderedDict([('name', '{$doc_root}/index.php'), ('group', 'www-data')])
        file_resource = FileResource(properties)
        self.assertEquals('www-data', file_resource.group)

    def test_mode(self):
        properties = OrderedDict([('name', '{$doc_root}/index.php'), ('mode', 644)])
        file_resource = FileResource(properties)
        self.assertEquals('644', file_resource.mode)

    def test_source(self):
        properties = OrderedDict([('name', '{$doc_root}/index.php'), ('source', '/var/www/index.php')])
        file_resource = FileResource(properties)
        self.assertEquals('/var/www/index.php', file_resource.source)
