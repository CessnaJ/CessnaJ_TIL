year =int(input())

if year % 400 == 0:
    print(f'{year} is Leap year')
elif (year % 4) == 0 and (year%100) != 0:
    print(f'{year} is Leap year')
else:
    print(f'{year} is not Leap year')