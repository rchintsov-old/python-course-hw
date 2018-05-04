import src.supertool.similar_files as sf
import unittest
import os


class TestMD5Calc(unittest.TestCase):
    
    def test_md5_calc_with_non_dupl_file_positive(self):
        self.assertEqual(sf.md5_calc('duplicates/non_dupl.txt'),
                         'aa6c1acf485ea24d50f0c55dc0e7944a', 'Wrong MD5')


    def test_md5_calc_with_non_dupl_file_output_type_positive(self):
        self.assertIsInstance(sf.md5_calc('duplicates/non_dupl.txt'), str,
                              'Wrong type of MD5')


class TestGetFilelist(unittest.TestCase):
    
    def test_get_filelist_from_duplicate_folder_positive(self):
        self.assertEqual(sf.get_filelist('duplicates'),
                         ['dupl_2.txt', 'non_dupl.txt', 'dupl_1.txt'], 
                         'Wrong file list')


    def test_get_filelist_from_duplicate_folder_type_positive(self):
        self.assertIsInstance(sf.get_filelist('duplicates'),
                              list, 'Wrong type of file list')


class TestCompareMD5Sums(unittest.TestCase):

    def setUp(self):
        os.chdir('duplicates')


    def test_compare_md5_sums_in_test_folder_positive(self):
        self.assertEqual(sf.compare_md5_sums(
            ['dupl_2.txt', 'non_dupl.txt', 'dupl_1.txt']),
            {'b517aac169caa1ca2a0a1ce57ca17b70': ['dupl_2.txt', 'dupl_1.txt']},
            'Wrong hash or file list of duplicates')


    def test_compare_md5_sums_in_test_folder_out_dict_positive(self):
        self.assertIsInstance(sf.compare_md5_sums(
            ['dupl_2.txt', 'non_dupl.txt', 'dupl_1.txt']), dict,
            'Wrong type of output duplicates list')

    def tearDown(self):
        os.chdir('../')


