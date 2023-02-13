from list_ext import List

years = List[int]()
# []

print(years.first_or_default(2012))
# output: 2012

print(years.last_or_default(2023))
# output: 2023


years.append(2020) # [2020]
years.append(2021) # [2020, 2021]

print(years.first)
# output: 2020
print(years.first_or_default(2012))
# output: 2020

print(years.last)
# output: 2021
print(years.last_or_default(2023))
# output: 2021

print(years.contains(2020))
# output: True
print(years.contains(2010))
# output: False

years.append(2022) # [2020, 2021, 2022]


print(years.concat())
# output: 2020, 2021, 2022
print(years.concat(sep=" "))
# output: 2020 2021 2022


years.append(2023) # [2020, 2021, 2022, 2023]

print(years.first_where(lambda x: (x % 2) == 1))
# output: 2021