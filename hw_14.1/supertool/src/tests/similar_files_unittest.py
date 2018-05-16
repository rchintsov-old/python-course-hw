import src.supertool.similar_files as sf
import unittest
import os
import io
from contextlib import redirect_stdout


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


class TestPrintSimilar(unittest.TestCase):
    
    def test_print_similar_with_no_similar_files_negative(self):

        expected_stdout = '\nSearch path: /home\nNo similar files.\n'
        stdout_handler = io.StringIO()

        with redirect_stdout(stdout_handler):
            sf.print_similar({}, '/home')

        got_stdout = stdout_handler.getvalue()
        self.assertEqual(expected_stdout, got_stdout, 'Wrong stdout')


    def test_print_similar_with_sample_similar_input_positive(self):

        expected_stdout = '\nSearch path: /\n\n1 group(s) of similar ' \
                          'files found:\ngroup 1: a.txt, b.txt\n'

        stdout_handler = io.StringIO()

        with redirect_stdout(stdout_handler):
            sf.print_similar({'123': ['a.txt', 'b.txt']}, '/')

        got_stdout = stdout_handler.getvalue()
        self.assertEqual(expected_stdout, got_stdout, 'Wrong stdout')


class TestMain(unittest.TestCase):

    def test_main_in_duplicates_dir_positive(self):

        expected_stdout = '\nSearch path: ./duplicates\n\n1 group(s) ' \
                          'of similar files found:\ngroup 1: dupl_2.txt, ' \
                          'dupl_1.txt\n'

        stdout_handler = io.StringIO()

        with redirect_stdout(stdout_handler):
            sf.main('./duplicates')

        got_stdout = stdout_handler.getvalue()
        self.assertEqual(expected_stdout, got_stdout, 'Wrong stdout')


    def test_main_in_test_ditectory_negative(self):

        expected_stdout = '\nSearch path: ./\nNo similar files.\n'

        stdout_handler = io.StringIO()

        with redirect_stdout(stdout_handler):
            sf.main('./')

        got_stdout = stdout_handler.getvalue()
        self.assertEqual(expected_stdout, got_stdout, 'Wrong stdout')

