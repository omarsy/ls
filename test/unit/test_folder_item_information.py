import unittest
from unittest import mock
from src.folder_item_information import creation_date, mode, item_name


class TestCreationDate(unittest.TestCase):
    """ Creation Date test cases
    """

    def test_creation_date_type_file(self):
        with mock.patch('os.path.getctime') as mocked_getctime:
            mocked_getctime.return_value = 1619359381.2359383
            result = creation_date({'item_path': './filename'})
            self.assertEqual(result, '2021-04-25 16:03')


class TestMode(unittest.TestCase):

    def test_mode_type_file(self):
        with mock.patch('os.stat') as mocked_stat:
            import os
            mocked_stat.return_value = os.stat_result((33204, 29463754, 19, 1, 293, 13, 72883,
                                                       1274110664, 1187778284, 1187778284))
            result = mode({'item_path': './filename'})
            self.assertEqual(result, 'rw-rw-r--')


class TestItemName(unittest.TestCase):

    def test_item_name_type_file(self):
        result = item_name({'item_path': './filename'})
        self.assertEqual(result, 'filename')
