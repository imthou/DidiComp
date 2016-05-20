import pandas as pd
import sys
import os

class DidiParse(object):
    """
    Parses all Didi files
    """

    def __init__(self):
        """
        """
        self.orderpath = '/data/season_1/training_data/order_data/'
        self.orderdir = os.listdir(os.getcwd() + self.orderpath)
        self.order_names = ['order_id','driver_id','passenger_id','start_district_hash','dest_district_hash','price','time']
        self.order = []
        self._parse_order_info()

    def _parse_order_info(self):
        """
        Output: DataFrame

        Parses all order info tables
        """
        for filename in self.orderdir:
            self.order.append(pd.read_csv(self.orderpath[1:] + filename, delimiter='\t', names=self.order_names, parse_dates=['time']))
            print "parsed {}".format(filename)
        self.order = pd.concat(self.order)

if __name__ == '__main__':
    didi = DidiParse()
