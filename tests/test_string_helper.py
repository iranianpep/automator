import unittest


from iautomate.string_helper import StringHelper


class TestStringHelper(unittest.TestCase):
    def test_replace_placeholder(self):
        helper = StringHelper.replace_placeholder('{$doc_root}/index.php', '{$doc_root}', '/var/www/html')
        self.assertEquals('/var/www/html/index.php', helper)

        helper = StringHelper.replace_placeholder('{doc_root}/index.php', '{$doc_root}', '/var/www/html')
        self.assertEquals('{doc_root}/index.php', helper)

        helper = StringHelper.replace_placeholder('doc_root/index.php', '{$doc_root}', '/var/www/html')
        self.assertEquals('doc_root/index.php', helper)
