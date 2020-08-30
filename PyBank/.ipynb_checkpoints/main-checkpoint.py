import os
import csv

import pandas as pd
# convert cvs file to xlsx
read_file = pd.read_csv (r'C:\Users\steve\homework\PyPoll_data.csv')
read_file.to_excel (r'C:\Users\steve\homework\PyPoll_data.xlsx', index = None, header=True)

# create year-month column from dates, to determine the total number of months included in the dataset
import pandas as pd
import datetime
import random

# xxx, to determine the net total of amount of "profit/losses" over the entire period

# xxx, to determine the greatest increase in profits (date and amount) over the entire period

# xxx, to determine the greatest decrease in losses (date and amount) over the entire period






