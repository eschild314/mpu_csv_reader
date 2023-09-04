import pandas as pd
from datetime import datetime

def convert_datetime():
  # Read the CSV file
  mdata = pd.read_csv('statement.csv')

  # A convoluted method to convert the Date column to datetime objects...
  # I knew there was a faster method but found it as soon as I finished this.
  for i in range(0, mdata[mdata.columns[0]].count()):
      dateStr = mdata.at[i, 'Date'].split('/')
      
      dateStr[2] = dateStr[2].split(' ')
      dateStr[2][1] = dateStr[2][1].split(':')
      if dateStr[2][1][1][-2:] == 'PM' and int(dateStr[2][1][0]) < 12:
          dateStr[2][1][0] = int(dateStr[2][1][0]) + 12

      dateStr[2][1][1] = int(dateStr[2][1][1][:-2])

      newDate = datetime(int(dateStr[2][0]), int(dateStr[0]), int(dateStr[1]), int(dateStr[2][1][0]), int(dateStr[2][1][1]))
      mdata.at[i, 'Date'] = newDate

  mdata.to_csv('statement1.csv')