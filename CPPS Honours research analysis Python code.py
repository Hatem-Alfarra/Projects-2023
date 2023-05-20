"""
Installation and importing pyperclip might be necessary to run this code.
This code is kept to how it is originally, even though, I have learned much more in computer science classes since
writing this code.
"""


# import pyperclip
import pyperclip


# x = input().lower()
# print(x != 'done')

# For the number of stains. If 2 assign the names of the proteins stained to variables
while True:
    stain_count = input('\nExcluding DAPI how many other stains are used (1 or 2): ')
    if stain_count == '1' or stain_count == '2':
        if stain_count == '2':

            print('\nWhat was stained:')
            stain1 = input('Stain 1: ')
            stain2 = input('Stain 2: ')
        break
    else:
        print("Please type either '1' or '2' ")

# Starting with control?
while True:
    ctr_first = input('\nAre you starting with the control? (y/n) ').lower()
    condition = 'Ctr'
    snap_number = 1
    if ctr_first == 'y' or ctr_first == 'n':
        if ctr_first == 'n':
            condition = input('Condition: ')
        break
    else:
        print("Type 'y' for yes and 'n' for no")

print("When done with the current condition type 'next condition'\n")

# x = input().lower()
snap_number = 1


while True:
    x = input().lower()

    if x == " ":
        if snap_number == 1:
            print(condition)
        if stain_count == '2':

            # assign string in the clipboard to the variable v
            v = pyperclip.paste()
            # the number of lines in the copied data
            nlines = v.count('\n')
            # finding the halfway line of the data
            half_lines = (nlines / 2) + 1
            # Changing the number assigned to half_lines to one with a line before it and a space after
            half_way = str('\n' + str(int(half_lines)) + '	')
            # fetching the position of the halfway string and returning its position
            half_way_position = v.find(half_way)

            print('Snap', snap_number, '\n' + stain1, '\n' + v[0:half_way_position] + '\n' + stain2 +
                  v[half_way_position:])

            snap_number += 1

        if stain_count == '1':
            # assign string in the clipboard to the variable v
            v = pyperclip.paste()

            print('Snap', snap_number, '\n', v)

            snap_number += 1

    elif x == "next condition":
        snap_number = 1
        condition = input('Condition: \n')
        if stain_count == '2':
            # assign string in the clipboard to the variable v
            v = pyperclip.paste()
            # the number of lines in the copied data
            nlines = v.count('\n')
            # finding the halfway line of the data
            half_lines = (nlines / 2) + 1
            # Changing the number assigned to half_lines to one with a line before it and a space after
            half_way = str('\n' + str(int(half_lines)) + '	')
            # fetching the position of the halfway string and returning its position
            half_way_position = v.find(half_way)

            print('Snap', snap_number, '\n' + stain1, '\n' + v[0:half_way_position] + '\n' + stain2 +
                  v[half_way_position:])

            snap_number += 1

        elif stain_count == '1':
            # assign string in the clipboard to the variable v
            v = pyperclip.paste()

            print('Snap', snap_number, '\n', v)

            snap_number += 1


