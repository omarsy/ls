import unittest
from src.list_folder_items import list_folder_items_with_prefix, list_folder_items
from src.folder_item_information import item_name


class TestListFolder(unittest.TestCase):
    def test_list_folder_all_filter_pass(self):
        with unittest.mock.patch('os.listdir') as mocked_listdir:
            mocked_listdir.return_value = ['file1', 'file2', 'file3']
            result = list(list_folder_items({'path': 'folder'}, [lambda *unused: True, lambda *unused: True,
                                                                 lambda *unused: True], [lambda *unused: '1', lambda *unused: '2', item_name]))
            self.assertEqual(result, ['1 2 file1', '1 2 file2', '1 2 file3'])

    def test_list_folder_one_filter_not_pass(self):
        with unittest.mock.patch('os.listdir') as mocked_listdir:
            mocked_listdir.return_value = ['file1', 'file2', 'file3']
            result = list(list_folder_items({'path': 'folder'}, [lambda *unused: False, lambda *unused: True,
                                                                 lambda *unused: True], [lambda *unused: '1', lambda *unused: '2', item_name]))
            self.assertEqual(result, [])

    def test_list_folder_empty_filter(self):
        with unittest.mock.patch('os.listdir') as mocked_listdir:
            mocked_listdir.return_value = ['file1', 'file2', 'file3']
            result = list(list_folder_items({'path': 'folder'}, [], [lambda *unused: '1', lambda *unused: '2', item_name]))
            self.assertEqual(result, ['1 2 file1', '1 2 file2', '1 2 file3'])

    def test_list_folder_all_filter_not_pass(self):
        with unittest.mock.patch('os.listdir') as mocked_listdir:
            mocked_listdir.return_value = ['file1', 'file2', 'file3']
            result = list(list_folder_items({'path': 'folder'}, [lambda *unused: False, lambda *unused: False,
                                                                 lambda *unused: False], [lambda *unused: '1', lambda *unused: '2', item_name]))
            self.assertEqual(result, [])


class TestListFolderItemsWithPrefix(unittest.TestCase):
    def test_list_folder_items(self):
        with unittest.mock.patch('os.listdir') as mocked_listdir:
            with unittest.mock.patch('os.path.isdir') as mocked_isdir:
                mocked_listdir.return_value = ['file1', 'file2', 'file3']
                mocked_isdir.return_value = True
                result = list(list_folder_items_with_prefix('folder', [], [item_name]))
                self.assertEqual(result, ['file1', 'file2', 'file3'])

    def test_list_folder_items_with_prefix(self):
        with unittest.mock.patch('os.listdir') as mocked_listdir:
            with unittest.mock.patch('os.path.isdir') as mocked_isdir:
                mocked_listdir.return_value = ['file1', 'file2', 'file3', 'fel']
                mocked_isdir.side_effect = [False, True]
                result = list(list_folder_items_with_prefix('folder/fi', [], [item_name]))
                self.assertEqual(result, ['file1', 'file2', 'file3'])

    def test_list_folder_items_unknown_folder(self):
        with unittest.mock.patch('os.path.isdir') as mocked_isdir:
            mocked_isdir.side_effect = [False, False]
            result = list(list_folder_items_with_prefix('folder', [], []))
            self.assertEqual(result, [])
