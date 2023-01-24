# future population estimation
import datetime

future_year = int(input("Enter a year in the future: "))

current_year = datetime.date.today().year
print("Current year is", current_year)

current_population = 307_357_870
days_in_year = 365

new_births_per_day = 86400 // 7
print('new births per day', new_births_per_day)

deaths_per_day = 86400 // 13
print('deaths per day', deaths_per_day)

new_inmigrants_per_day = 86400 // 35
print('new inmigrants per day', new_inmigrants_per_day)

difference_people_per_day = new_births_per_day - deaths_per_day
real_people_per_day = difference_people_per_day + new_inmigrants_per_day
print('real new people per day', real_people_per_day)

years = future_year - current_year
print('total years until', future_year, '=', years)

future_population = real_people_per_day * days_in_year * years
print(future_population, 'new people will be born in', years, 'years')

total = future_population + current_population
print("The population in", future_year, "will be", total)
