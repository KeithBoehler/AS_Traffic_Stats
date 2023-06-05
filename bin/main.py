"""
Where it all starts
"""
from datetime import datetime  # pylint: disable=unused-import
import pandas as pd  # pylint: disable=unused-import
import numpy as np  # pylint: disable=unused-import


def datetime_dataframe(loc_dataframe):
    '''
    Intent: Change the Date-Time Column data type from str to datetime
    Precond: Have loaded a datafrom from csv file generated from zoho
    Postcond: Data type of Date-Time will be datetime
    Bugs:
    '''
    # dataframe_col_name = "Date-Time"
    datetime_col = loc_dataframe["Date-Time"].to_numpy()
    for i in range(len(datetime_col)):
        datetime_col[i] = datetime.strptime(datetime_col[i],
                                            '%d-%b-%Y %H:%M:%S')
    new_frame = pd.DataFrame(datetime_col, columns=["Date-Time"])
    loc_dataframe.drop(columns="Date-Time")
    converted_df = pd.concat([new_frame, loc_dataframe])
    return converted_df


def main():
    '''
    Intent
    '''
    print('Start!')
    path_to_csv = "/home/keith/Projects/Python/AS_Traffic_Stats/data/real.csv"
    raw_data_frame = pd.read_csv(path_to_csv)
    trimmed_column_data = raw_data_frame[["Date-Time",
                                         "Customer",
                                          "Fulfillment Order ID",
                                          "Status"]]
    trimmed_column_data = datetime_dataframe(trimmed_column_data)
    print("Done!")


if __name__ == '__main__':
    main()
