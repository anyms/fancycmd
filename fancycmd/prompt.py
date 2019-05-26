# !/usr/bin/env python
# coding=utf-8

"""
Copyright (c) 2018 suyambu developers (http://codeinside.me/suyambu)
See the file 'LICENSE' for copying permission
"""

from .data_types import Str


class Prompt:
    def __init__(self):
        self.s = []

    def add(self, s, color="default"):
        if color == "default":
            self.s.append(s)
        else:
            o = Str(s)
            methods = dir(o.__class__)
            if color in methods:
                func = getattr(o, color)
                self.s.append(func())

        return self

    def get(self):
        return "".join(self.s)
