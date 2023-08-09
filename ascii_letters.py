#ascii_letters.py
'''
*****
*****
*****
*****
*****
'''
ascii_letters = {
        'A' : ['  *  ', ' * * ', '*****', '*   *', '*   *'],
        'B' : ['**** ', '*   *', '*****', '*   *', '**** '],
        'C' : ['*****', '*    ', '*    ', '*    ', '*****'],
        'D' : ['**** ', '*   *', '*   *', '*   *', '**** '],
        'E' : ['*****', '*    ', '**** ', '*    ', '*****']}

def print_letter(char):
    for slide in ascii_letters[char]:
        print(slide)

if __name__ == '__main__':
    for key in ascii_letters.keys():
        print_letter(key)
        print()
