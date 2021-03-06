import matplotlib.pyplot as plt
import csv
from datetime import datetime

open_file = open('death_valley_2018_simple.csv', 'r')

csv_file = csv.reader(open_file, delimiter=',')

header_row = next(csv_file)

#The enumerate() function returns both the index of each item and the value of each
# item as you loop through the list

for index, column_header in enumerate(header_row):
    print('Index:', index, 'Column Name:', column_header)

highs = list()
dates = list()
lows = list()
for row in csv_file:
    try:
        high = int(row[4])
        low = int(row[5])
        converted_date = datetime.strptime(row[2], '%Y-%m-%d')
    except ValueError:
        print(f'Missing data for {converted_date}')
    else:
        highs.append(high)
        lows.append(low)
        dates.append(converted_date)

#print(highs)

#plot highs

import matplotlib.pyplot as plt
#plot highs with dates as x axis
fig = plt.figure()
plt.plot(dates, highs, c='red')
plt.plot(dates, lows, c='blue')
#shade between highs and lows
plt.fill_between(dates, highs, lows, facecolor='blue', alpha=.1)
#label graph
plt.title('Daily high and low temps, 2018', fontsize=16)
plt.ylabel('Temperature (F)', fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)
#autoformat dates so they do not appear squished on visual
fig.autofmt_xdate()

plt.show()

#subplot examples
fig2, a = plt.subplots(2)
a[0].plot(dates, highs, c='red')
a[1].plot(dates, lows, c='blue')

plt.show()
