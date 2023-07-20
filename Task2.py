s = input('Please enter the word: ')
number = 0
letter = 0
for c in s:
    if c in ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9'):
        number += 1
    else:
        letter += 1
if number > 0 and letter > 0:
    print('MIXED')
elif number > 0 and letter == 0:
    print('NUMBER')
else:
    print('WORD')