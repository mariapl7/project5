import unittest
import os
from src.utils import load_json_file, save_json_file, is_duplicate


class TestUtils(unittest.TestCase):
    def setUp(self):
        self.filename = "test_data.json"
        self.test_data = [{'title': 'Разработчик'}, {'title': 'Дизайнер'}]
        save_json_file(self.filename, self.test_data)

    def tearDown(self):
        if os.path.exists(self.filename):
            os.remove(self.filename)

    def test_load_json_file(self):
        data = load_json_file(self.filename)
        self.assertEqual(data, self.test_data)

    def test_load_non_existent_file(self):
        data = load_json_file("non_existent_file.json")
        self.assertEqual(data, [])

    def test_is_duplicate(self):
        self.assertTrue(is_duplicate(self.test_data, 'Разработчик'))
        self.assertFalse(is_duplicate(self.test_data, 'Менеджер'))


if __name__ == '__main__':
    unittest.main()
