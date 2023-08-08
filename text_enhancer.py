print('Welcome to text enhancer. Please enter something. Enter \'q\' to quit.')
prompt = '//'
special_char = '+'
input_string = ''
input_string = input(prompt)
while input_string != 'q':
    returnString = ''
    returnString += special_char
    for character in input_string:
        returnString += character
        returnString += special_char
    print(f'I say: {returnString}')
    input_string = input(prompt)
