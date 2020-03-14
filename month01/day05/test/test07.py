"""
Test07
    将英文语句进行反转
    How are you->>you are How
"""
str_word = "How are you"
list_word = str_word.split()
word = " ".join(list_word[::-1])
print(word) 
