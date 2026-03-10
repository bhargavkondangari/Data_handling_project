l= "Belief comes from  truth, but identity is shadow to belief "

vowels ="aeiou"

count_vowels = {}

for char  in  l:
    if char in vowels:
        if char in count_vowels:
            count_vowels[char]+=1
        else:
            count_vowels[char] =1
print(count_vowels)