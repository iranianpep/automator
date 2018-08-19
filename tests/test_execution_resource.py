import unittest
import mock
from collections import OrderedDict
from iautomate.execution_resource import ExecutionResource


class TestExecutionResource(unittest.TestCase):
    @mock.patch('subprocess.Popen')
    def test_name(self, mock_subproc_popen):
        properties = OrderedDict([('name', 'pwd'), ('action', 'pwd')])
        execution_resource = ExecutionResource(properties)

        process_mock = mock.Mock()
        attrs = {'communicate.return_value': ('/to/dummy/dir', 'error')}
        process_mock.configure_mock(**attrs)
        mock_subproc_popen.return_value = process_mock

        execution_resource.run()

        self.assertTrue(mock_subproc_popen.called)
