import json
import datetime
import requests


date = datetime.date.today()
week = int(date.strftime("%W"))

url = "https://covid-19-data.p.rapidapi.com/totals"
headers = {
    'x-rapidapi-key': "d39c80742emsha4a71413f74e250p132e54jsnf58a627c3630",
    'x-rapidapi-host': "covid-19-data.p.rapidapi.com"
}
response = requests.request("GET", url, headers=headers)
data = json.loads(response.text)

file_path = '/Users/auk/code/projects/sandbox/python-practice/mini_challenges/covid/active_cases.json'


confirmed = 88830659  # data[0]['confirmed']
recovered = data[0]['recovered']
deaths = data[0]['deaths']
active = confirmed - recovered - deaths


with open(file_path) as f:
    activeDict = json.load(f)

lastHigh = activeDict['weeks'][str(week-1)]['high']
lastLow = activeDict['weeks'][str(week-1)]['low']
newHigh = lastHigh < active


def create_new_week(current_cases):
    if newHigh:
        new_week = {str(week): {
            'high': current_cases,
            'low': lastHigh,
            'diff': current_cases - lastHigh
        }}
    else:
        new_week = {str(week): {
            'high': lastLow,
            'low': current_cases,
            'diff': current_cases - lastLow
        }}
    activeDict['weeks'].update(new_week)


def update_current_week(current_cases):
    if current_cases < activeDict['weeks'][str(week)]['low']:
        activeDict['weeks'][str(week)]['low'] = current_cases
        activeDict['weeks'][str(week)]['diff'] = activeDict['weeks'][str(
            week)]['high'] - current_cases
    if current_cases > activeDict['weeks'][str(week)]['high']:
        activeDict['weeks'][str(week)]['high'] = current_cases
        activeDict['weeks'][str(week)]['diff'] = current_cases - \
            activeDict['weeks'][str(week)]['low']


if activeDict['totals']['current_week'] < week:
    activeDict['totals']['current_week'] = week
    create_new_week(active)
else:
    update_current_week(active)

with open(file_path, 'w') as f:
    json.dump(activeDict, f, indent=2)


# SPANISH FLUE NUMBERS FOR COMPARASON
SPANISH_CONFIRMED = 500000000  # word confirmed are used as domain language
SPANISH_DEATHS = 50000000
POPULATION_ADJUSTMENT_CONSTANT = 4.19
SPANISH_CONFIRMED_ADJUSTED = SPANISH_CONFIRMED * POPULATION_ADJUSTMENT_CONSTANT
SPANISH_DEATHS_ADJUSTED = SPANISH_DEATHS * POPULATION_ADJUSTMENT_CONSTANT

print('### Covid Update ### (<absolute compered to spanish flue>) (adjusted comparason)')
change_this_week = activeDict['weeks'][str(week)]['diff']
print(f'Change: {change_this_week:,}')
print(
    f'Confirmed: {confirmed:,} ({confirmed/SPANISH_CONFIRMED*100:.2f}%) ({confirmed/SPANISH_CONFIRMED_ADJUSTED*100:.2f}%)')
print(f'Recovered: {recovered:,}')
print(f'Deaths: {deaths:,} ({deaths/SPANISH_DEATHS*100:.2f}%) ({deaths/SPANISH_DEATHS_ADJUSTED*100:.2f}%)')
print(f'Active: {active:,}')
