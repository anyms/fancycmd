# !/usr/bin/env python
# coding=utf-8

"""
Copyright (c) 2018 suyambu developers (http://codeinside.me/suyambu)
See the file 'LICENSE' for copying permission
"""


class Str(str):
    def red(self):
        return "\001\033[31m\002{}\001\033[0m\002".format(self)

    def green(self):
        return "\001\033[32m\002{}\001\033[0m\002".format(self)

    def yellow(self):
        return "\001\033[33m\002{}\001\033[0m\002".format(self)

    def blue(self):
        return "\001\033[34m\002{}\001\033[0m\002".format(self)
