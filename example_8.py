char = input('Enter the letter: ')
#char = char.lower()

match char:
    case 'a':
        print(char,'is a vowel')
    case 'e':
        print(char, 'is a vowel')
    case 'i':
        print(char, 'is a vowel')
    case 'o':
        print(char, 'is a vowel')
    case 'u':
        print(char, 'is a vowel')
    case _:
        print(char,'is a consonant')




"""

char = input('Enter the letter: ')
vowels = ['a','e','i','o','u','A','E','I','O','U']

if char in vowels:
    print(char,'is a vowel')
else:
    print(char,'is a consonant')
    
"""