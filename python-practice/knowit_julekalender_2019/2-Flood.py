from urllib.request import urlopen

target_url = 'https://knowit-julekalender.s3.eu-central-1.amazonaws.com/2019-luke2/world.txt'
data = urlopen(target_url)

world = []
for i in data:
    world.append(i)

def count_water_in_line(line):
    water = 0
    maybewater = 0
    start = False
    for i in line:
        if i == '#':
            start = True
            water += maybewater
            maybewater = 0
        else:
            if start:
                maybewater += 1  
    return water

decoded_world = [line.decode() for line in world]

total_water = 0
for line in decoded_world:
    total_water += count_water_in_line(line)

print(total_water)


