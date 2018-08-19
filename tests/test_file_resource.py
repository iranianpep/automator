import unittest
from collections import OrderedDict
from iautomate.file_resource import FileResource


class TestFileResource(unittest.TestCase):
    def test_name(self):
        properties = OrderedDict([('name', '{$doc_root}/index.php'), ('action', 'install')])
        global_variables = OrderedDict([('doc_root', '/var/www/html')])
        file_resource = FileResource(properties, global_variables)
        self.assertEquals('/var/www/html/index.php', file_resource.name)
