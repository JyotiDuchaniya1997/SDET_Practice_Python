str1='hello yes its me. lets do it'
vowels=['a','i','e','o','u']
vow=0
consonants =0
for ch in str1:
    if ch.lower() in vowels:
        vow += 1
    else:
        if ch.isalpha:
            consonants+=1
print(f"Vowels in '{str1}' is {vow} and consonants is {consonants}")