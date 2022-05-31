# unittest

unittest case的运行流程：

- 写好一个完整的TestCase
- 多个TestCase 由TestLoder被加载到TestSuite里面, TestSuite也可以嵌套TestSuite
- 由TextTestRunner来执行TestSuite，测试的结果保存在TextTestResult中
- TestFixture指的是环境准备和恢复

**unittest中最核心的部分是：TestFixture、TestCase、TestSuite、TestRunner**



## 函数

用于测试环境的准备和恢复还原, 一般用到下面几个函数。

- setUp()：准备环境，执行每个测试用例的前置条件
- tearDown()：环境还原，执行每个测试用例的后置条件
- setUpClass()：必须使用@classmethod装饰器，所有case执行的前置条件，只运行一次
- tearDownClass()：必须使用@classmethod装饰器，所有case运行完后只运行一次

```
#!/usr/bin/python
# -*- coding: utf-8 -*-

def add(a, b):
    return a+b

def minus(a, b):
    return a-b

```

```
#!/usr/bin/python
# -*- coding: utf-8 -*-

import unittest
from demo import add, minus


class TestDemo(unittest.TestCase):
    """Test mathfuc.py"""

    @classmethod
    def setUpClass(cls):
        print ("this setupclass() method only called once.\n")

    @classmethod #修饰这是一个类方法，可以不用实例化，可以通过TestDemo.setUpClass()调用
    def tearDownClass(cls):
        print ("this teardownclass() method only called once too.\n")

    def setUp(self):
        print ("do something before test : prepare environment.\n")

    def tearDown(self):
        print ("do something after test : clean up.\n")

    def test_add(self):
        """Test method add(a, b)"""
        self.assertEqual(3, add(1, 2))
        self.assertNotEqual(3, add(2, 2))

    def test_minus(self):
        """Test method minus(a, b)"""
        self.assertEqual(1, minus(3, 2))
        self.assertNotEqual(1, minus(3, 2))

    @unittest.skip("do't run as not ready")
    def test_minus_with_skip(self):
        """Test method minus(a, b)"""
        self.assertEqual(1, minus(3, 2))
        self.assertNotEqual(1, minus(3, 2))


if __name__ == '__main__':
    # verbosity=*：默认是1；设为0，则不输出每一个用例的执行结果；2-输出详细的执行结果
    unittest.main(verbosity=1)
```



## 示例

mathfunc.py

```
def add(a, b):
    return a+b

def minus(a, b):
    return a-b

def multi(a, b):
    return a*b

def divide(a, b):
    return a/b
```

测试脚本：

```
# -*- coding: utf-8 -*-

import unittest
from mathfunc import *


class TestMathFunc(unittest.TestCase):
    """Test mathfuc.py"""

    def test_add(self):
        """Test method add(a, b)"""
        self.assertEqual(3, add(1, 2))
        self.assertNotEqual(3, add(2, 2))

    def test_minus(self):
        """Test method minus(a, b)"""
        self.assertEqual(1, minus(3, 2))

    def test_multi(self):
        """Test method multi(a, b)"""
        self.assertEqual(6, multi(2, 3))

    def test_divide(self):
        """Test method divide(a, b)"""
        self.assertEqual(2, divide(6, 3))
        self.assertEqual(2.5, divide(5, 2))

if __name__ == '__main__':
    unittest.main(verbosity=1)
```

测试结果

```
.F..
======================================================================
FAIL: test_divide (__main__.TestMathFunc)
Test method divide(a, b)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "D:/py/test_mathfunc.py", line 26, in test_divide
    self.assertEqual(2.5, divide(5, 2))
AssertionError: 2.5 != 2

----------------------------------------------------------------------
Ran 4 tests in 0.000s

FAILED (failures=1)
```

能够看到一共运行了4个测试，失败了1个，并且给出了失败原因，`2.5 != 2` 也就是说我们的divide方法是有问题的。

这就是一个简单的测试，有几点需要说明的：

1、在第一行给出了每一个用例执行的结果的标识，成功是 .，失败是 F，出错是 E，跳过是 S。从上面也可以看出，测试的执行跟方法的顺序没有关系，test_divide写在了第4个，但是却是第2个执行的。

2、**每个测试方法均以 test 开头，否则是不被unittest识别的**。

3、在unittest.main()中加 verbosity 参数可以控制输出的错误报告的详细程度，默认是 1，如果设为 0，则不输出每一用例的执行结果，即没有上面的结果中的第1行；如果设为 2，则输出详细的执行结果



## testcase顺序执行

新建testcase，在将testcase加到testsuite之后再run

在文件夹中我们再新建一个文件，**test_suite.py**：

```
# -*- coding: utf-8 -*-

import unittest
from test_mathfunc import TestMathFunc

if __name__ == '__main__':
    suite = unittest.TestSuite()

    tests = [TestMathFunc("test_add"), TestMathFunc("test_minus"), TestMathFunc("test_divide")]
    suite.addTests(tests)#将case加到suite里

    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)
```



## 跳过某个testcase

```
...

class TestMathFunc(unittest.TestCase):
    """Test mathfuc.py"""

    ...

    @unittest.skip("I don't want to run this case.")
    def test_divide(self):
        """Test method divide(a, b)"""
        print "divide"
        self.assertEqual(2, divide(6, 3))
        self.assertEqual(2.5, divide(5, 2))
```

skip装饰器一共有三个

```
unittest.skip(reason)
unittest.skipIf(condition, reason)
unittest.skipUnless(condition, reason)
skip无条件跳过，skipIf当condition为True时跳过，skipUnless当condition为False时跳过。
```





## 输出测试结果

### 输出到文本里

````
if __name__ == '__main__':
    suite = unittest.TestSuite()

    tests = [TestMathFunc("test_add"), TestMathFunc("test_minus"), TestMathFunc("test_divide")]
    suite.addTests(tests)
    with open("myfile.txt","rw+") as f:
        runner = unittest.TextTestRunner(stream=f ,verbosity=2)
        runner.run(suite)
````



### 输出到html

```

```









