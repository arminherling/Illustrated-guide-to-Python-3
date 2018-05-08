# Exercise: Write Python code to determine if 1800, 1900, 1903, 2000, and 2002 are leap years.

year = 1800
dividable_by_4 = year % 4 == 0
dividable_by_100 = year % 100 == 0
dividable_by_400 = year % 400 == 0
result = False

if(dividable_by_4 and dividable_by_100):
    result = dividable_by_400

print(year, 'is a leap year:', result)


year = 1900
dividable_by_4 = year % 4 == 0
dividable_by_100 = year % 100 == 0
dividable_by_400 = year % 400 == 0
result = False

if(dividable_by_4 and dividable_by_100):
    result = dividable_by_400

print(year, 'is a leap year:', result)


year = 1903
dividable_by_4 = year % 4 == 0
dividable_by_100 = year % 100 == 0
dividable_by_400 = year % 400 == 0
result = False

if(dividable_by_4 and dividable_by_100):
    result = dividable_by_400

print(year, 'is a leap year:', result)


year = 2000
dividable_by_4 = year % 4 == 0
dividable_by_100 = year % 100 == 0
dividable_by_400 = year % 400 == 0
result = False

if(dividable_by_4 and dividable_by_100):
    result = dividable_by_400

print(year, 'is a leap year:', result)


year = 2002
dividable_by_4 = year % 4 == 0
dividable_by_100 = year % 100 == 0
dividable_by_400 = year % 400 == 0
result = False

if(dividable_by_4 and dividable_by_100):
    result = dividable_by_400

print(year, 'is a leap year:', result)
