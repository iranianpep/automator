from shell_helper import ShellHelper


class PackageHelper(object):
    # run the shell command and print the output if is in debug mode
    @staticmethod
    def is_package_installed(package_name):
        result = ShellHelper.run_command("dpkg-query --show --showformat='${db:Status-Status}' " + package_name)
        if result == 'installed':
            return True
        else:
            return False