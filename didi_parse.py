import pandas as pd
import sys

class DidiParse(object):
    """
    Parses all Didi files
    """

    def __init__(self, filename):
        """
        Input: String
        """
        self.filename = filename
        self.order_names = ['order_id','driver_id','passenger_id','start_district_hash','dest_district_hash','price','time']
        self._parse_order_info()

    def _parse_order_info(self):
        """
        Output: DataFrame
        """
        self.order = pd.read_csv(self.filename, delimiter='\t', names=self.order_names)

if __name__ == '__main__':
    filename = 'data/season_1/training_data/order_data/order_data_2016-01-01'
    didi = DidiParse(filename=filename)
