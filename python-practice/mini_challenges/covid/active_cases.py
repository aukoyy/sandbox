from urllib.request import urlopen
import json
import datetime

# API: https://documenter.getpostman.com/view/4876530/SzRxUpPv?version=latest#bf1a26fe-0c42-4b47-8cca-57ce5d9309ac

date = datetime.date.today()
week = int(date.strftime("%W"))

target_url = 'https://covid19-update-api.herokuapp.com/api/v1/cases/active'
file_path = '/Users/auk/code/projects/sandbox/python-practice/mini_challenges/covid/active_cases.json'
data = urlopen(target_url)
data = data.read().decode()
data = json.loads(data)
current_cases = data['activeCases']['total']

with open(file_path) as f:
  activeDict = json.load(f)


def create_new_week(current_cases):
  #TODO: add from last week
  lastHigh = activeDict['weeks'][str(week-1)]['high']
  lastLow = activeDict['weeks'][str(week-1)]['low']
  
  if lastHigh < current_cases: # new high
    new_week = {str(week): {
      'high': current_cases,
      'low': lastHigh,
      'diff': current_cases - lastHigh
    }}
  else:# new low
    new_week = {str(week): {
      'high': lastLow,
      'low': current_cases,
      'diff': current_cases - lastLow
    }}
  activeDict['weeks'].update(new_week)


def update_current_week(current_cases):
  if current_cases < activeDict['weeks'][str(week)]['low']:
    activeDict['weeks'][str(week)]['low'] = current_cases
    activeDict['weeks'][str(week)]['diff'] = activeDict['weeks'][str(week)]['high'] - current_cases
  if current_cases > activeDict['weeks'][str(week)]['high']:
    activeDict['weeks'][str(week)]['high'] = current_cases
    activeDict['weeks'][str(week)]['diff'] = current_cases - activeDict['weeks'][str(week)]['low']


if activeDict['totals']['current_week'] < week:
  activeDict['totals']['current_week'] = week
  create_new_week(current_cases)
else:
  update_current_week(current_cases)

with open(file_path, 'w') as f:
  json.dump(activeDict, f, indent=2)


print('### Covid Update ###')
print('Current cases: ' + '{:,}'.format(current_cases))
change_this_week = activeDict['weeks'][str(week)]['diff']
print('Change this week: ' + '{:,}'.format(change_this_week))