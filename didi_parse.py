import pandas as pd
import sys

class DidiParse(object):

    def __init__(self, filename):
        """
        Input: String
        """
        self.filename = filename

    def parse_order_info(filename):
        """
        
        """
        col_names = ['order_id','driver_id','passenger_id','start_district_hash','dest_district_hash','price','time']
        df = pd.read_csv(filename, delimiter='\t', names=col_names)

if __name__ == '__main__':
    filename = 'data/season_1/training_data/order_data/order_data_2016-01-01'
    didi = DidiParse(filename=filename)
    parse_order_info(filename)
