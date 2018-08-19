import unittest
import mock


from iautomate.package_helper import PackageHelper
from iautomate.shell_helper import ShellHelper


class TestShellHelper(unittest.TestCase):
    @mock.patch('subprocess.Popen')
    def test_run_command(self, mock_subproc_popen):
        process_mock = mock.Mock()

        # mock ShellHelper.run_command function and returned installed
        attrs = {'communicate.return_value': ('installed', 'error')}
        process_mock.configure_mock(**attrs)
        mock_subproc_popen.return_value = process_mock

        helper = PackageHelper()
        helper.is_package_installed('apache2')

        self.assertTrue(helper.is_package_installed('apache2'))
        self.assertTrue(mock_subproc_popen.called)

        # mock ShellHelper.run_command function and returned None
        attrs = {'communicate.return_value': (None, 'error')}
        process_mock.configure_mock(**attrs)
        mock_subproc_popen.return_value = process_mock

        helper.is_package_installed('apache2')

        self.assertFalse(helper.is_package_installed('apache2'))
        self.assertTrue(mock_subproc_popen.called)
