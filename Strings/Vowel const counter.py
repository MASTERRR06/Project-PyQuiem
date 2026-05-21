input_str = input("Enter the word or sentence:\n")
vowels_count = 0
consonants_count = 0
vowels = "aeiouAEIOU"
uppercase_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lowercase_letters = "abcdefghijklmnopqrstuvwxyz"
for char in input_str:
    isLetter=False
    for upper in uppercase_letters:
        if char==upper:
            isLetter=True
            break

    if not isLetter:
        for lower in lowercase_letters:
            if char==lower:
                isLetter=True
                break

    if isLetter:
        vowel=False
        for v in vowels:
            if char==v:
                vowel=True
                break

        if vowel:
            vowels_count+=1
        else:
            consonants_count+=1

print("Vowels",vowels_count)
print("consonants",consonants_count)
