#!/usr/bin/python
# -*- coding: utf-8 -*-

import unittest
from test_mathfunc import TestMathFunc

if __name__ == '__main__':
    suite = unittest.TestSuite()

    tests = [TestMathFunc("test_add"), TestMathFunc("test_minus"), TestMathFunc("test_divide")]
    suite.addTests(tests)
    with open("myfile.txt","rw+") as f:
        runner = unittest.TextTestRunner(stream=f ,verbosity=2)
        runner.run(suite)