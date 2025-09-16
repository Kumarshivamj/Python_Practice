a = "I love My INDIA"
vowel ="aeiouAEIOU"
count_vowel= 0
count_consonant = 0
for i in a:
    if i in vowel:
        count_vowel = count_vowel+1
    else:
        count_consonant = count_consonant+1
print(f"{count_vowel} vowel are there in String")
print(f"{count_consonant} consonant are there in String")


