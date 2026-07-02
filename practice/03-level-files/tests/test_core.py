import sys
import os
import unittest

# 把 src/ 加入搜索路径（测试文件在 tests/，需要往回走一层）
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from package.add import add
from package.minus import minus
from package.core import calculate


class TestAdd(unittest.TestCase):
    """测试 add 模块"""

    def test_positive(self):
        self.assertEqual(add(2, 3), 5)

    def test_negative(self):
        self.assertEqual(add(-1, -1), -2)

    def test_zero(self):
        self.assertEqual(add(0, 5), 5)
        self.assertEqual(add(0, 0), 0)


class TestMinus(unittest.TestCase):
    """测试 minus 模块"""

    def test_positive_result(self):
        self.assertEqual(minus(5, 3), 2)

    def test_negative_result(self):
        self.assertEqual(minus(3, 5), -2)

    def test_zero(self):
        self.assertEqual(minus(5, 0), 5)


class TestCalculate(unittest.TestCase):
    """测试 core.calculate"""

    def test_returns_tuple(self):
        result = calculate(5, 3)
        self.assertIsInstance(result, tuple)
        self.assertEqual(len(result), 2)

    def test_correct_values(self):
        add_result, minus_result = calculate(10, 4)
        self.assertEqual(add_result, 14)
        self.assertEqual(minus_result, 6)


if __name__ == '__main__':
    unittest.main()
