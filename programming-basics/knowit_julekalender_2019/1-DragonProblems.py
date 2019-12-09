from urllib.request import urlopen

target_url = 'https://knowit-julekalender.s3.eu-central-1.amazonaws.com/sau.txt'
data = urlopen(target_url)

sheep_oneliner = data.read().decode()
sheep_strings = sheep_oneliner.split(', ')
daily_sheep = [int(sheep) for sheep in sheep_strings]



# if intake >= apetite => dragon grow by one
# surplus sheep are added to the next day
# if intake < apetite => dragon_size & dragon_apetite shrink by one & shrinkingDays += 1
# if shrinkingDays >= 5 => dragen gets angry and eats the whole village

dragon_size = 50
day = 0
surplus_sheep = 0
starving_days = 0
daily_sheep_mock = [50, 52, 52, 49, 50, 47, 45, 43, 50, 55]

for number_of_sheep in daily_sheep:
    number_of_sheep += surplus_sheep
    surplus_sheep = 0
    if number_of_sheep >= dragon_size:
        starving_days = 0
        surplus_sheep = number_of_sheep - dragon_size
        dragon_size += 1
    else:
        dragon_size -= 1
        starving_days += 1

    day += 1
    print(f'Day: {day} - size: {dragon_size} - sheep: {number_of_sheep} + {surplus_sheep} - starved: {starving_days}')
    if starving_days >= 5:
        print(f'Day {day} - WHAAAAAAAAAAAAAAAAAG!')
        print(f'Survided {day-1} days')
        break
    


