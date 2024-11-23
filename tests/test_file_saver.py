import unittest
import os
from src.file_saver import JSONFileHandler  # Предполагая, что у вас есть этот класс


class TestJSONFileHandler(unittest.TestCase):
    def setUp(self):
        self.filename = "test_data.json"
        self.handler = JSONFileHandler(filename=self.filename)

    def tearDown(self):
        if os.path.exists(self.filename):
            os.remove(self.filename)

    def test_save_data(self):
        data = [{'title': 'Разработчик', 'salary': 60000}]
        self.handler.save_data(data)
        loaded_data = self.handler.load_data()
        self.assertEqual(loaded_data, data)

    def test_save_duplicate_data(self):
        data1 = [{'title': 'Разработчик', 'salary': 60000}]
        data2 = [{'title': 'Разработчик', 'salary': 70000}]  # Дубликат
        self.handler.save_data(data1)
        self.handler.save_data(data2)
        loaded_data = self.handler.load_data()
        self.assertEqual(len(loaded_data), 1)  # Проверка на уникальность

    def test_delete_data(self):
        data = [{'title': 'Разработчик', 'salary': 60000}]
        self.handler.save_data(data)
        self.handler.delete_data('Разработчик')
        loaded_data = self.handler.load_data()
        self.assertEqual(loaded_data, [])


if __name__ == '__main__':
    unittest.main()
