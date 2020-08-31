from urllib.request import urlopen
import json

# API: https://documenter.getpostman.com/view/4876530/SzRxUpPv?version=latest#bf1a26fe-0c42-4b47-8cca-57ce5d9309ac

target_url = 'https://covid19-update-api.herokuapp.com/api/v1/cases/active'
file_path = '/Users/auk/code/projects/sandbox/python-practice/mini_challenges/covid/active_cases.txt'
data = urlopen(target_url)
data = data.read().decode()
data = json.loads(data)


with open(file_path, "r") as file:
    first_line = file.readline()
    for last_line in file:
      pass


timeStamp = data['timeStamp']
currentCases = data['activeCases']['total']
change_from_last_run = currentCases - int(last_line.replace(',',''))

f = open(file_path, "a")
f.write('\n\n')
f.write(timeStamp + '\n')
f.write('Change from last run: {:,}'.format(change_from_last_run))
f.write('\n' + str('{:,}'.format(currentCases)))
print('\nChange from last run : ' + str('{:,}'.format(change_from_last_run)) + '\n')

f.close()