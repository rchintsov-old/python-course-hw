import unittest
from stats import stats
    

class TestCsvDataFromUrl(unittest.TestCase):

    def test_csv_data_from_url_positive(self):
        self.assertEqual(stats.csv_data_from_url('https://raw.githubusercontent.com/plotly/datasets/master/iris.csv')[0], ['SepalLength', 'SepalWidth', 'PetalLength', 'PetalWidth', 'Name'], "Wrong answer")


class TestCategoricalEncoding(unittest.TestCase):

    def test_categorical_encoding_positive(self):
        self.assertEqual(stats.categorical_encoding(1, [2, 1]), 1, "Wrong answer")


    def test_categorical_encoding_positive_2(self):
        self.assertEqual(stats.categorical_encoding(3, [2, 1]), -1, "Wrong answer")


class TestMean(unittest.TestCase):

    def test_mean_positive(self):
        self.assertEqual(stats.mean([1,2]), 1.5, "Wrong answer")


    # testing an exception of ValueError: len of x == 0
    def test_mean_ValueError_exception(self):

        with self.assertRaises(ValueError) as e:
            stats.mean([])

        self.assertEqual(str(e.exception), "len of x == 0", "description doesn't match")


class TestMedian(unittest.TestCase):

    def test_median_positive(self):
        self.assertEqual(stats.median([1,2,3,4]), 2.5, "Wrong answer")


    def test_median_positive_2(self):
        self.assertEqual(stats.median([1,2,3]), 2, "Wrong answer")


    # testing an exception of ValueError: len of x == 0
    def test_median_ValueError_exception(self):

        with self.assertRaises(ValueError) as e:
            stats.median([])

        self.assertEqual(str(e.exception), "len of x == 0", "description doesn't match")


class TestMode(unittest.TestCase):

    def test_mode_positive(self):
        self.assertEqual(stats.mode([1,2,2,3]), [2], "Wrong answer")


    # testing an exception of ValueError: len of x == 0
    def test_mode_ValueError_exception(self):

        with self.assertRaises(ValueError) as e:
            stats.mode([])

        self.assertEqual(str(e.exception), "len of x == 0", "description doesn't match")


class TestQuantile(unittest.TestCase):

    def test_quantile_positive(self):
        self.assertEqual(stats.quantile([1,20,40,60,80,100], 0.5), 60, "Wrong answer")


    # testing an exception of ValueError: len of x == 0
    def test_quantile_ValueError_exception(self):

        with self.assertRaises(ValueError) as e:
            stats.quantile([], 0.5)

        self.assertEqual(str(e.exception), "len of x == 0", "description doesn't match")


class TestDataRange(unittest.TestCase):

    def test_data_range_positive(self):
        self.assertEqual(stats.data_range([1,2,3.5]), 2.5, "Wrong answer")


    # testing an exception of ValueError: len of x == 0
    def test_data_range_ValueError_exception(self):

        with self.assertRaises(ValueError) as e:
            stats.data_range([])

        self.assertEqual(str(e.exception), "len of x == 0", "description doesn't match")


class TestVariance(unittest.TestCase):

    def test_variance_positive(self):
        self.assertEqual(stats.variance([1,2,3]), 1.0, "Wrong answer")


    # testing an exception of ValueError: len of x == 0
    def test_variance_ValueError_exception(self):

        with self.assertRaises(ValueError) as e:
            stats.variance([])

        self.assertEqual(str(e.exception), "len of x == 0", "description doesn't match")


class TestStd(unittest.TestCase):

    def test_std_positive(self):
        self.assertEqual(stats.std([1,2,3]), 1.0, "Wrong answer")


    # testing an exception of ValueError: len of x == 0
    def test_std_ValueError_exception(self):

        with self.assertRaises(ValueError) as e:
            stats.std([])

        self.assertEqual(str(e.exception), "len of x == 0", "description doesn't match")


class TestDot(unittest.TestCase):

    def test_dot_positive(self):
        self.assertEqual(stats.dot([1,2,3], [1,2,3]), 14, "Wrong answer")


    # testing an exception of ValueError: x or y is empty
    def test_dot_ValueError_exception(self):

        with self.assertRaises(ValueError) as e:
            stats.dot([], [])

        self.assertEqual(str(e.exception), "x or y is empty", "description doesn't match")


class TestCovariation(unittest.TestCase):

    def test_covariation_positive(self):
        self.assertEqual(stats.covariation([1,2,3], [1,2,3]), 1.0, "Wrong answer")


    # testing an exception of ValueError: x or y is empty
    def test_covariation_ValueError_exception(self):

        with self.assertRaises(ValueError) as e:
            stats.covariation([], [])

        self.assertEqual(str(e.exception), "x or y is empty", "description doesn't match")


class TestCorrelation(unittest.TestCase):

    def test_correlation_positive(self):
        self.assertEqual(stats.correlation([1,2,3], [1,2,3]), 1.0, "Wrong answer")


    # testing an exception of ValueError: x or y is empty
    def test_correlation_ValueError_exception(self):

        with self.assertRaises(ValueError) as e:
            stats.correlation([], [])

        self.assertEqual(str(e.exception), "x or y is empty", "description doesn't match")


class TestMakeBuckets(unittest.TestCase):

    def test_make_buckets_positive(self):
        self.assertEqual(stats.make_buckets([1,2,3], 1), {1: 1, 2: 1, 3: 1}, "Wrong answer")


    # testing an exception of ValueError: len of x == 0 or bucket_size is 0
    def test_make_buckets_ValueError_exception(self):

        with self.assertRaises(ValueError) as e:
            stats.make_buckets([], 1)

        self.assertEqual(str(e.exception), "len of x == 0 or bucket_size is 0", "description doesn't match")


    def test_make_buckets_ValueError_exception_2(self):

        with self.assertRaises(ValueError) as e:
            stats.make_buckets([1,2,3], 0)

        self.assertEqual(str(e.exception), "len of x == 0 or bucket_size is 0", "description doesn't match")


class TestBoxplot(unittest.TestCase):

    def test_boxplot_returns_None(self):
        self.assertIsNone(stats.boxplot([1,2,3]), "The function returned some result")


    # testing an exception of ValueError: len of x == 0
    def test_boxplot_ValueError_exception(self):

        with self.assertRaises(ValueError) as e:
            stats.boxplot([])

        self.assertEqual(str(e.exception), "len of x == 0", "description doesn't match")


class TestHistogram(unittest.TestCase):

    def test_histogram_returns_None(self):
        self.assertIsNone(stats.histogram([1,2,3]), "The function returned some result")


    # testing an exception of ValueError: len of x == 0
    def test_histogram_ValueError_exception(self):

        with self.assertRaises(ValueError) as e:
            stats.histogram([])

        self.assertEqual(str(e.exception), "len of x == 0", "description doesn't match")


class TestPlot(unittest.TestCase):

    def test_plot_returns_None(self):
        self.assertIsNone(stats.plot([1,2,3]), "The function returned some result")


    # testing an exception of ValueError: len of x == 0
    def test_plot_ValueError_exception(self):

        with self.assertRaises(ValueError) as e:
            stats.plot([])

        self.assertEqual(str(e.exception), "len of x == 0", "description doesn't match")


class TestPdf(unittest.TestCase):

    def test_pdf_positive(self):
        self.assertEqual(stats.pdf([1,2,3]), [0.24197072451914337, 0.3989422804014327, 0.24197072451914337], "Wrong answer")


    # testing an exception of ValueError: len of x == 0
    def test_pdf_ValueError_exception(self):

        with self.assertRaises(ValueError) as e:
            stats.pdf([])

        self.assertEqual(str(e.exception), "len of x == 0", "description doesn't match")


class TestCdf(unittest.TestCase):

    def test_cdf_positive(self):
        self.assertEqual(stats.cdf([1,2,3]), [0.15865525393145707, 0.5, 0.8413447460685429], "Wrong answer")


    # testing an exception of ValueError: len of x == 0
    def test_cdf_ValueError_exception(self):

        with self.assertRaises(ValueError) as e:
            stats.cdf([])

        self.assertEqual(str(e.exception), "len of x == 0", "description doesn't match")


if __name__ == '__main__':
    unittest.main()
