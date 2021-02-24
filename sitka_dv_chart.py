import matplotlib.pyplot as plt
import csv
from datetime import datetime

dv_file = open('death_valley_2018_simple.csv', 'r')
sitka_file = open('sitka_weather_2018_simple.csv', 'r')

dv_file = csv.reader(dv_file, delimiter=',')
sitka_file = csv.reader(sitka_file, delimiter=',')

dv_headers = next(dv_file)
sitka_headers = next(sitka_file)

#The enumerate() function returns both the index of each item and the value of each
# item as you loop through the list

max_label = 'TMAX'
min_label = 'TMIN'
date_label = 'DATE'
#get index positions of max and min columns for sitka and death valley file
for index, column_header in enumerate(dv_headers):
    if column_header == max_label:
        dv_max_index = index
    if column_header == min_label:
        dv_min_index = index
    if column_header == date_label:
        date_index = index

for index, column_header in enumerate(sitka_headers):
    if column_header == max_label:
        sitka_max_index = index
    if column_header == min_label:
        sitka_min_index = index

sitka_highs = list()
sitka_lows = list()
dv_highs = list()
dv_lows = list()
dates = list()

for dv_row, sitka_row in zip(dv_file, sitka_file):
    try:
        dv_high = int(dv_row[dv_max_index])
        dv_low = int(dv_row[dv_min_index])
        sitka_high = int(sitka_row[sitka_max_index])
        sitka_low = int(sitka_row[sitka_min_index])
        converted_date = datetime.strptime(dv_row[date_index], '%Y-%m-%d')
    except ValueError:
        print(f'Missing data for {converted_date}')
    else:
        sitka_highs.append(sitka_high)
        sitka_lows.append(sitka_low)
        dv_highs.append(dv_high)
        dv_lows.append(dv_low)
        dates.append(converted_date)

fig, a = plt.subplots(2)
plt.title(
    'Temperature Comparison Between SITKA Airport, AK US, and Death Valley, CA US',
    fontsize=16)
fig.autofmt_xdate()
plt.tick_params(axis='both', which='major', labelsize=16)
#sitka plot
a[0].plot(dates, sitka_highs, c='red')
a[0].plot(dates, sitka_lows, c='blue')
a[0].fill_between(dates, sitka_highs, sitka_lows, facecolor='blue', alpha=.1)
a[0].set_title('SITKA Airport, AK US', fontsize=16)
a[0].set_ylabel('Temperature (F)', fontsize=16)
#death valley plot
a[1].plot(dates, dv_highs, c='red')
a[1].plot(dates, dv_lows, c='blue')
a[1].fill_between(dates, dv_highs, dv_lows, facecolor='blue', alpha=.1)
a[1].set_title('SITKA Airport, AK US', fontsize=16)
a[1].set_ylabel('Temperature (F)', fontsize=16)

plt.show()
