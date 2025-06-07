str1= "listen"
str2="Listen"
if sorted(str1.lower()) == sorted(str2.lower()):
    print('Both strings are anagrams')
else:
    print("Non Anagrams") 