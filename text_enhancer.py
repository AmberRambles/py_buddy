print('Welcome to text enhancer. Please enter something. Enter \'q\' to quit.')
prompt = '//'
input_string = ''
input_string = input(prompt)
while input_string != 'q':
  for char_index,character in enumerate(input_string[:]):
    input_string[char_index].insert('+')
    print(f'Current value: {character}')
  print('I say: {input_string}')
  input_string = input(prompt)