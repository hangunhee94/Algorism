Hour, Minute = map(int, input().split())

if Minute > 44:
    print(Hour, Minute-45)
elif Minute < 45 and Hour > 0:
    print(Hour-1, Minute+15)
else:
    print(23, Minute+15)
