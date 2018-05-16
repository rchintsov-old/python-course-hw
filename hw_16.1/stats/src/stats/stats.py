import codecs
import csv
import doctest
import urllib
from math import floor
from scipy.stats import norm
from collections import Counter
import matplotlib.pyplot as plt


def csv_data_from_url(url, encoding='utf-8'):
    """
    Receive CSV file from url and transform it to list of lists.

    :param str  url: URL for downloading.
    :param str encoding: encoding of file.
    :return: retrieved data.
    :rtype: list of lists
    """
    result = urllib.request.urlopen(url)

    reader = csv.reader(codecs.iterdecode(result, encoding))

    data = []
    for row in reader:
        data.append(row)

    return data


def categorical_encoding(item, categories):
    """
    Numerical encoding items for specified categories.
    If there are no appropriate category, returns -1.

    :param object item: item to encode.
    :param list categories: categories to encode by.
    :return: digit.
    :rtype: int
    """
    for num, cat in enumerate(categories):
        if item == cat:
            return num
    else:
        return -1


def mean(x):
    """
    Mean of X.

    :param list or tuple x: array to calculate mean.
    :return: mean.
    :rtype: float or None
    :raise ValueError: when len of x == 0.
    """
    if x:
        return sum(x) / len(x)
    else:
        raise ValueError('len of x == 0')


def median(x):
    """
    Median of X.

    :param list or tuple x: array to calculate median.
    :return: median.
    :rtype: int or float
    :raise ValueError: when len of x == 0.
    """
    if x:
        sorted_x = sorted(x)
        n = len(x)
        mid = n // 2
        if n % 2 == 1:
            return sorted_x[mid]
        else:
            return (sorted_x[mid] + sorted_x[mid-1]) / 2

    else:
        raise ValueError('len of x == 0')


def mode(x):
    """
    Mode of X.

    :param list or tuple x: array to calculate mode.
    :return: list of modes.
    :rtype: list
    :raise ValueError: when len of x == 0.
    """
    if x:
        counts = Counter(x)
        max_val = max(counts.values())
        return [k for k, counts in counts.items() if counts == max_val]
    else:
        raise ValueError('len of x == 0')


def quantile(x, percentile):
    """
    Returns value of specified quantile of X.

    :param list or tuple x: array to calculate Q value.
    :param float percentile: percentile (unit fraction).
    :return: Q value.
    :rtype: int or float
    :raise ValueError: when len of x == 0
    """
    if x:
        p_idx = int(percentile * len(x))
        return sorted(x)[p_idx]
    else:
        raise ValueError('len of x == 0')


def data_range(x):
    """
    Range of X.

    :param list or tuple x: array to calculate range.
    :return: range.
    :rtype: int or float
    :raise ValueError: when len of x == 0.
    """
    if x:
        return max(x) - min(x)
    else:
        raise ValueError('len of x == 0')


def variance(x):
    """
    Variance of X.

    :param list or tuple x: array to calculate variance.
    :return: variance.
    :rtype: float
    :raise ValueError: when len of x == 0.
    """
    if x:
        m = mean(x)
        return sum([(i - m) ** 2 for i in x]) / (len(x) - 1)
    else:
        raise ValueError('len of x == 0')


def std(x):
    """
    Standard deviation of X.

    :param list or tuple x: array to calculate std.
    :return: Standard deviation.
    :rtype: float
    :raise ValueError: when len of x == 0.
    """
    if x:
        return variance(x) ** 0.5
    else:
        raise ValueError('len of x == 0')


def dot(x, y):
    """
    Sum of multiplying X and Y elementwise.

    :param list or tuple x: 1st array.
    :param list or tuple y: 2nd array.
    :return: sum of multiplied array.
    :rtype: int or float
    :raise ValueError: when x or y is empty
    """
    if x and y:
        return sum([i * j for i, j in zip(x, y)])
    else:
        raise ValueError('x or y is empty')


def covariation(x, y):
    """
    Covariation of X and Y.

    :param list or tuple x: 1st array.
    :param list or tuple y: 2nd array.
    :return: covariation.
    :rtype: float
    :raise ValueError: when x or y is empty
    """
    if x and y:
        m_x = mean(x)
        m_y = mean(y)
        dev_x = [i - m_x for i in x]
        dev_y = [i - m_y for i in x]

        return dot(dev_x, dev_y) / (len(x) - 1)
    else:
        raise ValueError('x or y is empty')


def correlation(x, y):
    """
    Correlation between X and Y.

    :param list or tuple x: 1st array.
    :param list or tuple y: 2nd array.
    :return: correlation value.
    :rtype: float
    :raise ValueError: when x or y is empty.
    """
    if x and y:
        std_x = std(x)
        std_y = std(y)
        if std_x > 0 and std_y > 0:
            return covariation(x, y) / std_x / std_y
        return 0
    else:
        raise ValueError('x or y is empty')


def make_buckets(x, bucket_size):
    """
    Make buckets from X.

    :param list or tuple x: array to calculate buckets.
    :param int bucket_size: bucket step.
    :return: buckets.
    :rtype: dict
    :raise ValueError: when len of x == 0.
    """
    if x and bucket_size:
        return dict(Counter([bucket_size * floor(i / bucket_size) for i in x]))
    else:
        raise ValueError('len of x == 0 or bucket_size is 0')


def boxplot(x):
    """
    Box plot function.

    :param array x: array to ploting with.
    :return: plot object.
    :rtype: object
    :raise ValueError: when len of x == 0.
    """
    if x:
        plt.boxplot(x)
    else:
        raise ValueError('len of x == 0')


def histogram(x):
    """
    Histogram plot function.

    :param array x: array to ploting with.
    :return: plot object.
    :rtype: object
    :raise ValueError: when len of x == 0.
    """
    if x:
        plt.hist(x)
    else:
        raise ValueError('len of x == 0')


def plot(x, *args, **kwargs):
    """
    Plotting function.

    :param array x: array to ploting with.
    :return: plot object.
    :rtype: object
    :raise ValueError: when len of x == 0.
    """
    if x:
        plt.plot(x, *args, **kwargs)
    else:
        raise ValueError('len of x == 0')


def pdf(x):
    """
    Probability density function.

    :param array x: array for pdf matching.
    :return: list of values.
    :rtype: list
    :raise ValueError: when len of x == 0.
    """
    if x:
        return norm.pdf(x, mean(x), std(x)).tolist()
    else:
        raise ValueError('len of x == 0')


def cdf(x):
    """
    Cumulative distribution function.

    :param array x: array for cdf matching.
    :return: list of values.
    :rtype: list
    :raise ValueError: when len of x == 0.
    """
    if x:
        return norm.cdf(x, mean(x), std(x)).tolist()
    else:
        raise ValueError('len of x == 0')
