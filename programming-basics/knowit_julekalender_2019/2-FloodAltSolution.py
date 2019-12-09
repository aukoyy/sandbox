from urllib.request import urlopen

target_url = 'https://knowit-julekalender.s3.eu-central-1.amazonaws.com/2019-luke2/world.txt'

with urlopen(target_url) as response:
    lines = [line.decode() for line in response]

    total = 0
    for line in lines:
        line = line.strip()
        total += line.count(' ')


print(total)