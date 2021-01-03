# -*- coding: utf-8 -*-
# Intro: 目录引入模块单元测试
# Author: Ztj
# Email: ztj1993@gmail.com
# Date: 2020-01-03

import os
import unittest

from ZtjDirImport import DirImport

self_dir = os.path.dirname(os.path.abspath(__file__))
modules_dir = os.path.join(self_dir, 'modules')


class TestDirImport(unittest.TestCase):

    def test_init(self):
        obj = DirImport('modules', modules_dir)
        self.assertIsNotNone(obj.get('modules.a'))
        self.assertIsNotNone(obj.get('modules.b'))
        self.assertIsNotNone(obj.get('modules.c'))
        self.assertIsNotNone(obj.get('modules.d'))
        self.assertIsNone(obj.get('modules.e'))

    def test_disable(self):
        obj = DirImport('modules', modules_dir)
        obj.disable()
        self.assertIsNone(obj.get('modules.a'))
        self.assertIsNotNone(obj.get('modules.b'))

    def test_filter(self):
        obj = DirImport('modules', modules_dir)
        obj.filter('name')
        self.assertIsNotNone(obj.get('modules.a'))
        self.assertIsNone(obj.get('modules.d'))

    def test_enable(self):
        obj = DirImport('modules', modules_dir)
        obj.enable()
        self.assertIsNone(obj.get('modules.a'))
        self.assertIsNone(obj.get('modules.d'))


if __name__ == '__main__':
    unittest.main()
