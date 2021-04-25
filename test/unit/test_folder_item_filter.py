import unittest
from src.folder_item_filter import is_file, is_basename_prefixed


class TestIsFile(unittest.TestCase):

    def test_is_file_return_true_type_file(self):
        with unittest.mock.patch('os.path.isfile') as mocked_isfile:
            mocked_isfile.return_value = True
            result = is_file({'item_path': './filename'})
            self.assertEqual(result, True)


class TestIsBasenamePrefixed(unittest.TestCase):

    def test_is_basename_prefixed_good_prefix_type_file(self):
        result = is_basename_prefixed({'item_path': './filename', 'prefix': 'fi'})
        self.assertEqual(result, True)

    def test_is_basename_prefixed_bad_prefix_type_file(self):
        result = is_basename_prefixed({'item_path': './filename', 'prefix': 'fis'})
        self.assertEqual(result, False)
