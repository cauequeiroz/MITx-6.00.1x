s = 'azcbobobegghakl'
occurs = 0

index = 0
while index < len(s):
    if s[index] == 'b' and s[index-1] == 'o' and s[index-2] == 'b':
        occurs += 1
    index += 1

print('Number of times bob occurs is:', occurs)
    
