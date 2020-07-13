s = 'abcdefghijklmnopqrstuvwxyz'

longest = ''
current = None

for c in s:
    if current is None:
        current = c
    elif c >= current[-1]:
        current += c
    else:
        if len(current) > len(longest):
            longest = current
        
        current = c

if len(longest) == 0:
    longest = current
    
print('Longest substring in alphabetical order is:', longest)