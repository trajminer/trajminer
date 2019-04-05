import pandas as pd
import utm
from datetime import datetime


data = pd.read_csv('https://www.fs.fed.us/pnw/starkey/data/' +
                   'tables/Starkey_OR_Main_Telemetry_1993-1996_Data.txt')


def convert_utm_lat(row):
    return utm.to_latlon(row[1], row[2], 11, 'T')[0]


def convert_utm_long(row):
    return utm.to_latlon(row[1], row[2], 11, 'T')[1]


def format_date_utc(row):
    dt = str(row[6])
    dt = dt[6:8] + '-' + dt[4:6] + '-' + dt[0:4] + ' ' + str(row[5])
    return datetime.strptime(dt, '%d-%m-%Y %H:%M:%S')


def format_date_local(row):
    dt = str(row[7])
    dt = dt[6:8] + '-' + dt[4:6] + '-' + dt[0:4] + ' ' + str(row[8])
    return datetime.strptime(dt, '%d-%m-%Y %H:%M:%S')


def rename_animal(row):
    if(str(row[10]).strip() == 'C'):
        return 'cattle'
    if(str(row[10]).strip() == 'E'):
        return 'elk'
    if(str(row[10]).strip() == 'D'):
        return 'deer'
    return row[10]

data['lat'] = data.apply(lambda x: convert_utm_lat(x), axis=1)
data['lon'] = data.apply(lambda x: convert_utm_long(x), axis=1)
data['date_time_utc'] = data.apply(lambda x: format_date_utc(x), axis=1)
data['date_time_local'] = data.apply(lambda x: format_date_local(x), axis=1)
data[' Species'] = data.apply(lambda x: rename_animal(x), axis=1)

data.columns = [x.strip() for x in data.columns]
data.drop(['UTMGrid', 'GMDate', 'GMTime', 'LocDate', 'LocTime', 'Year',
           'UTME', 'UTMN', 'StarkeyTime', 'UTMGridEast', 'UTMGridNorth',
           'RadNum'],
          axis='columns', inplace=True)

data.rename(columns={'Id': 'tid',
                     'Species': 'species',
                     'Elev': 'altitude',
                     'Grensunr': 'sunrise_time_utc',
                     'Grensuns': 'sunset_time_utc',
                     'Obswt': 'obs_weight'}, inplace=True)

data.sort_values(by=['tid', 'date_time_utc'], ascending=True, inplace=True)
data.to_csv('starkey_animals.csv', index=False)
