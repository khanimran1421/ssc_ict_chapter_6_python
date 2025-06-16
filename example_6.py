print('1: Feet to meters, 2: meters to feet.')

choice = int(input('Enter your choice: '))

if choice ==1:
    num = float(input('Enter number of feet: '))
    print('Meter:', round((num/3.28),3))
else:
    num = float(input('Enter number of meters: '))
    print('Feet',round((num*3.28),3))