'''

'''
import unittest
from bin.main import datetime_dataframe
import pandas as pd
from datetime import datetime


class TestCSVReading(unittest.TestCase):
    '''docs
    '''
    def test_str_to_datetime(self):
        """ Test converting string date to datetime obj """
        test_frame = pd.read_csv(
            "/home/keith/Projects/Python/AS_Traffic_Stats/data/single.csv")
        test_frame = datetime_dataframe(test_frame)
        hard_date = datetime(2022, 12, 9, 14, 20, 52)
        self.assertEqual(test_frame["Date-Time"].iloc[0], hard_date)


if __name__ == '__main__':
    unittest.main()
