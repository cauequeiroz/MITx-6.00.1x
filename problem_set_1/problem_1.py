s = 'azcbobobegghakl'
vowels = ['a', 'e', 'i', 'o', 'u']
vowels_counter = 0

for letter in s:
    if letter in vowels:
        vowels_counter += 1

print('Number of vowels:', vowels_counter)
