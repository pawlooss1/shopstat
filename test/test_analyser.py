import unittest
import pandas as pd

import shopstat.analyser as analyser

class AnalyserTest(unittest.TestCase):

    @classmethod
    def setUp(self):
        self.addTypeEqualityFunc(pd.Series, assertSeriesEqual)
    
    def test_prices_rounding(self):
        # given
        input = pd.Series([1.125, 4.101, 5.599])
        # when
        output = analyser.round_prices(input)
        # then
        self.assertEqual(output, pd.Series([1.13, 4.11, 5.6]))
        self.assertEqual(output[0], 1.13)
        self.assertEqual(output[1], 4.11)
        self.assertEqual(output[2], 5.6)


def assertSeriesEqual(first, second, msg=None):
    if not first.equals(second):
        raise self.failureException(msg)

if __name__ == '__main__':
    unittest.main()