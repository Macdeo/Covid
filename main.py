import datetime
import re
import requests
import json
from datetime import datetime
import pandas as pd
import matplotlib.pyplot as plt
import itertools

# Class set to make a text bold or underlined


class makeBold:
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'


# This is to create current date and time
today = datetime.today()
now = today.strftime("%B %d, %Y")
getTime = datetime.now()
time = getTime.strftime("%HH%M")

print('Welcome, today date is', now, 'at:', time)
print('This Application is to display information on hospital data relating to the COVID-19 epidemic in France.')

# Get the user input on the department
dept = input('Please enter the French department: ')
dept[0].upper()+dept[1:]

# The Json request is done here
# url = https://data.opendatasoft.com/api/records/1.0/search/?dataset=donnees-hospitalieres-covid-19-dep-france%40public&q=&facet=date&facet=countrycode_iso_3166_1_alpha3&facet=region_min&facet=nom_dep_min&facet=sex&refine.sex=Tous&refine.nom_dep_min=Calvados
cUrl = "https://data.opendatasoft.com/api/records/1.0/search/?dataset=donnees-hospitalieres-covid-19-dep-france%40public&q=&rows=10000&sort=-date&facet=date&facet=countrycode_iso_3166_1_alpha3&facet=region_min&facet=nom_dep_min&facet=sex&refine.sex=Tous&refine.nom_dep_min=" + dept
print(cUrl)
covidData = requests.get(cUrl)

# Convert the request gotton from covidData to Json format
jsonData = covidData.json()

# Write to file using the converted Json format variable
with open('data.json', 'w') as outfile:
    importData = json.dump(jsonData, outfile, indent=4)

if jsonData["nhits"] == 0:
    print('There is no department called:', dept)
else:
    print('You have chosen the', (makeBold.BOLD + dept +
          makeBold.END), 'department and it exists !!!')


# keys will ymonths (e.g. "2020-10") and values will be accumulation of newintcare
months = {1: 'Jan', 2: 'Feb', 3: 'Mar', 4: 'Apr', 5: 'May', 6: 'Jun',
          7: 'Jul', 8: 'Aug', 9: 'Sep', 10: 'Oct', 11: 'Nov', 12: 'Dec'}
total = {}


# Get to display the number of intensive care per month
for care in jsonData['records']:
    date = care['fields']['date']
    if "day_intcare_new" in care['fields']:
        intcare = care['fields']['day_intcare_new']
    else:
        intcare = 0

    #ymonth = date[0:7]
    year = date[0:4]
    monthlist = int(date[5:7])
    mon = months[monthlist]

    death = 0
    hospDay = 0
    dayOut = 0

    if "day_hosp" in care['fields']:
        hospDay = care['fields']['day_hosp']
    else:
        hospDay = 0

    if 'day_out_new' in care['fields']:
        dayOut = care['fields']['day_out_new']
    else:
        dayOut = 0

    if 'day_death_new' in care['fields']:
        death = care['fields']['day_death_new']
    else:
        death = 0

    if year in total:
        if mon in total[year]:
            total[year][mon]['hospDay'] = total[year][mon]['hospDay'] + hospDay
            total[year][mon]['intcare'] = total[year][mon]['intcare'] + intcare
            total[year][mon]['dayOut'] = total[year][mon]['dayOut'] + dayOut
            total[year][mon]['death'] = total[year][mon]['death'] + death
        else:
            total[year][mon] = {
                'hospDay': hospDay,
                'intcare': intcare,
                'dayOut': dayOut,
                'death': death,
            }
    else:
        total[year] = {
            mon: {
                'hospDay': hospDay,
                'intcare': intcare,
                'dayOut': dayOut,
                'death': death,
            }
        }



df1 = (pd.DataFrame.from_dict(total["2020"])).T
df2 = (pd.DataFrame.from_dict(total["2021"])).T
df3 = (pd.DataFrame.from_dict(total["2022"])).T

print(df1)
# print(df2)
# print(df3)

frames = [df1, df2, df3]
result = pd.concat(frames, keys=('2020', '2021', '2022'))


print(result)

toCSV = result.to_csv('Covid_data.csv', encoding='utf-8')

readCSV = pd.read_csv('Covid_data.csv')
'''jsonData = dict()
care = jsonData['records']['fields']['reg_code']
print(type(care))'''


#plt.plot(readCSV.intcare, readCSV.death)
plt.scatter(readCSV.death, readCSV.hospDay)
plt.ylabel('Months')
plt.xlabel('Number of Care')
plt.legend()
plt.show()

#plt.pie(carepermonth, carepermonthtime)
# plt.bar()
