import sys
import re

from application import App
from tkinter import messagebox
import subprocess


def get_jdk_version():
    try:
        process = subprocess.Popen(['java', '-version'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        error, output = process.communicate()
        # print('output', output.decode(sys.getdefaultencoding()))
        # print('error', error.decode(sys.getdefaultencoding()))
        if process.returncode == 0:
            version_line = output.decode().split('\n')[0]
            match = re.search(r'\".*\"', version_line)
            if match:
                jdk_version = match.group(0)
                return jdk_version[1:-1]
            else:
                sys.exit(-1)
        else:
            messagebox.showerror(title='错误', message='无JAVA环境，请确保正确安装JDK并设置好环境变量')
            sys.exit(-1)
    except Exception as e:
        print(str(e))
        sys.exit(-1)


if __name__ == '__main__':
    java_version = get_jdk_version()
    if java_version < '1.8':
        messagebox.showerror(title='错误', message='Java版本过低，请升级')
        sys.exit(-1)
    app = App('ChromHmm')


