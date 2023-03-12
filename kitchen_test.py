import unittest
from unittest.mock import MagicMock

import kitchen


class TestKitchen(unittest.TestCase):
    def test_get_order(self):
        test_order = """3 столик: Карбонара, Ташкентский чай, Салат Оливье"""
        kitchen.Kitchen.parse_order = MagicMock(return_value=test_order)
        my_kitchen = kitchen.Kitchen({'Повар', 'Шеф', 'Нарезчик'})
        test_file = 'abcd'
        my_kitchen.get_order(test_file)

        with open(f'{test_file}.txt') as f:
            self.assertEqual(f.read(), test_order)