from urllib.request import urlopen
import json
import datetime

# API: https://documenter.getpostman.com/view/4876530/SzRxUpPv?version=latest#bf1a26fe-0c42-4b47-8cca-57ce5d9309ac

target_url = 'https://covid19-update-api.herokuapp.com/api/v1/cases/active'
data = urlopen(target_url)
data = data.read().decode()
data = json.loads(data)

with open('active_cases.json') as f:
  activeDict = json.load(f)


date = datetime.date.today()
week = int(date.strftime("%W"))


current_cases = data['activeCases']['total']
def create_new_week(current_cases):
  new_week = {str(week): {
    'high': current_cases,
    'low': current_cases,
    'diff': 0
  }}
  activeDict['weeks'].update(new_week)

print(activeDict['weeks']['33'])
#print(type(activeDict['weeks'][str(week)]['low']))

def update_current_week(current_cases):
  if current_cases < activeDict['weeks'][str(week)]['low']:
    activeDict['weeks'][str(week)]['low'] = current_cases
  if current_cases > activeDict['weeks'][str(week)]['high']:
    activeDict['weeks'][str(week)]['high'] = current_cases
  activeDict['weeks'][str(week)]['diff'] = activeDict['weeks'][str(week)]['high'] - activeDict['weeks'][str(week)]['low']

if activeDict['totals']['current_week'] < week:
  activeDict['totals']['current_week'] = week
  create_new_week(current_cases)
else:
  update_current_week(current_cases)

print(json.dumps(activeDict, indent=2))

