import os
import csv

import pandas as pd

read_file = pd.read_csv (r'C:\Users\steve\homework\PyPoll_data.csv')
read_file.to_excel (r'C:\Users\steve\homework\PyPoll_data.xlsx', index = None, header=True)




