number = int(input('Enter a integer: '))
result = 0

print('')

while result ** 3 < abs(number):
    print('Trying', result, '** 3 ==', result ** 3)
    result += 1

print('')
print('Checking', result, '** 3 ==', result ** 3)

if result ** 3 == abs(number):
    if number < 0:
        result = -result
    print('Found! The cube root of', number, 'is', result)
else:
    print('Sorry, this number is not a perfect cube')
