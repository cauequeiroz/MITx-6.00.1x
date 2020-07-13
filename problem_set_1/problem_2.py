s = 'obobooboboboboboobooboobbobbazbob'
occurs = 0

bob_str = ''
for letter in s:
    bob_str += letter

    if 'bob' in bob_str:
        occurs += 1
        bob_str = letter

print('Number of times bob occurs is:', occurs)
    
